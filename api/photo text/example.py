import requests

url = "https://photo-text.api-sina-free.workers.dev/Hello"
response = requests.get(url)

with open("hello.png", "wb") as f:
    f.write(response.content)

print("🖼 Image saved")
