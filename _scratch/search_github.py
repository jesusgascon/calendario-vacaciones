import urllib.request
import json
import urllib.parse

def search_repo(query):
    print(f"\n--- Searching GitHub for: {query} ---")
    url = "https://api.github.com/search/code?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github.v3+json"})
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            items = data.get("items", [])
            paths = set()
            for it in items[:15]:
                repo = it["repository"]["full_name"]
                path = it["path"]
                score = it.get("score", 0)
                print(f"[{repo}] {path}")
    except Exception as e:
         print("Error:", e)

search_repo("sesametime.com/api/v3")
search_repo("api.sesametime.com")
search_repo("schedule/v1/work-entries")

