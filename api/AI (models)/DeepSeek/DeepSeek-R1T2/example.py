import requests

text = "What is your name?"
url = f"https://deepseek.api-sina-free.workers.dev/?text={text}"

res = requests.get(url)
data = res.json()

print("👤 Creator:", data["creator"])
print("📡 Channel:", data["channel"])
print("🧠 Answer:", data["answer"])
