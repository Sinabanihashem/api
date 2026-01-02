import requests

API = "https://football.api-sina-free.workers.dev/news"

res = requests.get(API, timeout=10)
data = res.json()

for news in data["data"]:
    print(news["title"])
