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

# 1. Fetch 'me' to get employeeId
req = urllib.request.Request("https://back-eu1.sesametime.com/api/v3/security/me", headers=headers)
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        me_id = data.get("data", {}).get("employee", {}).get("id")
        print(f"Me ID: {me_id}")
except Exception as e:
    print(f"Error ME: {e}")
    me_id = ""

endpoints = [
    f"/schedule/v1/work-entries?employeeId={me_id}",
    f"/project/v1/time-entries?employeeId={me_id}",
    f"/api/v3/work-entries?employeeId={me_id}",
    f"/core/v3/work-entries?employeeId={me_id}",
]

for ep in endpoints:
    url = "https://api-eu1.sesametime.com" + ep
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            print(f"✅ GET {url} -> 200 OK")
            print(r.read().decode()[:100])
    except urllib.error.HTTPError as e:
        print(f"⚠️  GET {url} -> {e.code}")

