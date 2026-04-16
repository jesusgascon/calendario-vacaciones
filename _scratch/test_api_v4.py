import urllib.request
import urllib.error
import json

with open("config.json") as f:
    config = json.load(f)

active_id = config.get("activeId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")
cid = company["companyId"] if company else config.get("companyId")

endpoints = [
    f"/api/v3/companies/{cid}/employees/presence",
    f"/api/v3/companies/{cid}/presence",
    f"/api/v3/companies/{cid}/presence-status",
    f"/core/v3/companies/{cid}/work-entries",
    f"/schedule/v1/companies/{cid}/work-entries",
    f"/schedule/v1/work-entries",
    f"/api/v3/employees/{cid}/presence",
]

base_url = "https://back-eu1.sesametime.com"

def check(path, method="GET"):
    url = base_url + path
    headers = {
        "Authorization": f"Bearer {token}",
        "x-company-id": cid,
        "csid": cid,
    }
    req = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            data = r.read()
            print(f"✅ {method} {url} -> 200 OK")
    except urllib.error.HTTPError as e:
        print(f"❌ {method} {url} -> {e.code}")

for ep in endpoints:
    check(ep)

