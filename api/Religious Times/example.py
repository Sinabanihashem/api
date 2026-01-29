import requests

API = "https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=Mashhad"

res = requests.get(API, timeout=10)
data = res.json()

print(data["data"]["prayer_times"]["out"]["Maghrib"])
