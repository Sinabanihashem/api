# 📖 SinaStoryAPI version : 1.0.0

وب‌سرویس **SinaStoryAPI** یک سرویس ساده و سبک برای دریافت **داستان‌های کوتاه رندوم فارسی** است ✨  
این API برای استفاده در **ربات‌ها، اپلیکیشن‌ها و وب‌سایت‌ها و...** طراحی شده و  
فقط با یک درخواست GET، یک داستان تصادفی دریافت می‌کنید — **بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://dastan.api-sina-free.workers.dev

---

## 📥 ورودی وب‌سرویس

این وب‌سرویس **هیچ ورودی‌ای ندارد**  
هر درخواست، یک داستان رندوم برمی‌گرداند.

---

## 📦 خروجی وب‌سرویس

| کلید | نوع | توضیح |
|----|----|------|
| `status` | `boolean` | وضعیت موفق بودن درخواست |
| `dev` | `object` | اطلاعات توسعه‌دهنده |
| `dev.channel` | `string` | کانال رسمی API |
| `dev.creator` | `string` | سازنده سرویس |
| `result` | `string` | متن داستان رندوم |

---

## 🧪 نمونه درخواست

```http
GET https://dastan.api-sina-free.workers.dev
```

---

# 🧾 نمونه خروجی

```json
{
  "status": true,
  "dev": {
    "channel": "@Sinabani_api",
    "creator": "@Sinabanis"
  },
  "result": "پدر سیلی محکمی به صورت پسر زد و گفت: مگه این شام چه عیبی دارد که لب نمی زنی؟ پسر در حالی که به نون و پنیر و مقداری سبزی چشم دوخته بود از پای سفره به گوشه ای خزید و سر بر بالین نهاد. صبح وقتی غذای پسر در بقچه پدر جای می گرفت، پسرک دانست امروز پدر صبحانه دارد و چشمانش از شادی تر شد."
}
```

---

# 💻 نمونه استفاده در Python

```py
import requests

res = requests.get("https://dastan.api-sina-free.workers.dev")
data = res.json()

if data["status"]:
    print("📖 داستان رندوم:\n")
    print(data["result"])
```

---

# 🤖 استفاده در ربات‌ها / (Rubika Bot)

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_story_bot")

API_URL = "https://dastan.api-sina-free.workers.dev"

def get_story():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "داستان":
        data = get_story()
        if not data or not data.get("status"):
            return await message.reply("❌ خطا در دریافت داستان")

        await message.reply(
            f"📖 *داستان رندوم:*\n\n{data['result']}",
            parse_mode="markdown"
        )

bot.run()
```

---

# 🎯 ویژگی‌ها

✅ داستان رندوم در هر درخواست
✅ بدون نیاز به API Key
✅ مناسب ربات‌ها و اپلیکیشن‌ها
✅ خروجی JSON تمیز و ساده
✅ کاملاً RESTful


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                      
🗳 Rubika: https://rubika.ir/Sinabani_api                    
🔗 Endpoint: https://dastan.api-sina-free.workers.dev

---

---

# 📖 SinaStoryAPI version : 1.0.0

**SinaStoryAPI** is a lightweight and simple web service for retrieving **random Persian short stories** ✨  
This API is designed for use in **bots, mobile apps, and websites**  
With just one GET request, you receive a random story — **No API key required** 🚀

---

## 🌐 API Endpoint

https://dastan.api-sina-free.workers.dev

---

## 📥 API Input

This API **does not require any input parameters**  
Each request returns a new random story.

---

## 📦 API Response

| Key | Type | Description |
|----|----|-------------|
| `status` | `boolean` | Request success status |
| `dev` | `object` | Developer information |
| `dev.channel` | `string` | Official API channel |
| `dev.creator` | `string` | Service creator |
| `result` | `string` | Random story text |

---

## 🧪 Sample Request

```http
GET https://dastan.api-sina-free.workers.dev
```

---

# 🧾 Sample Response

```json
{
  "status": true,
  "dev": {
    "channel": "@Sinabani_api",
    "creator": "@Sinabanis"
  },
  "result": "پدر سیلی محکمی به صورت پسر زد و گفت: مگه این شام چه عیبی دارد که لب نمی زنی؟ پسر در حالی که به نون و پنیر و مقداری سبزی چشم دوخته بود از پای سفره به گوشه ای خزید و سر بر بالین نهاد. صبح وقتی غذای پسر در بقچه پدر جای می گرفت، پسرک دانست امروز پدر صبحانه دارد و چشمانش از شادی تر شد."
}
```

---

# 💻 Python Usage Example

```py
import requests

res = requests.get("https://dastan.api-sina-free.workers.dev")
data = res.json()

if data["status"]:
    print("📖 Random Story:\n")
    print(data["result"])
```

---

# 🤖 Bots / Usage (Rubika Bot)

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_story_bot")

API_URL = "https://dastan.api-sina-free.workers.dev"

def get_story():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.lower() == "story":
        data = get_story()
        if not data or not data.get("status"):
            return await message.reply("❌ Failed to fetch story")

        await message.reply(
            f"📖 *Random Story:*\n\n{data['result']}",
            parse_mode="markdown"
        )

bot.run()
```

---

# 🎯 Features

✅ Random story on each request
✅ No API key required
✅ Ideal for bots and applications
✅ Clean and simple JSON response
✅ Fully RESTful


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                   
🗳 Rubika: https://rubika.ir/Sinabani_api               
🔗 Endpoint: https://dastan.api-sina-free.workers.dev
