# 📱 Myket App Search API
### Version: Myket API v1.0.0

وب‌سرویس **Myket App Search API** یک API سریع، سبک و بدون نیاز به API Key برای  
🔍 **جستجوی اپلیکیشن‌ها در مایکت** است.

این سرویس با دریافت **نام اپلیکیشن** و سایر پارامترها، اطلاعات کامل اپ‌ها را از سایت **مایکت** جمع‌آوری کرده و  
خروجی استاندارد **JSON** برمی‌گرداند.

🔹 اجرا شده روی **Cloudflare Workers**                  
🔹 مناسب ربات‌ها، وب‌سایت‌ها و اپلیکیشن‌ها                  
🔹 پشتیبانی از جزئیات کامل اپ‌ها، لینک دانلود و اسکرین‌شات‌ها                       

---

## 🧠 نحوه کار API (Architecture)

1️⃣ کاربر نام اپلیکیشن و پارامترها را ارسال می‌کند                   
2️⃣ Worker اطلاعات را از صفحه جستجوی مایکت دریافت می‌کند                      
3️⃣ جزئیات اپلیکیشن شامل نام، package، icon، لینک و توضیحات جمع‌آوری می‌شود                         
4️⃣ خروجی JSON استاندارد برگردانده می‌شود                          

---

## 🌐 آدرس اصلی وب‌سرویس

https://myket.api-sina-free.workers.dev/

---

## 🔗 Endpoint

### 🔹 جستجوی اپلیکیشن‌ها

GET /

#### پارامترهای Query

| پارامتر | نوع | الزامی | توضیح |
|---------|----|------|------|
| `text`  | `string` | ✅ | نام اپلیکیشن یا کلمه کلیدی جستجو |
| `lang`  | `string` | ✅ | زبان نتایج (`fa`, `en` و غیره) |
| `count` | `number` | ✅ | تعداد نتایج در هر صفحه |
| `page`  | `number` | ❌ | شماره صفحه نتایج (پیش‌فرض 1) |
| `sort`  | `string` | ❌ | نوع مرتب‌سازی (`newest`, `popular`) |
| `format`| `string` | ❌ | حالت خروجی (`lite` یا `full`) |

---

## 📦 ساختار خروجی API

### حالت lite

```json
{
  "ok": true,
  "channel": "@Sinabani_api",
  "writer": "@Sinabanis",
  "count": 10,
  "data": [
    {
      "name": "Example App",
      "package": "com.example.app",
      "icon": "https://static.myket.ir/icon.png",
      "link": "https://myket.ir/app/com.example.app",
      "download": "https://myket.ir/dl?packageName=com.example.app"
    }
  ]
}
```
### حالت full

```json
{
  "ok": true,
  "channel": "@Sinabani_api",
  "writer": "@Sinabanis",
  "count": 10,
  "data": [
    {
      "name": "Example App",
      "package": "com.example.app",
      "icon": "https://static.myket.ir/icon.png",
      "link": "https://myket.ir/app/com.example.app",
      "download": "https://myket.ir/dl?packageName=com.example.app",
      "description": "توضیحات کامل اپلیکیشن",
      "screenshots": [
        "https://static.myket.ir/screenshot1.png",
        "https://static.myket.ir/screenshot2.png"
      ]
    }
  ]
}
```

---

# 🧪 نمونه درخواست ساده

```http
GET https://myket.api-sina-free.workers.dev/?text=تلگرام&lang=fa&count=10&page=1&sort=popular&format=full
```

---

# 🧾 نمونه خروجی

```json
{
  "ok": true,
  "channel": "@Sinabani_api",
  "writer": "@Sinabanis",
  "count": 10,
  "data": [
    {
      "name": "تلگرام",
      "package": "org.telegram.messenger",
      "icon": "https://static.myket.ir/icon.png",
      "link": "https://myket.ir/app/org.telegram.messenger",
      "download": "https://myket.ir/dl?packageName=org.telegram.messenger",
      "description": "پیام‌رسان تلگرام با امکانات کامل...",
      "screenshots": [
        "https://static.myket.ir/screenshot1.png",
        "https://static.myket.ir/screenshot2.png"
      ]
    }
  ]
}
```

---

# ⚠️ مدیریت خطاها

### وضعیت	پیام

400	پارامتر text یا lang یا count ارسال نشده یا نامعتبر
448	خطا در دریافت اطلاعات از مایکت
500	خطای داخلی سرور



---

# 💻 استفاده کامل در Python

```py
import requests

API = "https://myket.api-sina-free.workers.dev/"

def search_app(text, lang="fa", count=10, page=1, sort="", format="full"):
    params = {
        "text": text,
        "lang": lang,
        "count": count,
        "page": page,
        "sort": sort,
        "format": format
    }
    res = requests.get(API, params=params, timeout=10)
    data = res.json()
    return data

apps = search_app("تلگرام")
print(apps)
```

---

# 💻 استفاده کامل در Node.js

```js
const API = "https://myket.api-sina-free.workers.dev/";

async function searchApp(text) {
  const params = new URLSearchParams({
    text,
    lang: "fa",
    count: 10,
    page: 1,
    sort: "popular",
    format: "full"
  });
  const res = await fetch(`${API}?${params}`);
  const data = await res.json();
  console.log(data);
}

searchApp("تلگرام");
```

---

# 🤖 استفاده در ربات Rubika

```py
from rubpy import Client, filters
import requests

bot = Client(name="myket_bot")
API = "https://myket.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()
    if not text.lower().startswith("مایکت"):
        return

    query = text[6:].strip()
    if not query:
        return await message.reply("❗ لطفاً نام اپلیکیشن را وارد کنید.")

    try:
        res = requests.get(API, params={
            "text": query,
            "lang": "fa",
            "count": 1,
            "format": "full"
        }, timeout=10)
        data = res.json()
    except Exception as e:
        return await message.reply(f"❌ خطا در ارتباط با سرور:\n{e}")

    if not data.get("ok"):
        return await message.reply(f"❌ خطا: {data.get('data')}")

    apps = data.get("data", [])
    if not apps:
        return await message.reply("❌ اپلیکیشنی پیدا نشد.")

    app = apps[0]

    name = app.get("name", "-")
    description = app.get("description", "-")
    screenshots_count = len(app.get("screenshots", []))
    download = app.get("download", "-")
    icon = app.get("icon", "")

    text_reply = (
        f"📝 **{name}**\n\n"
        f"📂 توضیحات:\n{description}\n\n"
        f"🖼 تعداد اسکرین‌شات‌ها: {screenshots_count}\n"
        f"⬇️ [دانلود]({download})"
    )

    if icon:
        await message.reply_photo(photo=icon, caption=text_reply, parse_mode="markdown")
    else:
        await message.reply(text_reply, parse_mode="markdown")

bot.run()
```

---

# ⚙️ ویژگی‌ها

✅ بدون API Key

✅ جستجوی سریع و سبک

✅ پشتیبانی از نام اپ و کلمات کلیدی

✅ امکان مرتب‌سازی نتایج (sort)

✅ پشتیبانی از حالت کامل و خلاصه (format)

✅ جمع‌آوری جزئیات واقعی اپ‌ها (description, screenshots)

✅ کامل و مناسب Production , RESTful

✅ اجرا شده روی Cloudflare Workers


---

# 🎯 موارد استفاده

● ربات‌های جستجوی اپلیکیشن

● وب‌سایت‌های نقد و بررسی اپ‌ها

● داشبوردهای مدیریت اپ‌ها

● اپلیکیشن‌های موبایل

● ابزارهای مانیتورینگ مایکت

● پروژه‌های دانشجویی و حرفه‌ای


---

# 👤 Developer

### mir sina banihashem

📍 Hosted on: Cloudflare Workers
🗳 Rubika: https://rubika.ir/Sinabani_api
🔗 API Endpoint: https://myket.api-sina-free.workers.dev/
