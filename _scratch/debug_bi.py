import urllib.request
import json
import ssl
import os

ssl_context = ssl._create_unverified_context()

def get_config():
    with open('config.json') as f:
        return json.load(f)

cfg = get_config()
active_cid = cfg.get("activeId")
company = next(c for c in cfg["companies"] if c["companyId"] == active_cid)
token = company["token"]

url = "https://bi-engine.sesametime.com/api/v3/analytics/report-query"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "csid": active_cid,
    "x-company-id": active_cid,
    "X-Region": "EU1",
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/"
}

query = {
    "from": "schedule_context_check",
    "select": [
        {"field": "schedule_context_check.date", "alias": "date"},
        {"field": "core_context_employee.id", "alias": "employeeId"},
        {"field": "core_context_employee.name", "alias": "employeeName"}
    ],
    "where": [
        {"field": "schedule_context_check.date", "operator": ">=", "value": "2026-04-01"},
        {"field": "schedule_context_check.date", "operator": "<=", "value": "2026-04-30"}
    ],
    "limit": 5
}

print(f"Testing BI for company {active_cid}...")
req = urllib.request.Request(url, data=json.dumps(query).encode(), headers=headers, method='POST')
try:
    with urllib.request.urlopen(req, context=ssl_context) as res:
        data = json.loads(res.read())
        print("✅ BI SUCCESS")
        print(json.dumps(data, indent=2)[:1000])
except Exception as e:
    print(f"❌ BI FAILED: {e}")
