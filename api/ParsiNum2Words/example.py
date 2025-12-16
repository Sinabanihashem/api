import requests

url = "https://number.api-sina-free.workers.dev/123456789"
response = requests.get(url)

print(response.json())
