#!/usr/bin/env python3
"""Sync shorts.yaml -> Cloudflare 301 redirect rules for the short domain.

Source of truth: shorts.yaml at the wiki root. This script parses it,
validates it, and either emits the Cloudflare ruleset JSON (--emit-json) or
pushes it to the zone's http_request_dynamic_redirects phase (--apply).

Auth for --apply: env CF_API_TOKEN (token with Zone:Rules Edit + Zone:Zone
Read). Zone is resolved by name from CF_ZONE (default: the registry `domain`).
Stdlib only.

Usage:
  python3 sync.py                 # validate + summary
  python3 sync.py --emit-json     # print ruleset JSON (manual dashboard import)
  python3 sync.py --apply         # push to Cloudflare (requires CF_API_TOKEN)
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


def build_rules(domain, target_base, redirects):
    # Dashboard-native "Redirect Rules" (zone phase http_request_redirect).
    # NOTE: the older dynamic-redirects phase is deprecated; Bulk Redirects is
    # the 950-rule upgrade path (needs account-level ruleset) if we outgrow
    # the free plan's static redirect quota (10/zone).
    rules = []
    for code, path in redirects:
        uri = "/" + code if code else "/"
        target = target_base + ("/" + path if path else "/")
        if code:
            expr = (
                f'http.host eq "{domain}" and '
                f'http.request.uri.path eq "{uri}"'
            )
        else:
            expr = f'http.host eq "{domain}"'
        rules.append({
            "action": "redirect",
            "expression": expr,
            "action_parameters": {
                "status_code": 301,
                "preserve_query_string": False,
                "redirect_from_value": {
                    "source": f"https://{domain}{uri}",
                    "target": {"type": "static", "value": target},
                },
            },
            "description": f"rcpts short: {uri} -> {path or 'wiki home'}",
        })
    return rules


def cf_api(method, endpoint, token, body=None, strict=True):
    url = "https://api.cloudflare.com/client/v4/" + endpoint.lstrip("/")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + token)
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
        sys.exit(f"Cloudflare API error: {out.get('errors')}")
    return out["result"]


def apply_rules(domain, rules):
    token = os.environ.get("CF_API_TOKEN")
    if not token:
        sys.exit("CF_API_TOKEN not set — cannot apply")
    zones = cf_api(
        "GET",
        f"zones?name={urllib.parse.quote(domain)}",
        token,
    )
    if not zones:
        sys.exit(f"no Cloudflare zone found for {domain} "
                 "(add the domain to your Cloudflare account first)")
    zone_id = zones[0]["id"]
    body = {
        "name": "rcpts short links",
        "description": f"Synced from research-wiki shorts.yaml "
                       f"({len(rules)} rules). Do not edit in dashboard.",
        "phase": "http_request_redirect",
        "rules": rules,
    }
    # Preferred: zone phase entrypoint (Rulesets API, redirect phase is not
    # creatable as a bare zone ruleset).
    out = cf_api(
        "POST",
        f"zones/{zone_id}/rulesets/phases/http_request_redirect/entrypoint",
        token, body, strict=False,
    )
    if out.get("success"):
        r = out["result"]
        print(f"pushed ruleset {r['id']} to zone {domain} entrypoint "
              f"({len(rules)} redirect rules)")
        return
    first_err = out.get("errors")
    # Fallback: account-level ruleset bound to the zone (needs CF_ACCOUNT_ID
    # and an account-scoped token).
    account_id = os.environ.get("CF_ACCOUNT_ID")
    if account_id:
        out2 = cf_api(
            "POST", f"accounts/{account_id}/rulesets", token,
            dict(body, zone_id=zone_id), strict=False,
        )
        if out2.get("success"):
            r = out2["result"]
            print(f"pushed account ruleset {r['id']} bound to zone {domain} "
                  f"({len(rules)} redirect rules)")
            return
        sys.exit(f"both push paths failed.\nzone entrypoint: {first_err}\n"
                 f"account ruleset: {out2.get('errors')}")
    sys.exit(f"zone entrypoint push failed: {first_err}\n"
             "(if the entrypoint is rejected, set repo variable CF_ACCOUNT_ID "
             "and use an account-scoped token)")


def main():
    domain, target_base, redirects = parse_registry()
    errors = validate(domain, target_base, redirects)
    if errors:
        print("REGISTRY ERRORS:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    named = [c for c, _ in redirects if c]
    print(f"ok: {len(named)} codes + root on {domain} -> {target_base}")
    rules = build_rules(domain, target_base, redirects)
    args = sys.argv[1:]
    if "--emit-json" in args:
        print(json.dumps(
            {"phase": "http_request_redirect", "rules": rules}, indent=2))
    if "--apply" in args:
        apply_rules(domain, rules)


if __name__ == "__main__":
    main()
