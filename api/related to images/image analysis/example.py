import requests

# File upload
with open("test.png", "rb") as f:
    res = requests.post("https://image-analysis.api-sina-free.workers.dev/", files={"image": f})

print(res.json())

# Direct URL
url = "https://image-analysis.api-sina-free.workers.dev/?url=https://example.com/test.png"
res = requests.get(url)
print(res.json())
