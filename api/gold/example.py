import requests

res = requests.get("https://gold.api-sina-free.workers.dev/gold")
data = res.json()

print("💰 18K Gold:", data["gold_18_ayar"])
print("🥇 Emami Coin:", data["sekke_emami"])
print("⏱ Last Update:", data["updated_at"])
