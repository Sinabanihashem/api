import requests

API = "https://car.api-sina-free.workers.dev/cars?type=imported"

res = requests.get(API)
cars = res.json()["cars"]

for c in cars:
    print("🚘 Name:", c["name"])
    print("🏷 Brand:", c["brand"])
    print("💵 Market Price:", c["market_price"])
    print("📉 Change:", c["change_percent"])
    print("⏱ Updated:", c["last_update"])
    print("-" * 30)
