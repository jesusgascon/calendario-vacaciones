import urllib.request
import urllib.error
import urllib.parse
import json
import os

with open("config.json") as f:
    config = json.load(f)

# Find active firm
active_id = config.get("activeId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
if not company:
    # try legacy format
    token = config.get("token")
    cid = config.get("companyId")
else:
    token = company["token"]
    cid = company["companyId"]

base_url = "https://back-eu1.sesametime.com"

endpoints = [
    f"/core/v3/employees",
    f"/api/v3/employees",
    f"/core/v3/presence",
    f"/schedule/v1/presence",
    f"/api/v3/work-entries",
    f"/core/v3/work-entries",
    f"/schedule/v1/work-entries",
    f"/api/v1/work-entries",
]

def check_endpoint(path, method="GET", query=""):
    url = base_url + path + query
    headers = {
        "Authorization": f"Bearer {token}",
        "csid": cid,
        "x-company-id": cid,
        "X-Sesame-Region": "eu1"
    }
    req = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            results = data.get("data", []) if isinstance(data, dict) else data
            print(f"✅ {method} {path} - 200 OK (Results: {len(results) if isinstance(results, list) else type(results)})")
    except urllib.error.HTTPError as e:
        print(f"❌ {method} {path} - {e.code}")
    except Exception as e:
        print(f"❌ {method} {path} - Error: {e}")

for ep in endpoints:
    check_endpoint(ep)

