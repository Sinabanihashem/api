# 🏀 SinaSportsNewsAPI version : 1.0.0

وب‌سرویس **SinaSportsNewsAPI** یک API سریع و سبک برای دریافت **آخرین اخبار ورزشی** از منابع معتبر است 🔥  
این سرویس اطلاعات کامل هر خبر شامل تیتر، زیرتیتر، متن و رسانه‌های مرتبط (عکس و ویدیو) را ارائه می‌دهد  
**بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://sports.api-sina-free.workers.dev/sports

---

## 📥 ورودی وب‌سرویس

این API **هیچ ورودی یا پارامتری ندارد**  
با هر درخواست، لیست کامل اخبار ورزشی دریافت می‌شود 📊

---

## 📦 ساختار خروجی وب‌سرویس

| کلید | نوع | توضیح |
|-----|-----|--------|
| `channel` | `string` | شناسه کانال منتشرکننده |
| `creator` | `string` | نام توسعه‌دهنده |
| `data` | `array` | لیست کامل اخبار ورزشی |

---

## 📦 پارامترهای داخل `data`

| کلید | نوع | توضیح |
|-----|-----|--------|
| `id` | `string` `(UUID)` | شناسه یکتای خبر |
| `title` | `string` | عنوان یا تیتر اصلی خبر |
| `sub_title` | `string` \| `null` | زیرعنوان خبر (در صورت عدم وجود مقدار null است) |
| `media` | `object` | اطلاعات رسانه‌ای خبر |

---

## 🎬 پارامترهای داخل `media`

| کلید | نوع | توضیح |
|-----|-----|--------|
| `photo` | `string` | آدرس تصویر اصلی خبر |
| `thumbnail` | `string` | نسخه کوچک‌شده تصویر |
| `video` | `string` \| `null` | ویدیوی مرتبط با خبر (در صورت نبود، null) |
| `title` | `string` | متن یا توضیح خبر |
| `cover_image` | `string` \| `null` | تصویر کاور خبر (در صورت نبود، null) |

---

## 🧪 نمونه درخواست

`GET` https://sports.api-sina-free.workers.dev/sports

---

## 🧾 نمونه خروجی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": [
    {
      "id": "b0ac5451-b27c-48ea-aa4a-cfa0336c1a5d",
      "title": "گزارش بازی تراکتور و چادرملو؛ صدرنشین زیر سایه قهرمان!",
      "sub_title": null,
      "media": {
        "photo": "https://static.football360.ir/nesta2/media/posts_media/خلاصه_بازی_KOObpth_u9F64bn.jpg",
        "thumbnail": "https://static.football360.ir/nesta2/media/posts_media/thumbnails/کاور_گزارش_اختصاصی_تراکتور_چادرمولو__thumb.jpg",
        "video": "https://s3.ir-thr-at1.arvanstorage.ir/site-videos/Sadegh/تراکتور%20چادر.mp4",
        "title": "گزارش بازی تراکتور و چادرملو",
        "cover_image": "https://static.football360.ir/nesta2/media/posts_media/covers/کاور_گزارش_اختصاصی_تراکتور_چادرمولو_.jpg"
      }
    }
  ]
}
```

---

# 💻 نمونه استفاده در Python

```py
import requests

res = requests.get("https://sports.api-sina-free.workers.dev/sports")
data = res.json()

for item in data["data"]:
    print("⚽", item["title"])
    print("🆔", item["id"])
    if item["media"]["video"]:
        print("🎥 Video:", item["media"]["video"])
    print("-" * 40)
```

---

# 🤖 استفاده در ربات‌ها / Rubika
```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_sports_news_bot")

API_URL = "https://sports.api-sina-free.workers.dev/sports"

def get_sports_news():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "اخبار ورزشی":
        data = get_sports_news()
        if not data:
            return await message.reply("❌ خطا در دریافت اخبار ورزشی")

        news_list = data.get("data", [])
        if not news_list:
            return await message.reply("📭 خبری یافت نشد.")

        result = "⚽ *آخرین اخبار ورزشی:*\n\n"
        for item in news_list:
            result += f"🔸 {item['title']}\n"
            if item.get("sub_title"):
                result += f"▫️ {item['sub_title']}\n"
            if item["media"].get("video"):
                result += f"🎥 ویدیو: {item['media']['video']}\n"
            result += "\n"

        await message.reply(result[:4000], parse_mode="markdown")

bot.run()
```

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                    
🗳 Rubika: https://rubika.ir/Sinabani_api                  
🔗 Endpoint: https://sports.api-sina-free.workers.dev/sports

---

---

# 🏀 SinaSportsNewsAPI version : 1.0.0

**SinaSportsNewsAPI** is a fast and lightweight API for fetching the **latest sports news** from reliable sources 🔥  
This service provides full details for each news item, including headline, subtitle, text, and related media (images & videos)  
**No API key required** 🚀

---

## 🌐 API Endpoint

https://sports.api-sina-free.workers.dev/sports

---

## 📥 API Input

This API **does not require any input parameters**  
Each request returns the complete list of sports news 📊

---

## 📦 API Response Structure

| Key | Type | Description |
|-----|------|-------------|
| `channel` | `string` | Publisher channel identifier |
| `creator` | `string` | Developer username |
| `data` | `array` | Full list of sports news |

---

## 📦 Parameters inside `data`

| Key | Type | Description |
|-----|------|-------------|
| `id` | `string` (UUID) | Unique news identifier |
| `title` | `string` | Main news headline |
| `sub_title` | `string` \| null | News subtitle (null if not available) |
| `media` | `object` | Media-related information |

---

## 🎬 Parameters inside `media`

| Key | Type | Description |
|-----|------|-------------|
| `photo` | `string` | Main news image URL |
| `thumbnail` | `string` | Thumbnail version of the image |
| `video` | `string` \| `null` | Related news video (null if unavailable) |
| `title` | `string` | News content text |
| `cover_image` | `string` \| `null` | News cover image (null if unavailable) |

---

## 🧪 Sample Request

`GET` https://sports.api-sina-free.workers.dev/sports

---

## 🧾 Sample Response

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "data": [
    {
      "id": "b0ac5451-b27c-48ea-aa4a-cfa0336c1a5d",
      "title": "Match Report: Tractor vs Chadormalu; League Leaders Under the Champion’s Shadow!",
      "sub_title": null,
      "media": {
        "photo": "https://static.football360.ir/nesta2/media/posts_media/خلاصه_بازی_KOObpth_u9F64bn.jpg",
        "thumbnail": "https://static.football360.ir/nesta2/media/posts_media/thumbnails/کاور_گزارش_اختصاصی_تراکتور_چادرمولو__thumb.jpg",
        "video": "https://s3.ir-thr-at1.arvanstorage.ir/site-videos/Sadegh/تراکتور%20چادر.mp4",
        "title": "Match report: Tractor vs Chadormalu",
        "cover_image": "https://static.football360.ir/nesta2/media/posts_media/covers/کاور_گزارش_اختصاصی_تراکتور_چادرمولو_.jpg"
      }
    }
  ]
}
```

---

# 💻 Python Usage Example

```py
import requests

res = requests.get("https://sports.api-sina-free.workers.dev/sports")
data = res.json()

for item in data["data"]:
    print("⚽", item["title"])
    print("🆔", item["id"])
    if item["media"]["video"]:
        print("🎥 Video:", item["media"]["video"])
    print("-" * 40)
```

---

# 🤖 Usage in Bots / Rubika

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_sports_news_bot")

API_URL = "https://sports.api-sina-free.workers.dev/sports"

def get_sports_news():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "اخبار ورزشی":
        data = get_sports_news()
        if not data:
            return await message.reply("❌ خطا در دریافت اخبار ورزشی")

        news_list = data.get("data", [])
        if not news_list:
            return await message.reply("📭 خبری یافت نشد.")

        result = "⚽ *آخرین اخبار ورزشی:*\n\n"
        for item in news_list:
            result += f"🔸 {item['title']}\n"
            if item.get("sub_title"):
                result += f"▫️ {item['sub_title']}\n"
            if item["media"].get("video"):
                result += f"🎥 ویدیو: {item['media']['video']}\n"
            result += "\n"

        await message.reply(result[:4000], parse_mode="markdown")

bot.run()
```

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers
🗳 Rubika: https://rubika.ir/Sinabani_api
🔗 Endpoint: https://sports.api-sina-free.workers.dev/sports
