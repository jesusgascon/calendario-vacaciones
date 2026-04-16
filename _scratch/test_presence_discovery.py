import urllib.request
import urllib.error
import json
import ssl

# Ignorar verificación SSL si es necesario
ssl_context = ssl._create_unverified_context()

def test_endpoint(url, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req, context=ssl_context) as response:
            data = json.loads(response.read().decode('utf-8'))
            items = data.get('data', [])
            if isinstance(items, dict): # A veces es { items: [] }
                items = items.get('items', [])
            
            count = len(items) if isinstance(items, list) else (1 if items else 0)
            return True, count, data
    except Exception as e:
        return False, 0, str(e)

with open("config.json") as f:
    config = json.load(f)

token = config.get("token")
company_id = config.get("companyId")
base_url = config.get("backendUrl", "https://back-eu1.sesametime.com")

start = "2026-04-01"
end = "2026-04-30"

endpoints = [
    f"{base_url}/api/v3/statistics/daily-computed-hour-stats?from={start}&to={end}",
    f"{base_url}/api/v3/attendance/presence",
    f"{base_url}/api/v3/statistics/summary?from={start}&to={end}",
    f"{base_url}/api/v3/work-entries/search?limit=1000&from={start}&to={end}",
    f"{base_url}/api/v3/attendance/work-entries/search?limit=1000&from={start}&to={end}",
    f"{base_url}/api/v3/employees/presence"
]

print(f"Testing {len(endpoints)} endpoints for team discovery...")
for url in endpoints:
    success, count, data = test_endpoint(url, token)
    status = "✅ SUCCESS" if success else "❌ FAIL"
    print(f"{status} | Found {count} recs | URL: {url}")
    if success and count > 1:
        print(f"  --> POTENTIAL TEAM ENDPOINT DETECTED!")
    elif not success:
        print(f"  Error: {data}")

