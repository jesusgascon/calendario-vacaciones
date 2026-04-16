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

url = "https://back-eu1.sesametime.com/api/v3/employees?limit=5"
headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json"
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        print("Success!")
        if data.get("data") and len(data["data"]) > 0:
            print("Fields first user:", list(data["data"][0].keys()))
            if "status" in data["data"][0]:
                print("Status:", data["data"][0]["status"])
        else:
            print("No data.")
except urllib.error.HTTPError as e:
    print(f"❌ {e.code}")
    print(e.read().decode()[:500])

