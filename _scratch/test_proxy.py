import urllib.request
import urllib.error
import json

# Llama a nuestro proxy local para probarlo
url = "http://localhost:8765/sesame-api/api/v3/employees/ab1b2a7e-b921-4e5e-b5d8-d3b54ea7e5a0/checks?from=2026-04-01&to=2026-04-30&limit=2000"
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as r:
        res = json.loads(r.read().decode())
        print(f"Proxy SUCCESS: {len(res.get('data',[]))} checks")
except urllib.error.HTTPError as e:
    print(f"Proxy FAILED: {e.code} {e.reason}")
