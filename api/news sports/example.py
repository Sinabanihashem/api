import requests

res = requests.get("https://sports.api-sina-free.workers.dev/sports")
data = res.json()

for item in data["data"]:
    print("⚽", item["title"])
    print("🆔", item["id"])
    if item["media"]["video"]:
        print("🎥 Video:", item["media"]["video"])
    print("-" * 40)
