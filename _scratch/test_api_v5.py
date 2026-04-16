import urllib.request
import urllib.error
import urllib.parse
import json

with open("config.json") as f:
    config = json.load(f)

active_id = config.get("activeId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")
cid = company["companyId"] if company else config.get("companyId")

endpoints = [
    f"/project/v1/time-entries",
    f"/schedule/v1/work-entries",
    f"/api/v3/work-entries",
    f"/api/v3/checks",
    f"/core/v3/presence"
]

methods = ["GET", "POST"]
base_urls = ["https://back-eu1.sesametime.com", "https://api-eu1.sesametime.com", "https://api.sesametime.com"]

for base in base_urls:
    for ep in endpoints:
        for method in methods:
            url = base + ep
            headers = {
                "Authorization": f"Bearer {token}",
                "x-company-id": cid,
                "csid": cid,
                "Content-Type": "application/json"
            }
            req = urllib.request.Request(url, headers=headers, method=method, data=b"{}" if method == "POST" else None)
            try:
                with urllib.request.urlopen(req) as r:
                    print(f"✅ {method} {url} -> 200 OK")
            except urllib.error.HTTPError as e:
                # 405 means route exists but wrong method. 403 means auth or permissions but route exists!
                # 422 means invalid body, route exists.
                if e.code in [403, 405, 422, 500, 400, 401]:
                     print(f"⚠️  {method} {url} -> {e.code}")
            except Exception as e:
                pass

