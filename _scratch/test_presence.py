from curl_cffi import requests
import json

with open("config.json") as f:
    config = json.load(f)
cid = config.get("activeId") or config.get("companyId")
company = next((c for c in config.get("companies", []) if c["companyId"] == cid), None)
token = company["token"] if company else config.get("token")

url = "https://back-eu1.sesametime.com/api/v3/presence-status"
headers = {"Authorization": f"Bearer {token}", "csid": cid, "x-company-id": cid}

try:
    res = requests.get(url, headers=headers, impersonate="chrome110")
    print(f"Status: {res.status_code}")
    print(res.text[:200])
except Exception as e:
    print(e)
