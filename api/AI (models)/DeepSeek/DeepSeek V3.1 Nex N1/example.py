import requests

text = "What is artificial intelligence?"
url = f"https://deepseek-v3.api-sina-free.workers.dev/?text={text}"

res = requests.get(url, timeout=15)
data = res.json()

print("👤 Creator:", data["creator"])
print("📡 Channel:", data["channel"])
print("🧠 Answer:", data["answer"])
