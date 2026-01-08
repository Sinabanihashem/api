# 🎮 Minecraft News API
### نسخه: Minecraft API v1.0.0

وب‌سرویس **Minecraft News API** یک API سریع، سبک و بدون نیاز به API Key برای  
📰 **دریافت آخرین اخبار بازی ماینکرفت** است.

این سرویس جدیدترین اخبار مرتبط با ماینکرفت را از مجله‌ی کافه‌بازار جمع‌آوری کرده و  
خروجی استاندارد و ساخت‌یافته **JSON** ارائه می‌دهد.

🔹 اجرا شده روی **Leapcell.io**  
🔹 مناسب ربات‌ها، وب‌سایت‌ها و اپلیکیشن‌های موبایل  
🔹 ارائه عنوان خبر، خلاصه، تصویر، تاریخ و لینک خبر  

---

## 🧠 نحوه کار API (Architecture)

1️⃣ کلاینت درخواست دریافت اخبار را ارسال می‌کند  
2️⃣ سرویس اطلاعات اخبار ماینکرفت را از منبع خبری دریافت می‌کند  
3️⃣ داده‌ها پردازش، استانداردسازی و پاک‌سازی می‌شوند  
4️⃣ خروجی نهایی به صورت JSON بازگردانده می‌شود  

---

## 🌐 آدرس اصلی وب‌سرویس

https://minecraft-api-sina-free.leapcell.app

---

## 🔗 Endpoints

### 🔹 دریافت آخرین اخبار ماینکرفت

```http
GET /minecraft-news?page=1
```
> پارامتر page اختیاری است (پیش‌فرض ۱).

---

### 🔹 پارس کردن HTML خام

```http
POST /minecraft-news/parse
Content-Type: text/plain
```

> در Body باید متن HTML خام دسته‌بندی اخبار ماینکرفت ارسال شود.

---

# 📦 ساختار خروجی API

```json
{
  "channel": "@Sinabani_api",
  "writer": "@Sinabanis",
  "page": 1,
  "count": 8,
  "items": [
    {
      "image_url": "https://mag.cafebazaar.ir/wp-content/uploads/2026/01/Screenshot-1404-10-18-at-10.24.57.jpg.webp",
      "title": "عنوان خبر",
      "summary": "خلاصه یا توضیح کوتاه خبر",
      "date": "۱۴۰۴/۱۰/۱۸",
      "link": "https://mag.cafebazaar.ir/new-minecraft-snapshot-adds-updated-models-for-baby-mobs/",
      "topic": "آخرین اخبار ماینکرافت"
    }
  ]
}
```

---

## 🧾 توضیح فیلدهای خروجی

| فیلد       | نوع      | توضیح |
|------------|----------|-------|
| `channel`  | `string` | نام کانال یا منبع انتشار API |
| `writer`   | `string` | نام توسعه‌دهنده API |
| `page`     | `integer`| شماره صفحه دریافت‌شده |
| `count`    | `integer`| تعداد اخبار استخراج‌شده |
| `items`    | `array`  | لیست اخبار ماینکرفت |
| `image_url`| `string` | لینک تصویر خبر |
| `title`    | `string` | عنوان خبر |
| `summary`  | `string` | خلاصه خبر |
| `date`     | `string` | تاریخ انتشار خبر |
| `link`     | `string` | لینک مستقیم خبر |
| `topic`    | `string` | موضوع یا دسته‌بندی خبر |

---

# 🧪 نمونه درخواست

```http
GET https://minecraft-api-sina-free.leapcell.app/minecraft-news?page=1
```

---

# 🧾 نمونه خروجی

```json
{
  "channel": "@Sinabani_api",
  "writer": "@Sinabanis",
  "page": 1,
  "count": 1,
  "items": [
    {
      "image_url": "https://mag.cafebazaar.ir/wp-content/uploads/2026/01/Screenshot-1404-10-18-at-10.24.57.jpg.webp",
      "title": "به‌روزرسانی جدید ماینکرفت برای مدل‌های بچه‌ماب‌ها",
      "summary": "ماینکرفت با اسنپ‌شات جدید مدل‌های بچه‌ماب‌ها را تغییر داده است...",
      "date": "۱۴۰۴/۱۰/۱۸",
      "link": "https://mag.cafebazaar.ir/new-minecraft-snapshot-adds-updated-models-for-baby-mobs/",
      "topic": "آخرین اخبار ماینکرافت"
    }
  ]
}
```

---

# ⚠️ مدیریت خطاها

| وضعیت | پیام |
|-------|------|
| 448   | خطا در دریافت اخبار ماینکرفت از منبع |
| 500   | خطای داخلی سرور |

### 🧾 نمونه خطا

```json
{
  "ok": false,
  "channel": "@Sinabani_api",
  "writer": "@Sinabanis",
  "data": "خطا در دریافت اخبار ماینکرفت."
}
```

---

# 💻 استفاده کامل در Python

```py
import requests

API = "https://minecraft-news-sinabanihashem4650-mn3t8pgp.leapcell.dev/minecraft-news"

def getminecraftnews(page=1):
    try:
        res = requests.get(API, params={"page": page}, timeout=10)
        return res.json()
    except Exception as e:
        return {
            "ok": False,
            "error": str(e)
        }

newsdata = getminecraft_news()

for news in news_data.get("items", []):
    print(news["title"], news["link"])
```

---

# 💻 استفاده کامل در Node.js

```js
const API = "https://minecraft-news-sinabanihashem4650-mn3t8pgp.leapcell.dev/minecraft-news";

async function getMinecraftNews() {
  try {
    const res = await fetch(API + "?page=1");
    const data = await res.json();
    console.log(data.items);
  } catch (err) {
    console.error("Error fetching news:", err);
  }
}

getMinecraftNews();
```

---

# 🤖 استفاده در ربات (Rubika , py)

```py
import requests
from rubpy import Client, filters

API = "https://minecraft-news-sinabanihashem4650-mn3t8pgp.leapcell.dev/minecraft-news"

bot = Client(name="minecraftnewsbot")

@bot.onmessageupdates(filters.text)
async def handler(message):
    text = message.text.strip().lower()

    if text not in ["اخبار ماینکرفت", "/minecraft", "minecraft"]:
        return

    try:
        res = requests.get(API, timeout=10)
        data = res.json()
    except Exception as e:
        return await message.reply(f"❌ خطا در ارتباط با سرور:\n{e}")

    news_list = data.get("items", [])
    if not news_list:
        return await message.reply("❌ خبری دریافت نشد.")

    news = news_list[0]

    title = news.get("title", "-")
    summary = news.get("summary", "-")
    image = news.get("image_url", "")

    reply_text = (
        f"🎮 {title}\n\n"
        f"📰 {summary}"
    )

    if image:
        await message.reply_photo(
            photo=image,
            caption=reply_text,
            parse_mode="markdown"
        )
    else:
        await message.reply(
            reply_text,
            parse_mode="markdown"
        )

bot.run()
```

---

# ⚙️ ویژگی‌ها

✅ بدون نیاز به API Key  
✅ دریافت سریع و سبک اخبار ماینکرفت  
✅ خروجی JSON استاندارد  
✅ مناسب استفاده در Production  
✅ RESTful و پایدار  
✅ اجرا شده روی Leapcell.io  

---

# 🎯 موارد استفاده

● ربات‌های خبری ماینکرفت  
● وب‌سایت‌های گیمینگ  
● اپلیکیشن‌های موبایل  
● داشبوردهای خبری  
● پروژه‌های دانشجویی و حرفه‌ای  

---

# 👤 Developer

### Mir Sina Banihashem

📍 Hosted on: Leapcell.io  
🗳 Rubika: https://rubika.ir/Sinabaniapi  
🔗 API Endpoint: https://minecraft-api-sina-free.leapcell.app

---

---
