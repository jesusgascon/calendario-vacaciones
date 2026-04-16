import urllib.request
import urllib.error
import json

with open("config.json") as f:
    config = json.load(f)

companies = config.get("companies", [])
if not companies:
    # Handle simple config case
    companies = [{"companyId": config.get("companyId"), "token": config.get("token"), "name": "Default"}]

url = "https://bi-engine.sesametime.com/api/v3/analytics/report-query"

for company in companies:
    cid = company.get("companyId")
    token = company.get("token")
    name = company.get("name", cid)
    
    headers = {
        "Authorization": f"Bearer {token}",
        "x-company-id": cid,
        "csid": cid,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://app.sesametime.com",
        "Referer": "https://app.sesametime.com/",
        "Accept": "application/json, text/plain, */*",
    }

    payload = {
        "moduleName": "work-entries",
        "limit": 5,
        "columns": ["id"]
    }

    req = urllib.request.Request(url, headers=headers, method="POST", data=json.dumps(payload).encode())
    print(f"Testing Company: {name} (ID: {cid[:8]}...)")
    try:
        with urllib.request.urlopen(req) as r:
            print("  ✅ 200 OK")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        if "Request forbidden by administrative rules" in body:
            print(f"  ❌ {e.code} Forbidden (WAF Blocked)")
        else:
            print(f"  ❌ {e.code} Error: {body[:100]}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

