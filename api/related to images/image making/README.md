# 🖼 SinaImageAPI — نسخه 1.0.0

**SinaImageAPI** یک سرویس ساده و سریع برای ساخت تصویر از روی متن است.  
هر توضیح فارسی یا انگلیسی که وارد کنید، یک تصویر مرتبط ساخته و مستقیماً به عنوان خروجی بازگردانده می‌شود.  
این API بدون هیچ کلید دسترسی و بدون نیاز به تنظیمات پیچیده قابل استفاده است.

---

## 🌐 آدرس درخواست

https://image.api-sina-free.workers.dev/generate?text=متن

---

## 🔎 پارامتر ورودی

| پارامتر | توضیح | ضرورات |
|--------|--------|--------|
| `text` | توضیح یا جمله‌ای که تصویر براساس اون ساخته بشه | اجباری |

---

## 📦 خروجی

خروجی این وب‌سرویس **مستقیماً تصویر** است (image/jpeg).  
خروجی JSON وجود نداره و نمیده.

---

## 🧪 نمونه درخواست

https://image.api-sina-free.workers.dev/generate?text=پرنده%20سفید%20زیبا

خروجی: تصویر JPEG

---

## 💻 نمونه استفاده در Python

```py
import requests

url = "https://image.api-sina-free.workers.dev/generate?text=blue futuristic city"

res = requests.get(url)

with open("image.jpg", "wb") as f:
    f.write(res.content)

print("Image saved!")
```

---

## 🤖 نمونه ربات روبیکا (Python)

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_image_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    txt = message.text.strip()

    if txt.startswith("عکس "):
        prompt = txt.replace("عکس ", "")
        link = f"https://image.api-sina-free.workers.dev/generate?text={prompt}"

        img = requests.get(link).content
        await message.reply_photo(photo=img)

bot.run()
```

---

# 🎯 ویژگی‌های سرویس

● استفاده آسان و سریع

● بدون نیاز به API Key

● خروجی مستقیم تصویر

● مناسب ربات، وب‌اپ، اسکریپت و پروژه‌های گرافیکی

● پشتیبانی کامل

---

# 👤 Developer

**mir sina banihashem**
📍 Hosted on Cloudflare Workers
🛠 Rubika: https://rubika.ir/Sinabani_api
🔗 Endpoint: https://image.api-sina-free.workers.dev/generate


---

---

# 🖼 SinaImageAPI — Version 1.0.0

SinaImageAPI is a simple and fast web service that generates an image based on any text you provide.
You can write a short or long description, and the service returns a picture related to it.
No API key required — no complex configuration needed.


---

# 🌐 Endpoint

https://image.api-sina-free.workers.dev/generate?text=your+text


---

# 🔎 Query Parameter

Parameter	Description	Required

text	The prompt or description for generating the image	✔ Yes



---

# 📦 Response

The API returns the image directly as image/jpeg.
No JSON, no wrapper — just the picture.


---

# 🧪 Example Request

https://image.api-sina-free.workers.dev/generate?text=futuristic neon city at night

Output: JPEG image.


---

# 💻 Example (Python)

```py
import requests

url = "https://image.api-sina-free.workers.dev/generate?text=golden dragon in the sky"

res = requests.get(url)

with open("result.jpg", "wb") as f:
    f.write(res.content)

print("Image saved!")
```

---

# 🤖 Rubika Bot Example

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_image_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    txt = message.text.strip()

    if txt.lower().startswith("image "):
        prompt = txt.replace("image ", "")
        link = f"https://image.api-sina-free.workers.dev/generate?text={prompt}"

        img = requests.get(link).content
        await message.reply_photo(photo=img, caption="Image generated")

bot.run()
```

---

# 🎯 Features

● Fast and easy to use

● No API key required

● Direct image output

● Works with any programming language

● Suitable for bots, web apps, scripts, and automation

---

# 👤 Developer

**mir sina banihashem**
Hosted on Cloudflare Workers
Rubika: https://rubika.ir/Sinabani_api
API URL: https://image.api-sina-free.workers.dev/generate
