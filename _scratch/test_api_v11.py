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
    "https://app.sesametime.com/api/v3/presence",
    "https://app.sesametime.com/api/v3/statistics/presence",
    "https://app.sesametime.com/api/v3/contact-directory",
    "https://app.sesametime.com/api/v3/checks/search",
    "https://app.sesametime.com/api/v3/work-entries/search",
]

for url in endpoints:
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
             print(f"✅ GET {url} -> 200")
             print(r.read().decode()[:100])
    except urllib.error.HTTPError as e:
        print(f"⚠️  GET {url} -> {e.code}")

