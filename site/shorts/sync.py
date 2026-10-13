#!/usr/bin/env python3
"""Sync shorts.yaml -> Cloudflare Bulk Redirects (rcpts.link 301s).

Ground truth (verified 2026-10-13 against the live API + CF OpenAPI):
- Zone-level redirect phase is dead for new zones ("phase http_request_redirect
  not allowed at zone level"); the zone entrypoint rejects it too.
- Account-level `http_request_redirect` rulesets accept ONLY list-based
  (`from_list`) redirect rules — i.e. Bulk Redirects. `from_value` is rejected
  at account level.
So this script uploads the whole registry as one Bulk Redirect list (CSV) and
points a single account-entrypoint rule at it. Both endpoints are
account-scoped and work with an API token:

  1. POST /accounts/{CF_ACCOUNT_ID}/rulesets/bulk_redirects?filename=<name>.csv
     raw CSV body (no header):
     source_url,target_url,status_code,include_subpath,preserve_query_string
     Re-uploading the same filename replaces the list.
  2. PUT  /accounts/{CF_ACCOUNT_ID}/rulesets/phases/http_request_redirect/entrypoint
     body {name, description, rules:[{action: redirect,
            expression: http.request.full_uri in $<list_id>,
            action_parameters: {from_list: {name, key}}}]}
     Falls back to POST /accounts/{id}/rulesets kind=root if the entrypoint
     does not exist yet.

Auth env: CF_API_TOKEN (Account Rules and Filters: Edit), CF_ACCOUNT_ID.
Stdlib only.

Usage:
  python3 sync.py                 # validate + summary
  python3 sync.py --emit-json     # print CSV + rule JSON (manual import)
  python3 sync.py --apply         # push to Cloudflare
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REGISTRY = os.path.join(REPO_ROOT, "shorts.yaml")
CODE_RE = re.compile(r"^[a-z0-9]{3,12}$")
LIST_NAME = "rcpts_short"          # ^[a-zA-Z0-9_]+$ — matches filename stem
LIST_FILE = LIST_NAME + ".csv"


def parse_registry(path=REGISTRY):
    """Tiny parser for the deliberately simple registry format.

    Returns (domain, target_base, [(code, path), ...]).
    """
    domain = target_base = None
    redirects = []
    in_list = False
    pending = {}
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.startswith("domain:"):
                domain = stripped.split(":", 1)[1].strip()
                continue
            if stripped.startswith("target_base:"):
                target_base = stripped.split(":", 1)[1].strip().rstrip("/")
                continue
            if stripped.startswith("redirects:"):
                in_list = True
                continue
            if not in_list:
                continue
            if stripped.startswith("- "):
                if pending:
                    redirects.append(pending)
                pending = {}
                stripped = stripped[2:].strip()
            if ":" in stripped:
                key, val = stripped.split(":", 1)
                val = val.strip().strip('"').strip("'")
                pending[key.strip()] = val
    if pending:
        redirects.append(pending)
    return domain, target_base, [
        (r.get("code", ""), r.get("path", "")) for r in redirects
    ]


def validate(domain, target_base, redirects):
    errors = []
    if not domain or not target_base:
        errors.append("registry missing domain/target_base")
    seen = set()
    for code, path in redirects:
        if code == "":
            if path != "":
                errors.append(f"root code must have empty path, got {path!r}")
            continue
        if not CODE_RE.match(code):
            errors.append(f"bad code {code!r} (need lowercase [a-z0-9], 3-12 chars)")
        if code in seen:
            errors.append(f"duplicate code {code!r}")
        seen.add(code)
        if path:
            md = os.path.join(REPO_ROOT, path + ".md")
            if not os.path.isfile(md):
                errors.append(f"code {code!r} -> missing page {path}.md")
        else:
            errors.append(f"code {code!r} has empty path")
    return errors


def build_rows(domain, target_base, redirects):
    """[(source_url, target_url), ...] — one per registry entry.

    Sources carry the host, so matching is host-specific without any extra
    expression gate.
    """
    rows = []
    for code, path in redirects:
        source = f"https://{domain}/" + (code if code else "")
        target = target_base + ("/" + path if path else "/")
        rows.append((source, target))
    return rows


def build_csv(rows):
    return "".join(
        f"{src},{tgt},301,false,false\n" for src, tgt in rows
    ).encode()


def build_rule(list_id):
    return {
        "action": "redirect",
        "expression": f"http.request.full_uri in ${list_id}",
        "action_parameters": {
            "from_list": {"name": LIST_NAME, "key": "http.request.full_uri"},
        },
        "description": f"rcpts short links (bulk list {LIST_NAME})",
    }


def cf_api(method, endpoint, token, body=None, strict=True):
    url = "https://api.cloudflare.com/client/v4/" + endpoint.lstrip("/")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Content-Type", "application/json")
    req.add_header("CF-API-Version", "2")
    return _send(req, method, endpoint, strict)


def cf_raw_post(endpoint, token, body_bytes, content_type):
    url = "https://api.cloudflare.com/client/v4/" + endpoint.lstrip("/")
    req = urllib.request.Request(url, data=body_bytes, method="POST")
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Content-Type", content_type)
    req.add_header("CF-API-Version", "2")
    return _send(req, "POST", endpoint, strict=True)


def _send(req, method, endpoint, strict):
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            out = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        if not strict:
            return {"success": False, "errors": [{"http": e.code, "body": detail}]}
        sys.exit(f"Cloudflare HTTP {e.code} on {method} {endpoint}:\n{detail}")
    if not out.get("success"):
        if not strict:
            return out
        sys.exit(f"Cloudflare API error: {out.get('errors')}")
    return out.get("result", out)


def apply_registry(domain, target_base, redirects):
    token = os.environ.get("CF_API_TOKEN")
    account_id = os.environ.get("CF_ACCOUNT_ID")
    if not token:
        sys.exit("CF_API_TOKEN not set — cannot apply")
    if not account_id:
        sys.exit("CF_ACCOUNT_ID not set (repo variable) — account endpoints "
                 "require it")
    rows = build_rows(domain, target_base, redirects)
    # 1) Upload the bulk redirect list (same filename replaces prior list).
    result = cf_raw_post(
        f"accounts/{account_id}/rulesets/bulk_redirects"
        f"?filename={urllib.parse.quote(LIST_FILE)}",
        token, build_csv(rows), "text/csv",
    )
    list_id = result.get("id") or result.get("list_id")
    print(f"uploaded bulk list {LIST_FILE} id={list_id} "
          f"valid={result.get('numValid')} "
          f"existing={result.get('numAlreadyExist')}")
    if not list_id:
        sys.exit(f"upload succeeded but no list id in response: {result}")
    # 2) Point the account entrypoint at the list.
    body = {
        "name": "rcpts short links",
        "description": f"Synced from research-wiki shorts.yaml "
                       f"({len(rows)} entries). Do not edit in dashboard.",
        "rules": [build_rule(list_id)],
    }
    out = cf_api(
        "PUT",
        f"accounts/{account_id}/rulesets/phases/http_request_redirect/entrypoint",
        token, body, strict=False,
    )
    if out.get("success"):
        r = out["result"]
        print(f"entrypoint ruleset {r['id']} updated ({len(rows)} redirects live)")
        return
    # Entrypoint may not exist yet -> create the phase ruleset directly.
    out2 = cf_api(
        "POST", f"accounts/{account_id}/rulesets", token,
        dict(body, kind="root", phase="http_request_redirect"), strict=False,
    )
    if out2.get("success"):
        r = out2["result"]
        print(f"created account ruleset {r['id']} ({len(rows)} redirects live)")
        return
    sys.exit(f"list uploaded OK (id={list_id}) but ruleset push failed.\n"
             f"entrypoint PUT: {out.get('errors')}\n"
             f"ruleset POST: {out2.get('errors')}")


def main():
    domain, target_base, redirects = parse_registry()
    errors = validate(domain, target_base, redirects)
    if errors:
        print("REGISTRY ERRORS:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    named = [c for c, _ in redirects if c]
    rows = build_rows(domain, target_base, redirects)
    print(f"ok: {len(named)} codes + root on {domain} -> {target_base}")
    args = sys.argv[1:]
    if "--emit-json" in args:
        print(json.dumps({
            "bulk_list_filename": LIST_FILE,
            "csv": build_csv(rows).decode(),
            "rule_template": build_rule("<LIST_ID>"),
        }, indent=2))
    if "--apply" in args:
        apply_registry(domain, target_base, redirects)


if __name__ == "__main__":
    main()
