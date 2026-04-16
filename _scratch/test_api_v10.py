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

endpoints = [
    "https://api.sesametime.com/api/v3/work-entries",
    "https://back-eu1.sesametime.com/api/v3/work-entries",
    "https://app.sesametime.com/api/v3/work-entries",
    "https://app.sesametime.com/graphql",
]

for url in endpoints:
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            print(f"✅ GET {url} -> 200 OK")
    except urllib.error.HTTPError as e:
        print(f"⚠️  GET {url} -> {e.code}")

