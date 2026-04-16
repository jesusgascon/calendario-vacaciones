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
    f"/schedule/v1/work-entries",
    f"/api/v3/work-entries",
    f"/core/v3/work-entries",
    f"/project/v1/time-entries",
    f"/project/v1/projects"
]

methods = ["GET"]
base_urls = ["https://api-eu1.sesametime.com", "https://api.sesametime.com"]

for base in base_urls:
    for ep in endpoints:
        for method in methods:
            url = base + ep
            headers = {
                "Authorization": f"Bearer {token}",
                "x-company-id": cid,
                "csid": cid,
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Origin": "https://app.sesametime.com",
                "Referer": "https://app.sesametime.com/",
            }
            req = urllib.request.Request(url, headers=headers, method=method)
            try:
                with urllib.request.urlopen(req) as r:
                    print(f"✅ {method} {url} -> 200 OK")
            except urllib.error.HTTPError as e:
                print(f"⚠️  {method} {url} -> {e.code}")

