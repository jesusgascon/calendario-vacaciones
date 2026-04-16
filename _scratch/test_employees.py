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
    "User-Agent": "Mozilla/5.0",
}

# Fetch company employees
url = f"https://back-eu1.sesametime.com/api/v3/companies/{cid}/employees?limit=5"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        print(f"Company Employees => length: {len(data['data'])}")
        if len(data['data']) > 0:
             print("Keys:", list(data['data'][0].keys()))
             obj = data['data'][0]
             if 'presenceStatus' in obj or 'attendanceStatus' in obj or 'status' in obj:
                 print("Found presence inside employees!")
                 print("Status node:", obj.get('presenceStatus'), obj.get('attendanceStatus'), obj.get('status'))
except Exception as e:
    print(f"Error CE: {e}")

