import urllib.request
import urllib.error
import json

with open("config.json") as f:
    config = json.load(f)

active_id = config.get("activeId") or config.get("companyId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")

headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": active_id,
    "csid": active_id,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
}

# Try simple list of work entries
url = f"https://back-eu1.sesametime.com/api/v3/work-entries?limit=50&from=2026-04-14&to=2026-04-16"
try:
    req = urllib.request.Request(url, headers=headers, method='GET')
    with urllib.request.urlopen(req) as r:
        res = json.loads(r.read().decode())
        data = res.get('data', [])
        print(f"✅ Simple List SUCCESS! Got {len(data)} records.")
        if len(data) > 0:
            print(f"   Sample ID: {data[0].get('employeeId')}")
            others = [d for d in data if d.get('employeeId') != "ab1b2a7e-b921-4e5e-b5d8-d3b54ea7e5a0"]
            print(f"   Others found: {len(others)}")
except urllib.error.HTTPError as e:
    print(f"❌ Simple List FAILED: {e.code}")
