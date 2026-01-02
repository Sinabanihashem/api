# 📰 SinaNewsAPI version : 1.0.0

وب‌سرویس **SinaNewsAPI** یک API سبک و سریع برای دریافت **جدیدترین اخبار روز ایران و جهان** از منابع خبری معتبر است 🗞️⚡  
فقط با یک درخواست GET می‌تونی آخرین تیترهای خبری رو دریافت کنی — **بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://news.api-sina-free.workers.dev/news

---

## 📦 خروجی وب‌سرویس

| کلید | نوع | توضیح |
|-----|-----|--------|
| channel | string | شناسه کانال منتشرکننده |
| creator | string | نام توسعه‌دهنده |
| count | number | تعداد اخبار ارسال‌شده |
| news | array | لیست اخبار |
| news[].title | string | عنوان خبر |
| news[].link | string | لینک منبع خبر |

---

## 🧪 نمونه درخواست

GET https://news.api-sina-free.workers.dev/news

---

## 🧾 نمونه خروجی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "count": 5,
  "news": [
    {
      "title": "شوک بزرگ چین به ایران/ پکن محموله ایرانی را مصادره کرد",
      "link": "https://www.shahrekhabar.com/news/175982640069522"
    },
    {
      "title": "احتمال مداخله نظامی ترکیه در سوریه به نفع رژیم جولانی",
      "link": "https://www.shahrekhabar.com/news/175982598044448"
    }
  ]
}
```

---

# 💻 نمونه استفاده در Python

```py
import requests

res = requests.get("https://news.api-sina-free.workers.dev/news")
data = res.json()

print("📰 تعداد اخبار:", data["count"])

for item in data["news"]:
    print("🔸", item["title"])
    print("🔗", item["link"])
    print("-" * 30)
```

---

# 🤖 استفاده در ربات روبیکا / بات‌ها

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_news_bot")

API_URL = "https://news.api-sina-free.workers.dev/news"

def get_news():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "اخبار":
        data = get_news()
        if not data:
            return await message.reply("❌ خطا در دریافت اخبار")

        news_list = data.get("news", [])
        if not news_list:
            return await message.reply("📭 خبری یافت نشد.")

        result = "📰 *آخرین اخبار روز:*\n\n"
        for item in news_list:
            result += f"🔸 {item['title']}\n🔗 {item['link']}\n\n"

        await message.reply(result[:4000], parse_mode="markdown")

bot.run()
```

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                   
🗳 Rubika: https://rubika.ir/Sinabani_api                      
🔗 Endpoint: https://news.api-sina-free.workers.dev/news

---

---


# 📰 SinaNewsAPI version : 1.0.0

**SinaNewsAPI** is a lightweight and fast web service that provides the **latest daily news headlines** from reliable Iranian and international news sources 🗞️⚡  
With just a single GET request, you can fetch the newest news instantly — **no API key required** 🚀

---

## 🌐 API Endpoint

https://news.api-sina-free.workers.dev/news

---

## 📦 API Response Structure

| Key | Type | Description |
|-----|------|-------------|
| channel | string | Publisher channel identifier |
| creator | string | Developer username |
| count | number | Number of returned news items |
| news | array | List of news |
| news[].title | string | News title |
| news[].link | string | Original news source link |

---

## 🧪 Sample Request

GET https://news.api-sina-free.workers.dev/news

---

## 🧾 Sample Response

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "count": 5,
  "news": [
    {
      "title": "Major shock from China to Iran / Beijing seized Iranian shipment",
      "link": "https://www.shahrekhabar.com/news/175982640069522"
    },
    {
      "title": "Possibility of Turkish military intervention in Syria in favor of Jolani regime",
      "link": "https://www.shahrekhabar.com/news/175982598044448"
    }
  ]
}
```

---

# 💻 Python Usage Example

```py
import requests

res = requests.get("https://news.api-sina-free.workers.dev/news")
data = res.json()

print("📰 Total News:", data["count"])

for item in data["news"]:
    print("🔸", item["title"])
    print("🔗", item["link"])
    print("-" * 30)
```

---

# 🤖 Rubika Bot / Chatbot Example

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_news_bot")

API_URL = "https://news.api-sina-free.workers.dev/news"

def get_news():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.lower() == "news":
        data = get_news()
        if not data:
            return await message.reply("❌ Failed to fetch news.")

        news_list = data.get("news", [])
        if not news_list:
            return await message.reply("📭 No news found.")

        result = "📰 *Latest News Headlines:*\n\n"
        for item in news_list:
            result += f"🔸 {item['title']}\n🔗 {item['link']}\n\n"

        await message.reply(result[:4000], parse_mode="markdown")

bot.run()
```

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers              
🗳 Rubika: https://rubika.ir/Sinabani_api                 
🔗 Endpoint: https://news.api-sina-free.workers.dev/news
