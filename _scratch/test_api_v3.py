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

endpoints = [
    ("https://back-eu1.sesametime.com/core/v3/work-entries/search", "POST"),
    ("https://back-eu1.sesametime.com/api/v3/attendance/search", "POST"),
    ("https://back-eu1.sesametime.com/api/v3/time-entries", "GET"),
    ("https://back-eu1.sesametime.com/api/v3/time-entries/search", "POST"),
    ("https://back-eu1.sesametime.com/api/v3/statistics/presence/search", "POST"),
    ("https://back-eu1.sesametime.com/api/v3/presence", "GET"),
    ("https://back-eu1.sesametime.com/core/v3/presence", "GET"),
    ("https://back-eu1.sesametime.com/core/v3/attendance", "GET"),
    ("https://back-eu1.sesametime.com/api/v3/presence-status", "GET"),
    ("https://api-eu1.sesametime.com/core/v3/work-entries", "GET"),
    ("https://api-eu1.sesametime.com/schedule/v1/work-entries", "GET")
]

req_body = json.dumps({"limit": 50}).encode()

def check(url, method):
    headers = {
        "Authorization": f"Bearer {token}",
        "x-company-id": cid,
        "csid": cid,
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(url, headers=headers, method=method, data=req_body if method=="POST" else None)
    try:
        with urllib.request.urlopen(req) as r:
            data = r.read()
            # print(data)
            print(f"✅ {method} {url} -> 200 OK")
    except urllib.error.HTTPError as e:
        print(f"❌ {method} {url} -> {e.code}")

for ep, method in endpoints:
    check(ep, method)

