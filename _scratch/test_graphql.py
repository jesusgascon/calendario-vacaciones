import urllib.request
import urllib.parse
import json

with open("config.json") as f:
    config = json.load(f)

active_id = config.get("activeId")
company = next((c for c in config.get("companies", []) if c["companyId"] == active_id), None)
token = company["token"] if company else config.get("token")
cid = company["companyId"] if company else config.get("companyId")

url = "https://api-eu1.sesametime.com/graphql"

query = """
query IntrospectionQuery {
  __schema {
    queryType { name }
    mutationType { name }
    types {
      ...FullType
    }
  }
}
fragment FullType on __Type {
  kind
  name
  fields(includeDeprecated: true) {
    name
  }
}
"""

headers = {
    "Authorization": f"Bearer {token}",
    "x-company-id": cid,
    "csid": cid,
    "Content-Type": "application/json"
}

req = urllib.request.Request(url, headers=headers, method="POST", data=json.dumps({"query": query}).encode())
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        types = data["data"]["__schema"]["types"]
        query_type = next((t for t in types if t["name"] == "Query"), None)
        if query_type and "fields" in query_type and query_type["fields"]:
            for f in query_type["fields"]:
                if "presence" in f["name"].lower() or "entry" in f["name"].lower() or "check" in f["name"].lower() or "work" in f["name"].lower():
                    print("- " + f["name"])
        else:
            print("No query fields found.")
except Exception as e:
    print(f"Error: {e}")

