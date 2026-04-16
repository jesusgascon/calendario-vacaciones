import urllib.request
import urllib.error
import urllib.parse
import json

with open("config.json") as f:
    config = json.load(f)

active_id = config.get("activeId") or config.get("companyId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")

headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": active_id,
    "csid": active_id,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
}

bases = ["https://back-eu1.sesametime.com", "https://api-eu1.sesametime.com"]
paths = [
    f"/api/v3/companies/{active_id}/checks",
    f"/api/v3/employees/checks",
    f"/schedule/v1/checks",
    f"/schedule/v1/companies/{active_id}/checks",
    f"/core/v3/checks",
    f"/core/v3/companies/{active_id}/checks",
]

qs = "?from=2026-03-26&to=2026-05-06&includeOut=true"

for b in bases:
    for p in paths:
        url = b + p + qs
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as r:
                print(f"✅ FOUND IT! {url} -> 200 OK")
                print(r.read().decode()[:200])
        except urllib.error.HTTPError as e:
            if e.code not in [404, 405]:
                print(f"⚠️  {url} -> {e.code}")
