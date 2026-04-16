import urllib.request
import urllib.error
import json
import ssl

ssl_context = ssl._create_unverified_context()

def test_route(path, token):
    url = f"https://api-eu1.sesametime.com{path}" # Probar con el gateway oficial
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    print(f"Testing {url}...", end=" ")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=5) as response:
            print(f"✅ Success! Status: {response.status}")
            return True
    except urllib.error.HTTPError as e:
        print(f"❌ Failed: {e.code}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Nota: El token lo sacaremos del config.json del usuario si existe, 
# o simularemos la petición para ver si al menos el 'route_not_found' cambia a '401' (lo que indicaría que la ruta EXISTE)

routes = [
    "/schedule/v1/work-entries",
    "/attendance/v1/work-entries",
    "/core/v3/work-entries",
    "/api/v3/work-entries",
    "/api/v3/attendance/work-entries",
    "/core/v3/employees"
]

for r in routes:
    test_route(r, "dummy_token")
