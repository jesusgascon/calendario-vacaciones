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

# Fetch presence to get some employee IDs
url_presence = "https://back-eu1.sesametime.com/api/v3/work-entries/presence"
req_presence = urllib.request.Request(url_presence, headers=headers)
try:
    with urllib.request.urlopen(req_presence) as r:
        presences = json.loads(r.read().decode())['data']
        print(f"Got {len(presences)} presences.")
        emp_ids = [p['employee']['id'] for p in presences[:5]]
except Exception as e:
    print(f"Presence failed: {e}")
    emp_ids = ["ab1b2a7e-b921-4e5e-b5d8-d3b54ea7e5a0"] # default

# Now test checks for these employees
for emp_id in emp_ids:
    url = f"https://back-eu1.sesametime.com/api/v3/employees/{emp_id}/checks?from=2026-03-26&to=2026-05-06&includeOut=true"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            res = json.loads(r.read().decode())
            print(f"✅ Success for emp {emp_id}: {len(res.get('data',[]))} checks")
    except urllib.error.HTTPError as e:
        print(f"❌ Failed for emp {emp_id}: {e.code} {e.reason}")
