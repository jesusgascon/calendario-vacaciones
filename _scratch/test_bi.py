import urllib.request
import urllib.error
import json

with open("config.json") as f:
    config = json.load(f)

cid = config.get("activeId") or config.get("companyId")
company = next((c for c in config.get("companies", []) if c["companyId"] == cid), None)
token = company["token"] if company else config.get("token")

url = "https://bi-engine.sesametime.com/api/v3/analytics/report-query"

headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/",
    "Accept": "application/json, text/plain, */*",
}

payload = {
    "moduleName": "work-entries",
    "limit": 50,
    "columns": ["id"]
}

req = urllib.request.Request(url, headers=headers, method="POST", data=json.dumps(payload).encode())
try:
    with urllib.request.urlopen(req) as r:
        print("✅ 200 OK")
        print(len(r.read()))
except urllib.error.HTTPError as e:
    print(f"❌ {e.code}")
    print(e.read().decode()[:500])

