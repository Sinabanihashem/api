import requests
from datetime import datetime

API_URL = "https://dollar.api-sina-free.workers.dev/dollar"

def fetch_dollar():
    try:
        data = requests.get(API_URL, timeout=5).json()

        price_toman = data["price_toman"]
        price_rial = data["price_rial"]
        updated_at = data["updated_at"]
        source = data.get("source", "tgju.org")

        time_str = datetime.fromisoformat(updated_at.replace("Z", "+00:00")) \
                          .strftime("%Y-%m-%d %H:%M:%S")

        print(f"💰 Toman: {price_toman:,} T")
        print(f"💵 Rial:  {int(price_rial):,} R")
        print(f"⏱ Updated: {time_str}")
        print(f"🌐 Source: {source}")

    except Exception:
        print("Error connecting or fetching data.")

fetch_dollar()
