import urllib.request
import urllib.parse
import json

with open("config.json") as f:
    config = json.load(f)

active_id = config.get("activeId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")
cid = company["companyId"] if company else config.get("companyId")

url = "https://back-eu1.sesametime.com/graphql"
headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/"
}

query = "{ __typename }"
req = urllib.request.Request(url, headers=headers, method="POST", data=json.dumps({"query": query}).encode())

try:
    with urllib.request.urlopen(req) as r:
        print(r.read().decode())
except Exception as e:
    if hasattr(e, 'read'):
        print(e.read().decode())
    print(f"Error: {e}")

