# ⚽ Football News API
### نسخه: Football API v1.0.0

وب‌سرویس **Football News API** یک API سریع، سبک و بدون نیاز به API Key برای  
📰 **دریافت آخرین اخبار فوتبال** است.

این سرویس جدیدترین اخبار مرتبط با فوتبال را از منابع معتبر خبری ورزشی جمع‌آوری کرده و  
خروجی استاندارد و ساخت‌یافته **JSON** ارائه می‌دهد.

🔹 اجرا شده روی **Cloudflare Workers**  
🔹 مناسب ربات‌ها، وب‌سایت‌ها و اپلیکیشن‌های موبایل  
🔹 ارائه عنوان خبر، خلاصه، تصویر و شناسه یکتا  

---

## 🧠 نحوه کار API (Architecture)

1️⃣ کلاینت درخواست دریافت اخبار را ارسال می‌کند  
2️⃣ Worker اطلاعات اخبار فوتبال را از منبع خبری دریافت می‌کند  
3️⃣ داده‌ها پردازش، استانداردسازی و پاک‌سازی می‌شوند  
4️⃣ خروجی نهایی به صورت JSON بازگردانده می‌شود  

---

## 🌐 آدرس اصلی وب‌سرویس

https://football.api-sina-free.workers.dev/news

---

## 🔗 Endpoint

### 🔹 دریافت آخرین اخبار فوتبال

```http
GET /news
```
> این Endpoint نیازی به ارسال پارامتر ندارد.

---

## 📦 ساختار خروجی API

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": [
    {
      "id": "1573915",
      "title": "عنوان خبر",
      "subtitle": "خلاصه یا توضیح کوتاه خبر",
      "image": "https://example.com/image.jpg"
    }
  ]
}
```

---

## 🧾 توضیح فیلدهای خروجی

| فیلد | نوع | توضیح |
|------|-----|-------|
| `channel` | `string` | نام کانال یا منبع انتشار API |
| `creator` | `string` | نام توسعه‌دهنده API |
| `data` | `array` | لیست اخبار فوتبال |
| `id` | `string` | شناسه یکتای خبر |
| `title` | `string` | عنوان خبر |
| `subtitle` | `string` | توضیح کوتاه یا خلاصه خبر |
| `image` | `string` | لینک تصویر خبر (ممکن است خالی باشد) |


---

# 🧪 نمونه درخواست

```http
GET https://football.api-sina-free.workers.dev/news
```

---

# 🧾 نمونه خروجی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": [
    {
      "id": "1573915",
      "title": "تراکتور با پیشنهاد بهتر در آستانه ربودن گزینه پرسپولیس",
      "subtitle": "پیگیری‌ها نشان می‌دهد مذاکرات برای جذب این بازیکن آغاز شده است...",
      "image": "https://example.com/news.jpg"
    }
  ]
}
```

---


# ⚠️ مدیریت خطاها

| وضعیت | پیام |
|-------|------|
| 448 | خطا در دریافت اخبار فوتبال از منبع |
| 500 | خطای داخلی سرور |

### 🧾 نمونه خطا

```json
{
  "ok": false,
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": "خطا در دریافت اخبار فوتبال."
}
```

---

⚙️ ویژگی‌ها

✅ بدون نیاز به API Key

✅ دریافت سریع و سبک اخبار

✅ خروجی JSON استاندارد

✅ مناسب استفاده در Production

✅ RESTful و پایدار

✅ اجرا شده روی Cloudflare Workers


---

🎯 موارد استفاده

● ربات‌های خبری فوتبال

● وب‌سایت‌های ورزشی

● اپلیکیشن‌های موبایل

● داشبوردهای خبری

● پروژه‌های دانشجویی و حرفه‌ای


---

# 👤 Developer

### Mir Sina Banihashem

📍 Hosted on: Cloudflare Workers‌
🗳 Rubika: https://rubika.ir/Sinabani_api
🔗 API Endpoint: https://football.api-sina-free.workers.dev/news‌

---

---

# ⚽ Football News API
### Version: Football API v1.0.0

The **Football News API** is a fast, lightweight, and API-key-free web service for  
📰 **fetching the latest football news**.

This service collects the most recent football-related news from reliable Persian sports media sources and  
returns a clean, structured **JSON** response.

🔹 Hosted on **Cloudflare Workers**  
🔹 Suitable for bots, websites, and mobile apps  
🔹 Provides news title, subtitle, image, and unique ID  

---

## 🧠 API Architecture

1️⃣ Client sends a request to the API endpoint  
2️⃣ Worker fetches latest football news data  
3️⃣ News items are parsed and normalized  
4️⃣ Standard JSON response is returned  

---

## 🌐 Main API URL

https://football.api-sina-free.workers.dev/news

---

## 🔗 Endpoint

### 🔹 Get Latest Football News

```http
GET /news
```

> This endpoint does not require any query parameters.

---

## 📦 API Response Structure

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": [
    {
      "id": "1573915",
      "title": "News title",
      "subtitle": "News subtitle or summary",
      "image": "https://example.com/image.jpg"
    }
  ]
}
```

---

## 🧾 Response Fields Description

| Field | Type | Description |
|------|------|------------|
| `channel` | `string` | API publisher channel |
| `creator` | `string` | API developer |
| `data` | `array` | List of football news items |
| `id` | `string` | Unique news identifier |
| `title` | `string` | News title |
| `subtitle` | `string` | Short news summary |
| `image` | `string` | News image URL (can be empty) |


---

# 🧪 Example Request

```http
GET https://football.api-sina-free.workers.dev/news
```

---

# 🧾 Example Response

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": [
    {
      "id": "1573915",
      "title": "Tractor close to stealing Persepolis target",
      "subtitle": "Reports indicate negotiations are underway in Dubai...",
      "image": "https://www.example.com/news-image.jpg"
    }
  ]
}
```

---

# ⚠️ Error Handling

| Status | Message |
|--------|--------|
| 448 | Error fetching football news source |
| 500 | Internal server error |

### 🧾 Example Error

```json
{
  "ok": false,
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": "Failed to fetch football news."
}
```

---

# 💻 Python Example

```py
import requests

API = "https://football.api-sina-free.workers.dev/news"

res = requests.get(API, timeout=10)
data = res.json()

for news in data["data"]:
    print(news["title"])
```

---

# 💻 Node.js Example

```js
const API = "https://football.api-sina-free.workers.dev/news";

async function getNews() {
  const res = await fetch(API);
  const data = await res.json();
  console.log(data.data);
}

getNews();
```

---

# 🤖 Use in Bots (Rubika)

```py
import requests

API = "https://football.api-sina-free.workers.dev/news"

res = requests.get(API, timeout=10)
data = res.json()

news = data["data"][0]

text = f"""
⚽ {news['title']}

📰 {news['subtitle']}
"""

print(text)
```

---

# ⚙️ Features

✅ No API Key required

✅ Fast and lightweight

✅ Latest football news

✅ Clean and normalized JSON

✅ Ready for production use

✅ RESTful structure

✅ Hosted on Cloudflare Workers


---

# 🎯 Use Cases

● Football news bots

● Sports websites

● Mobile sports apps

● Live news dashboards

● Monitoring and aggregation tools

● Student and professional projects


---

# 👤 Developer

### Mir Sina Banihashem

📍 Hosted on: Cloudflare Workers
🗳 Rubika: https://rubika.ir/Sinabani_api
🔗 API Endpoint: https://football.api-sina-free.workers.dev/news
