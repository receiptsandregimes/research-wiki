#!/usr/bin/env python3
"""Sync shorts.yaml -> Cloudflare Bulk Redirects (rcpts.link 301s).

Documented flow (developers.cloudflare.com/rules/url-forwarding/
bulk-redirects/create-api/, Aug 2026 — verified live):

  1. POST /accounts/{CF_ACCOUNT_ID}/rules/lists
       {name, description, kind: "redirect"}          # create once, reuse
  2. POST /accounts/{acct}/rules/lists/{list_id}/items  # async, poll
       [{redirect: {source_url, target_url, status_code, ...}}, ...]
     plus GET items to prune entries no longer in the registry.
  3. Account ruleset on phase http_request_redirect with ONE rule:
       expression: http.request.full_uri in $<list_name>
       action_parameters.from_list: {name: <list_name>, key: full_uri}
     PUT .../rulesets/phases/http_request_redirect/entrypoint, fallback
     POST /accounts/{acct}/rulesets {kind: root, phase: ...}.

(Zone-level redirect rules are dead for new zones; account-level rules only
accept list-based `from_list`. The old CSV `rulesets/bulk_redirects` upload
endpoint does not accept API tokens.)

Auth env: CF_API_TOKEN (Account > Bulk URL Redirects: Edit OR Account Filter
Lists: Edit, plus Account Rulesets Write e.g. via Account Rules and Filters:
Edit), CF_ACCOUNT_ID. Stdlib only.

Usage:
  python3 sync.py                 # validate + summary
  python3 sync.py --emit-json     # print list/items/rule JSON (manual import)
  python3 sync.py --apply         # push to Cloudflare
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REGISTRY = os.path.join(REPO_ROOT, "shorts.yaml")
CODE_RE = re.compile(r"^[a-z0-9]{3,12}$")
LIST_NAME = "rcpts_short"   # ^[a-zA-Z0-9_]+$ — usable in rule expressions


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
    """[(source_url, target_url), ...] — sources carry the host."""
    rows = []
    for code, path in redirects:
        source = f"https://{domain}/" + (code if code else "")
        target = target_base + ("/" + path if path else "/")
        rows.append((source, target))
    return rows


def build_items(rows):
    return [
        {"redirect": {
            "source_url": src,
            "target_url": tgt,
            "status_code": 301,
            "subpath_matching": False,
            "preserve_query_string": False,
        }}
        for src, tgt in rows
    ]


def build_rule():
    return {
        "action": "redirect",
        "ref": LIST_NAME,
        "expression": f"http.request.full_uri in ${LIST_NAME}",
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
    if data is not None:
        req.add_header("Content-Type", "application/json")
    req.add_header("CF-API-Version", "2")
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
        sys.exit(f"Cloudflare API error on {method} {endpoint}: {out.get('errors')}")
    return out.get("result", out)


def wait_op(token, acct, op_id):
    """Poll an async list-items operation to completion."""
    for _ in range(60):
        st = cf_api("GET", f"accounts/{acct}/rules/lists/bulk_operations/{op_id}",
                    token)
        status = st.get("status")
        if status == "completed":
            return
        if status == "failed":
            sys.exit(f"list operation {op_id} failed: {st}")
        time.sleep(2)
    sys.exit(f"list operation {op_id} timed out")


def ensure_list(token, acct):
    lists = cf_api("GET",
                   f"accounts/{acct}/rules/lists?kind=redirect&per_page=100",
                   token)
    for l in lists or []:
        if l.get("name") == LIST_NAME:
            return l["id"]
    created = cf_api("POST", f"accounts/{acct}/rules/lists", token, {
        "name": LIST_NAME,
        "description": "rcpts.link short codes (synced from research-wiki "
                       "shorts.yaml). Do not edit in dashboard.",
        "kind": "redirect",
    })
    print(f"created redirect list {LIST_NAME} id={created['id']}")
    return created["id"]


def sync_items(token, acct, list_id, rows):
    current = cf_api("GET",
                     f"accounts/{acct}/rules/lists/{list_id}/items?per_page=1000",
                     token) or []
    cur_by_src = {}
    for it in current:
        src = (it.get("redirect") or {}).get("source_url")
        if src:
            cur_by_src[src] = it
    desired = {src: tgt for src, tgt in rows}

    stale_ids = [it.get("id") or it.get("item_id")
                 for src, it in cur_by_src.items() if src not in desired]
    if stale_ids:
        q = urllib.parse.quote(",".join(i for i in stale_ids if i))
        res = cf_api("DELETE",
                     f"accounts/{acct}/rules/lists/{list_id}/items?items={q}",
                     token)
        wait_op(token, acct, res["operation_id"])
        print(f"pruned {len(stale_ids)} stale entries")

    upsert = [
        item for item in build_items(rows)
        if (cur_by_src.get(item["redirect"]["source_url"], {}).get("redirect")
            or {}).get("target_url") != item["redirect"]["target_url"]
    ]
    if upsert:
        res = cf_api("POST", f"accounts/{acct}/rules/lists/{list_id}/items",
                     token, upsert)
        wait_op(token, acct, res["operation_id"])
        print(f"synced {len(upsert)} entries (added/changed)")
    else:
        print("list already current")


def push_ruleset(token, acct, n):
    body = {
        "name": "rcpts short links",
        "description": f"Synced from research-wiki shorts.yaml ({n} entries). "
                       "Do not edit in dashboard.",
        "rules": [build_rule()],
    }
    out = cf_api("PUT",
                 f"accounts/{acct}/rulesets/phases/http_request_redirect/entrypoint",
                 token, body, strict=False)
    if out.get("success"):
        print(f"entrypoint ruleset {out['result']['id']} updated "
              f"(list {LIST_NAME} live, {n} entries)")
        return
    out2 = cf_api("POST", f"accounts/{acct}/rulesets", token,
                  dict(body, kind="root", phase="http_request_redirect"),
                  strict=False)
    if out2.get("success"):
        print(f"created entrypoint ruleset {out2['result']['id']} "
              f"(list {LIST_NAME} live, {n} entries)")
        return
    sys.exit(f"list synced but ruleset push failed.\n"
             f"entrypoint PUT: {out.get('errors')}\n"
             f"ruleset POST: {out2.get('errors')}")


def apply_registry(domain, target_base, redirects):
    token = os.environ.get("CF_API_TOKEN")
    acct = os.environ.get("CF_ACCOUNT_ID")
    if not token:
        sys.exit("CF_API_TOKEN not set — cannot apply")
    if not acct:
        sys.exit("CF_ACCOUNT_ID not set (repo variable) — account endpoints "
                 "require it")
    rows = build_rows(domain, target_base, redirects)
    list_id = ensure_list(token, acct)
    sync_items(token, acct, list_id, rows)
    push_ruleset(token, acct, len(rows))


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
            "list": {"name": LIST_NAME, "kind": "redirect"},
            "items": build_items(rows),
            "rule": build_rule(),
        }, indent=2))
    if "--apply" in args:
        apply_registry(domain, target_base, redirects)


if __name__ == "__main__":
    main()
