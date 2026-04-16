from curl_cffi import requests
import json

with open("config.json") as f:
    config = json.load(f)
token = config.get("token")
cid = config.get("activeId") or config.get("companyId")

url = "https://bi-engine.sesametime.com/api/v3/analytics/report-query"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-ES,es;q=0.9,en;q=0.8",
    "authorization": f"Bearer {token}",
    "content-type": "application/json",
    "csid": cid,
    "origin": "https://app.sesametime.com",
    "priority": "u=1, i",
    "referer": "https://app.sesametime.com/",
    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "x-company-id": cid,
    "x-region": "EU1"
}

payload = {
    "from": "schedule_context_check",
    "select": [{"field": "schedule_context_check.date", "alias": "date"}],
    "limit": 5
}

res = requests.post(url, headers=headers, json=payload, impersonate="chrome110")
print("Status:", res.status_code)
print(res.text[:200])
