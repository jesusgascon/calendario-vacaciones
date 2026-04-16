import urllib.request
import urllib.error
import urllib.parse
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

paths = [
    "/api/v3/work-entries/search",
    "/api/v3/checks/search",
    "/api/v3/attendance/work-entries/search",
    "/api/v3/companies/{companyId}/work-entries/search"
]

payload = {
    "from": "2026-04-01",
    "to": "2026-04-30",
    "limit": 100
}

for path in paths:
    target_path = path.replace("{companyId}", active_id)
    url = f"https://back-eu1.sesametime.com{target_path}"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as r:
            res = json.loads(r.read().decode())
            data = res.get('data', [])
            print(f"✅ Success for {target_path}: Got {len(data)} entries")
            if len(data) > 0:
                print(f"   First entry employee: {data[0].get('employee', {}).get('firstName')} (ID: {data[0].get('employeeId')})")
                # Check if we see someone else
                others = [d for d in data if d.get('employeeId') != "ab1b2a7e-b921-4e5e-b5d8-d3b54ea7e5a0"]
                print(f"   Others found: {len(others)}")
    except urllib.error.HTTPError as e:
        print(f"❌ Failed for {target_path}: {e.code}")
