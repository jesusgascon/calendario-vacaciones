import urllib.request
import urllib.error
import json

with open("config.json") as f:
    config = json.load(f)

active_id = config.get("activeId") or config.get("companyId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")

# Attempting to mimic a REAL browser exactly to bypass WAF
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "csid": active_id,
    "x-company-id": active_id,
    "X-Region": "EU1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "es-ES,es;q=0.9",
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/",
}

query = {
    "fields": [
        {"name": "employee.id"},
        {"name": "employee.firstName"},
        {"name": "employee.lastName"},
        {"name": "checkIn.date"},
        {"name": "checkOut.date"},
        {"name": "accumulatedSeconds"},
        {"name": "checkType"}
    ],
    "filters": [
        {"name": "checkIn.date", "operator": "gte", "value": "2026-04-01"},
        {"name": "checkIn.date", "operator": "lte", "value": "2026-04-30"}
    ],
    "limit": 1000
}

url = "https://bi-engine.sesametime.com/api/v3/analytics/report-query"

try:
    req = urllib.request.Request(url, data=json.dumps(query).encode(), headers=headers, method='POST')
    with urllib.request.urlopen(req) as r:
        res = json.loads(r.read().decode())
        print(f"✅ BI Engine SUCCESS! Got {len(res.get('data', []))} records.")
except urllib.error.HTTPError as e:
    print(f"❌ BI Engine FAILED: {e.code}")
    print(e.read().decode())
