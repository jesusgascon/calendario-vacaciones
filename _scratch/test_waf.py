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

url = "https://bi-engine.sesametime.com/api/v3/analytics/report-query"

headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

payload = {
    "moduleName": "work-entries",
    "limit": 50
}

req = urllib.request.Request(url, headers=headers, method="POST", data=json.dumps(payload).encode())
try:
    with urllib.request.urlopen(req) as r:
        print("✅ 200 OK")
        # print(r.read()[:500])
except urllib.error.HTTPError as e:
    print(f"❌ {e.code}")
    print(e.read().decode()[:500])
except Exception as e:
    print(f"Error: {e}")

