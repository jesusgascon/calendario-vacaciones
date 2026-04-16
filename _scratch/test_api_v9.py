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

headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/",
}

req = urllib.request.Request("https://back-eu1.sesametime.com/api/v3/security/me", headers=headers)
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        me_id = data["employee"]["id"] if "employee" in data else data.get("id", "")
        # sometimes it returns a list if multiple roles? Let's trace
        if isinstance(data, list) and len(data) > 0:
            me_id = data[0].get("employee", {}).get("id", "")
        print(f"Me ID extracted: {me_id}")
except Exception as e:
    print(f"Error ME: {e}")
    me_id = ""

if me_id:
    url = f"https://api-eu1.sesametime.com/schedule/v1/work-entries?employeeId={me_id}&from=2026-04-01&to=2026-04-30"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            print(f"✅ GET {url} -> 200 OK")
    except urllib.error.HTTPError as e:
        print(f"⚠️  GET {url} -> {e.code}")
