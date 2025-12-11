# 👑 SinaGoldAPI version : 2.1.2

وب‌سرویس **SinaGoldAPI** یک سرویس سریع و سبک برای دریافت قیمت‌ لحظه‌ای **طلا و سکه** از معتبرترین منبع اعلام نرخ‌هاست 🇮🇷💰  
فقط با یک درخواست GET می‌تونی نرخ‌های لحظه‌ای رو بگیری — **بدون نیاز به API Key** 🚀


---

## 🌐 آدرس وب‌سرویس

https://gold.api-sina-free.workers.dev/gold

---

## 🔹 خروجی‌ها

| پارامتر | نوع | توضیح |
|--------|------|--------|
| gold_18_ayar | number | قیمت هر گرم طلای ۱۸ عیار |
| gold_24_ayar | number | قیمت هر گرم طلای ۲۴ عیار |
| gold_second_hand | number | قیمت طلای دست دوم |
| mesghal_tala | number | قیمت هر مثقال طلا |
| abshode_naghd | number | قیمت آبشده نقدی |
| abshode_moamelati | number | قیمت آبشده معاملاتی |
| sekke_emami | number | سکه امامی |
| sekke_bahar_azadi | number | سکه بهار آزادی |
| nim_sekke | number | نیم‌سکه |
| rob_sekke | number | ربع‌سکه |
| sekke_gerami | number | سکه گرمی |
| habab_* | number | حباب سکه‌ها |
| updated_at | string | زمان به‌روزرسانی |
| source | string | منبع دریافت قیمت |

---

## 🧪 نمونه درخواست

GET https://gold.api-sina-free.workers.dev/gold

---

## 🧾 نمونه خروجی

```json
{
  "gold_18_ayar": 104989000,
  "gold_24_ayar": 139983000,
  "gold_second_hand": 103588700,
  "mesghal_tala": 454890000,
  "abshode_naghd": 454740000,
  "abshode_moamelati": 454750000,
  "sekke_emami": 1114050000,
  "sekke_bahar_azadi": 1044300000,
  "nim_sekke": 582000000,
  "rob_sekke": 336000000,
  "sekke_gerami": 164000000,
  "habab_emami": 96460000,
  "habab_bahar": 27160000,
  "habab_nim": 73470000,
  "habab_rob": 81710000,
  "habab_gerami": 38910000,
  "updated_at": "2025-11-06T12:19:14.378Z",
  "source": "tgju.org"
}
```

---

## 💻 نمونه استفاده در Python

```python
import requests

res = requests.get("https://gold.api-sina-free.workers.dev/gold")
data = res.json()

print("💰 طلای 18 عیار:", data["gold_18_ayar"])
print("🥇 سکه امامی:", data["sekke_emami"])
print("⏱ آخرین بروزرسانی:", data["updated_at"])
```

---

## 🤖 استفاده در ربات روبیکا / بات‌ها

```python
from rubpy import Client, filters
import requests

bot = Client(name="sina_gold_pro")

API_URL = "https://gold.api-sina-free.workers.dev/gold"

def get_gold_data():
    try:
        res = requests.get(API_URL, timeout=5)
        return res.json()
    except:
        return None

def format_number(n):
    return f"{n:,}"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text in ["/help", "منو"]:
        return await message.reply(
            "💰 `قیمت طلا` → نمایش نرخ‌های اصلی\n"
            "📦 `جزئیات` → نمایش تمام نرخ‌ها + حباب‌ها\n"
            "🔄 `آپدیت` → بررسی آخرین زمان بروز رسانی\n"
            "ℹ️ `منبع` → نمایش منبع نرخ‌ها\n"
            , parse_mode="markdown"
        )

    elif text == "قیمت طلا":
        data = get_gold_data()
        if not data:
            return await message.reply("❗ خطا در دریافت اطلاعات.")
        
        await message.reply(
            f"💰 *قیمت لحظه‌ای طلا و سکه:*\n\n"
            f"🥇 طلای ۱۸ عیار: {format_number(data['gold_18_ayar'])} ریال\n"
            f"🏅 سکه امامی: {format_number(data['sekke_emami'])} ریال\n"
            f"🌓 نیم سکه: {format_number(data['nim_sekke'])} ریال\n"
            f"🌗 ربع سکه: {format_number(data['rob_sekke'])} ریال\n"
            f"\n⏱ بروزرسانی: {data['updated_at']}"
            , parse_mode="markdown"
        )

    elif text == "جزئیات":
        data = get_gold_data()
        if not data:
            return await message.reply("❗ خطا در دریافت اطلاعات.")

        await message.reply(
            f"📦 *جزئیات کامل قیمت‌ها:*\n\n"
            f"🥇 طلای ۱۸ عیار: {format_number(data['gold_18_ayar'])} ریال\n"
            f"🥇 طلای ۲۴ عیار: {format_number(data['gold_24_ayar'])} ریال\n"
            f"🟡 طلای دست دوم: {format_number(data['gold_second_hand'])} ریال\n"
            f"⚖️ مثقال طلا: {format_number(data['mesghal_tala'])} ریال\n"
            f"🔥 آبشده نقدی: {format_number(data['abshode_naghd'])} ریال\n"
            f"💹 آبشده معاملاتی: {format_number(data['abshode_moamelati'])} ریال\n\n"

            f"🏅 *قیمت انواع سکه:*\n"
            f"سکه امامی: {format_number(data['sekke_emami'])} ریال\n"
            f"سکه بهار آزادی: {format_number(data['sekke_bahar_azadi'])} ریال\n"
            f"نیم سکه: {format_number(data['nim_sekke'])} ریال\n"
            f"ربع سکه: {format_number(data['rob_sekke'])} ریال\n"
            f"سکه گرمی: {format_number(data['sekke_gerami'])} ریال\n\n"

            f"🎯 *حباب سکه‌ها:*\n"
            f"حباب امامی: {format_number(data['habab_emami'])} ریال\n"
            f"حباب بهار آزادی: {format_number(data['habab_bahar'])} ریال\n"
            f"حباب نیم سکه: {format_number(data['habab_nim'])} ریال\n"
            f"حباب ربع سکه: {format_number(data['habab_rob'])} ریال\n"
            f"حباب سکه گرمی: {format_number(data['habab_gerami'])} ریال\n\n"

            f"⏱ بروزرسانی: {data['updated_at']}\n"
            f"🔗 منبع: {data['source']}"
            , parse_mode="markdown"
        )

    elif text == "آپدیت":
        data = get_gold_data()
        if not data:
            return await message.reply("⛔ خطا در اتصال به سرور.")
        await message.reply(f"🔄 آخرین بروزرسانی: {data['updated_at']}")

    elif text == "منبع":
        data = get_gold_data()
        if not data:
            return await message.reply("⛔ اتصال برقرار نشد.")
        await message.reply(f"📌 منبع نرخ‌ها: {data['source']}")

bot.run()
```

---

## 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers          
🗳 Rubika: https://rubika.ir/Sinabani_api          
🔗 Endpoint: https://gold.api-sina-free.workers.dev/gold          

---

---

# 👑 SinaGoldAPI version : 2.1.2

The **SinaGoldAPI** web service is a fast and lightweight API for retrieving the real-time prices of **gold and coins** from one of the most reliable Iranian pricing sources 🇮🇷💰  
With just a simple GET request, you can instantly fetch all updated prices — **no API key required** 🚀

---

## 🌐 API Endpoint

https://gold.api-sina-free.workers.dev/gold

---

## 🔹 Output Fields

| Parameter | Type | Description |
|----------|------|-------------|
| gold_18_ayar | number | Price of 18K gold per gram |
| gold_24_ayar | number | Price of 24K gold per gram |
| gold_second_hand | number | Price of second-hand gold |
| mesghal_tala | number | Price of one Mesghal of gold |
| abshode_naghd | number | Cash molten gold price |
| abshode_moamelati | number | Trading molten gold price |
| sekke_emami | number | Emami coin price |
| sekke_bahar_azadi | number | Bahar Azadi coin price |
| nim_sekke | number | Half coin |
| rob_sekke | number | Quarter coin |
| sekke_gerami | number | One-gram coin |
| habab_* | number | Bubble prices of coins |
| updated_at | string | Last update timestamp |
| source | string | Data provider |

---

## 🧪 Sample Request

GET https://gold.api-sina-free.workers.dev/gold

---

## 🧾 Sample Response

```json
{
  "gold_18_ayar": 104989000,
  "gold_24_ayar": 139983000,
  "gold_second_hand": 103588700,
  "mesghal_tala": 454890000,
  "abshode_naghd": 454740000,
  "abshode_moamelati": 454750000,
  "sekke_emami": 1114050000,
  "sekke_bahar_azadi": 1044300000,
  "nim_sekke": 582000000,
  "rob_sekke": 336000000,
  "sekke_gerami": 164000000,
  "habab_emami": 96460000,
  "habab_bahar": 27160000,
  "habab_nim": 73470000,
  "habab_rob": 81710000,
  "habab_gerami": 38910000,
  "updated_at": "2025-11-06T12:19:14.378Z",
  "source": "tgju.org"
}
```

---

# 💻 Python Usage Example

```py
import requests

res = requests.get("https://gold.api-sina-free.workers.dev/gold")
data = res.json()

print("💰 18K Gold:", data["gold_18_ayar"])
print("🥇 Emami Coin:", data["sekke_emami"])
print("⏱ Last Update:", data["updated_at"])
```

---

# 🤖 Usage in Rubika Bot / Chat Bots

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_gold_pro")

API_URL = "https://gold.api-sina-free.workers.dev/gold"

def get_gold_data():
    try:
        res = requests.get(API_URL, timeout=5)
        return res.json()
    except:
        return None

def format_number(n):
    return f"{n:,}"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text in ["/help", "menu"]:
        return await message.reply(
            "💰 `gold price` → Show main prices\n"
            "📦 `details` → Show all prices + bubble values\n"
            "🔄 `update` → Check the last update timestamp\n"
            "ℹ️ `source` → Show the price source\n"
            , parse_mode="markdown"
        )

    elif text == "gold price":
        data = get_gold_data()
        if not data:
            return await message.reply("❗ Error fetching data.")
        
        await message.reply(
            f"💰 *Real-time Gold & Coin Prices:*\n\n"
            f"🥇 18K Gold: {format_number(data['gold_18_ayar'])} IRR\n"
            f"🏅 Emami Coin: {format_number(data['sekke_emami'])} IRR\n"
            f"🌓 Half Coin: {format_number(data['nim_sekke'])} IRR\n"
            f"🌗 Quarter Coin: {format_number(data['rob_sekke'])} IRR\n"
            f"\n⏱ Last Update: {data['updated_at']}"
            , parse_mode="markdown"
        )

    elif text == "details":
        data = get_gold_data()
        if not data:
            return await message.reply("❗ Error fetching data.")

        await message.reply(
            f"📦 *Full Price Details:*\n\n"
            f"🥇 18K Gold: {format_number(data['gold_18_ayar'])} IRR\n"
            f"🥇 24K Gold: {format_number(data['gold_24_ayar'])} IRR\n"
            f"🟡 Second-hand Gold: {format_number(data['gold_second_hand'])} IRR\n"
            f"⚖️ Mesghal Gold: {format_number(data['mesghal_tala'])} IRR\n"
            f"🔥 Cash Molten: {format_number(data['abshode_naghd'])} IRR\n"
            f"💹 Trading Molten: {format_number(data['abshode_moamelati'])} IRR\n\n"

            f"🏅 *Coin Prices:*\n"
            f"Emami Coin: {format_number(data['sekke_emami'])} IRR\n"
            f"Bahar Azadi Coin: {format_number(data['sekke_bahar_azadi'])} IRR\n"
            f"Half Coin: {format_number(data['nim_sekke'])} IRR\n"
            f"Quarter Coin: {format_number(data['rob_sekke'])} IRR\n"
            f"One-gram Coin: {format_number(data['sekke_gerami'])} IRR\n\n"

            f"🎯 *Coin Bubbles:*\n"
            f"Emami Bubble: {format_number(data['habab_emami'])} IRR\n"
            f"Bahar Bubble: {format_number(data['habab_bahar'])} IRR\n"
            f"Half Bubble: {format_number(data['habab_nim'])} IRR\n"
            f"Quarter Bubble: {format_number(data['habab_rob'])} IRR\n"
            f"One-gram Bubble: {format_number(data['habab_gerami'])} IRR\n\n"

            f"⏱ Last Update: {data['updated_at']}\n"
            f"🔗 Source: {data['source']}"
            , parse_mode="markdown"
        )

    elif text == "update":
        data = get_gold_data()
        if not data:
            return await message.reply("⛔ Server connection error.")
        await message.reply(f"🔄 Last Update: {data['updated_at']}")

    elif text == "source":
        data = get_gold_data()
        if not data:
            return await message.reply("⛔ Unable to connect.")
        await message.reply(f"📌 Price Source: {data['source']}")

bot.run()
```

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                  
🗳 Rubika: https://rubika.ir/Sinabani_api                 
🔗 Endpoint: https://gold.api-sina-free.workers.dev/gold          
