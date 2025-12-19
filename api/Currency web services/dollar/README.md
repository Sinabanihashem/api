# 💸 SinaDollar API — نسخه 1.0.3

**SinaDollarAPI** یک وب‌سرویس سریع، سبک و دقیق برای دریافت **قیمت لحظه‌ای دلار آزاد** به **ریال** و **تومان** است.  
این سرویس مستقیماً از وب‌سایت معتبر **tgju.org** بروزرسانی می‌شود و برای:

- ربات‌ها 🤖
- وب‌اپلیکیشن‌ها 💻
- داشبوردهای مالی 📊
- اسکریپت‌ها و اپ‌های اندروید 📱

کاملاً مناسب است.

> ⚡ بدون نیاز به API Key — فقط یک درخواست GET

---

## 🌐 Endpoint

https://dollar.api-sina-free.workers.dev/dollar

---

## 📥 ورودی‌ها

| نوع درخواست | توضیح |
|-----------|--------|
| GET | بدون نیاز به پارامتر |

```http
GET https://dollar.api-sina-free.workers.dev/dollar
```

---

## 📤 خروجی (JSON)

| پارامتر | نوع | توضیح |
|--------|------|--------|
| `creator` | string | شناسه توسعه‌دهنده |
| `source` | string | منبع رسمی داده (tgju.org) |
| `price_rial` | string | قیمت دلار به ریال |
| `price_toman` | number | قیمت دلار به تومان |
| `updated_at` | string (ISODate) | آخرین زمان بروزرسانی |

---

## 🧾 نمونه خروجی

```json
{
  "creator": "@Sinabani_api",
  "source": "tgju.org",
  "price_rial": "1076400",
  "price_toman": 107640,
  "updated_at": "2025-11-01T10:29:37.201Z"
}
```

---

💻 نمونه استفاده در Python

```python
import requests
from datetime import datetime

API_URL = "https://dollar.api-sina-free.workers.dev/dollar"

def fetch_dollar():
    try:
        data = requests.get(API_URL, timeout=5).json()

        price_toman = data["price_toman"]
        price_rial = data["price_rial"]
        updated_at = data["updated_at"]
        source = data.get("source", "tgju.org")

        time_str = datetime.fromisoformat(updated_at.replace("Z", "+00:00")) \
                          .strftime("%Y-%m-%d %H:%M:%S")

        print(f"💰 به تومان: {price_toman:,} تومان")
        print(f"💵 به ریال:  {int(price_rial):,} ریال")
        print(f"⏱ بروزرسانی: {time_str}")
        print(f"🌐 منبع: {source}")

    except Exception:
        print("خطا در اتصال یا دریافت اطلاعات.")

fetch_dollar()
```

---

🤖 نمونه ربات روبیکا (Rubpy)

```python
from rubpy import Client, filters
import requests
from datetime import datetime

bot = Client(name="sina_dollar_bot")
API_URL = "https://dollar.api-sina-free.workers.dev/dollar"

@bot.on_message_updates(filters.text)
async def main(message):
    if message.text.strip() in ["دلار", "dollar", "Dollar"]:
        try:
            data = requests.get(API_URL, timeout=5).json()

            price_toman = data["price_toman"]
            price_rial = data["price_rial"]
            updated_at = data["updated_at"]
            source = data.get("source", "tgju.org")

            time_str = datetime.fromisoformat(updated_at.replace("Z", "+00:00")).strftime("%Y/%m/%d - %H:%M:%S")

            await message.reply(
                f"💸 قیمت لحظه‌ای دلار آزاد:\n\n"
                f"💰 تومان: {price_toman:,}\n"
                f"💵 ریال: {int(price_rial):,}\n\n"
                f"⏱ بروزرسانی: {time_str}\n"
                f"🌐 منبع: {source}"
            )

        except:
            await message.reply("⚠️ خطا در دریافت اطلاعات.")

bot.run()
```

---

## ⚙️ اطلاعات فنی

| ویژگی | مقدار |
|------|-------|
| **Method** | `GET` |
| **Response Type** | `JSON` |
| **Content-Type** | `application/json; charset=utf-8` |
| **Host** | Cloudflare Workers |
| **Source Provider** | tgju.org |
| **Rate Limit** | بدون محدودیت رسمی (light usage recommended) |
| **Authentication** | نیاز ندارد (`No API Key`) |          


---

## 👤 Developer

mir sina banihashem          
📍 Rubika: https://rubika.ir/Sinabani_api          
🔗 API Endpoint: https://dollar.api-sina-free.workers.dev/dollar          

---

---

# 💸 SinaDollar API — Version 1.0.3

**SinaDollarAPI** is a fast, lightweight, and accurate web service for retrieving the **real-time price of the USD (Free Market)** in both **Rial** and **Toman**.  
This service is directly updated from the reliable source **tgju.org**, making it perfect for:

- Bots 🤖  
- Web applications 💻  
- Financial dashboards 📊  
- Scripts & Android apps 📱  

> ⚡ No API Key required — just one simple GET request

---

## 🌐 Endpoint

https://dollar.api-sina-free.workers.dev/dollar

---

## 📥 Request

| Method | Description |
|--------|-------------|
| GET | No parameters required |

```http
GET https://dollar.api-sina-free.workers.dev/dollar
```

---

## 📤 Response (JSON)

| Parameter | Type | Description |
|-----------|-------|-------------|
| `creator` | string | Developer identifier |
| `source` | string | Official data provider (tgju.org) |
| `price_rial` | string | USD price in Rial |
| `price_toman` | number | USD price in Toman |
| `updated_at` | string (ISODate) | Last update timestamp |

---

## 🧾 Sample Response

```json
{
  "creator": "@Sinabani_api",
  "source": "tgju.org",
  "price_rial": "1076400",
  "price_toman": 107640,
  "updated_at": "2025-11-01T10:29:37.201Z"
}
```

---

# 💻 Python Example

```py
import requests
from datetime import datetime

API_URL = "https://dollar.api-sina-free.workers.dev/dollar"

def fetch_dollar():
    try:
        data = requests.get(API_URL, timeout=5).json()

        price_toman = data["price_toman"]
        price_rial = data["price_rial"]
        updated_at = data["updated_at"]
        source = data.get("source", "tgju.org")

        time_str = datetime.fromisoformat(updated_at.replace("Z", "+00:00")) \
                          .strftime("%Y-%m-%d %H:%M:%S")

        print(f"💰 Toman: {price_toman:,} T")
        print(f"💵 Rial:  {int(price_rial):,} R")
        print(f"⏱ Updated: {time_str}")
        print(f"🌐 Source: {source}")

    except Exception:
        print("Error connecting or fetching data.")

fetch_dollar()
```

---

# 🤖 Rubika Bot Example (Rubpy)

```py
from rubpy import Client, filters
import requests
from datetime import datetime

bot = Client(name="sina_dollar_bot")
API_URL = "https://dollar.api-sina-free.workers.dev/dollar"

@bot.on_message_updates(filters.text)
async def main(message):
    if message.text.strip() in ["dollar", "Dollar", "USD", "دلار"]:
        try:
            data = requests.get(API_URL, timeout=5).json()

            price_toman = data["price_toman"]
            price_rial = data["price_rial"]
            updated_at = data["updated_at"]
            source = data.get("source", "tgju.org")

            time_str = datetime.fromisoformat(updated_at.replace("Z", "+00:00")) \
                                .strftime("%Y/%m/%d - %H:%M:%S")

            await message.reply(
                f"💸 Real-time USD Free Market Rate:\n\n"
                f"💰 Toman: {price_toman:,}\n"
                f"💵 Rial: {int(price_rial):,}\n\n"
                f"⏱ Updated: {time_str}\n"
                f"🌐 Source: {source}"
            )

        except:
            await message.reply("⚠️ Error retrieving data.")

bot.run()
```

---

# ⚙️ Technical Info

Property	Value

Method	GET
Response Type	JSON
Content-Type	application/json; charset=utf-8
Host	Cloudflare Workers
Source Provider	tgju.org
Rate Limit	No official limit (light usage recommended)
Authentication	None required (No API Key)



---

# 👤 Developer

mir sina banihashem
📍 Rubika: https://rubika.ir/Sinabani_api                      
🔗 API Endpoint: https://dollar.api-sina-free.workers.dev/dollar
