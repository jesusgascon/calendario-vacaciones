import urllib.request
import json

with open("config.json") as f:
    config = json.load(f)

cid = config.get("activeId") or config.get("companyId")
company = next((c for c in config.get("companies", []) if c["companyId"] == cid), None)
token = company["token"] if company else config.get("token")

url = "https://api-eu1.sesametime.com/graphql"
headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json",
    "Origin": "https://app.sesametime.com",
    "Referer": "https://app.sesametime.com/"
}

query = "query { __schema { queryType { name } } }"
payload = {"query": query}

req = urllib.request.Request(url, headers=headers, method="POST", data=json.dumps(payload).encode())
try:
    with urllib.request.urlopen(req) as r:
        print("✅", r.read().decode())
except Exception as e:
    if hasattr(e, 'read'):
         print(f"❌ {e.code}", e.read().decode())
    else:
         print(f"Error: {e}")

