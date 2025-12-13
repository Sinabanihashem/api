import requests

# Joke
jok_res = requests.get("https://jok.api-sina-free.workers.dev/jok")
jok_data = jok_res.json()
print("😂 Joke:", jok_data["result"])

# Fantasy Joke
fan_res = requests.get("https://jok.api-sina-free.workers.dev/fantezi")
fan_data = fan_res.json()
print("🎭 Fantasy Joke:", fan_data["result"])
