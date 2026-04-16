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

url = "https://back-eu1.sesametime.com/api/v3/analytics/report-query"

headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/",
    "Accept": "application/json, text/plain, */*",
}

req = urllib.request.Request(url, headers=headers, method="POST", data=b'{"moduleName":"work-entries","limit":50,"columns":["origin"]}')
try:
    with urllib.request.urlopen(req) as r:
        print("✅ 200 OK")
except urllib.error.HTTPError as e:
    print(f"❌ {e.code}")
    print(e.read().decode())
except Exception as e:
    print(f"Error: {e}")

