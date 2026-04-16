import urllib.request
import urllib.error
import json
import ssl

ssl_context = ssl._create_unverified_context()

def test_endpoint(url, token, company_id):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'x-company-id': company_id,
        'csid': company_id
    }
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req, context=ssl_context) as response:
            res_content = response.read().decode('utf-8')
            data = json.loads(res_content)
            
            # Navegación flexible por la respuesta
            items = data.get('data', [])
            if isinstance(items, dict):
                items = items.get('items', items.get('data', []))
            
            count = len(items) if isinstance(items, list) else 0
            
            # Ver IDs únicos detectados
            ids = set()
            if isinstance(items, list):
                for item in items:
                    eid = item.get('employeeId') or (item.get('employee') or {}).get('id')
                    if eid: ids.add(str(eid))
            
            return True, count, len(ids), data
    except Exception as e:
        return False, 0, 0, str(e)

with open("config.json") as f:
    config = json.load(f)

token = config.get("token")
company_id = config.get("companyId")
base_url = config.get("backendUrl", "https://back-eu1.sesametime.com")

start = "2026-04-01"
end = "2026-04-30"

# Candidatos con empresa inyectada en la ruta
endpoints = [
    f"{base_url}/api/v3/statistics/daily-computed-hour-stats?from={start}&to={end}",
    f"{base_url}/api/v3/attendance/presence",
    f"{base_url}/api/v3/companies/{company_id}/attendance/presence",
    f"{base_url}/api/v3/work-entries/search?limit=1000&from={start}&to={end}",
    f"{base_url}/api/v3/attendance/work-entries/search?limit=1000&from={start}&to={end}",
    f"{base_url}/api/v3/employees"
]

print(f"Testing {len(endpoints)} endpoints with Company headers...")
for url in endpoints:
    success, count, uniq_ids, data = test_endpoint(url, token, company_id)
    status = "✅ SUCCESS" if success else "❌ FAIL"
    if success:
        print(f"{status} | Found {count} items ({uniq_ids} uniq IDs) | URL: {url}")
        if uniq_ids > 1:
            print("  !!!! TEAM DISCOVERY SUCCESSFUL !!!!")
    else:
        print(f"{status} | Error: {data[:100]} | URL: {url}")

