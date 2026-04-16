from curl_cffi import requests
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
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/",
    "Accept": "application/json, text/plain, */*",
}

payload = {
    "moduleName": "work-entries",
    "limit": 50,
    "columns": ["id"]
}

try:
    # Use impersonation to spoof Chrome
    res = requests.post(url, headers=headers, json=payload, impersonate="chrome110")
    print(f"Status Code: {res.status_code}")
    print("Response snippet:", res.text[:200])
except Exception as e:
    print(f"Error: {e}")

