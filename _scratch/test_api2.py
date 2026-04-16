import urllib.request
import urllib.error
import json

with open("config.json") as f:
    config = json.load(f)

# Find active firm
active_id = config.get("activeId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")
cid = company["companyId"] if company else config.get("companyId")

endpoints = [
    "https://api.sesametime.com/schedule/v1/work-entries",
    "https://api.sesametime.com/schedule/v1/work-entries?limit=5",
    "https://api.sesametime.com/api/v3/work-entries",
    "https://back-eu1.sesametime.com/api/v3/presence",
    "https://api.sesametime.com/schedule/v1/presence",
]

def check(url):
    headers = {
        "Authorization": f"Bearer {token}",
        "x-company-id": cid,
        "csid": cid
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            print(f"✅ {url} -> 200 OK")
    except urllib.error.HTTPError as e:
        print(f"❌ {url} -> {e.code}")

for ep in endpoints:
    check(ep)

