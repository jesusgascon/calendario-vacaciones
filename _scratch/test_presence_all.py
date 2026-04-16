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

# Try the presence endpoint which is often used for the real-time team view
url = "https://back-eu1.sesametime.com/api/v3/work-entries/presence"
try:
    req = urllib.request.Request(url, headers=headers, method='GET')
    with urllib.request.urlopen(req) as r:
        res = json.loads(r.read().decode())
        print(f"✅ Presence Success! Got {len(res.get('data', []))} records.")
        if len(res.get('data', [])) > 0:
            p = res.get('data', [])[0]
            print(f"   Sample: {p.get('employee', {}).get('firstName')} - Status: {p.get('status')}")
except urllib.error.HTTPError as e:
    print(f"❌ Presence FAILED: {e.code}")

# Try the statistics endpoint
url = f"https://back-eu1.sesametime.com/api/v3/statistics/checks?from=2026-04-14&to=2026-04-16"
try:
    req = urllib.request.Request(url, headers=headers, method='GET')
    with urllib.request.urlopen(req) as r:
        res = json.loads(r.read().decode())
        print(f"✅ Statistics Success!")
except urllib.error.HTTPError as e:
    print(f"❌ Statistics FAILED: {e.code}")
