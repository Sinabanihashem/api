# 💰 Currency Price API
### Version : Excoino Proxy v1.0.0

وب‌سرویس **Crypto Currency Price API** یک API سریع، سبک و بدون نیاز به API Key برای  
📊 **دریافت قیمت لحظه‌ای ارزهای دیجیتال** است.

این سرویس با دریافت **نام یا نماد ارز دیجیتال**، اطلاعات کامل آن ارز را از منبع معتبر **Excoino** دریافت کرده  
و پس از پردازش، خروجی استاندارد JSON برمی‌گرداند.

🔹 اجرا شده روی **Cloudflare Workers**                  
🔹 مناسب ربات‌ها، وب‌سایت‌ها و اپلیکیشن‌ها                  
🔹 پشتیبانی از لوگوی ارزها با Proxy اختصاصی                       

---

## 🧠 نحوه کار API (Architecture)

1️⃣ کاربر نام یا نماد ارز را ارسال می‌کند                   
2️⃣ Worker اطلاعات را از Excoino دریافت می‌کند                      
3️⃣ ارز موردنظر فیلتر می‌شود                         
4️⃣ لینک لوگو از طریق Cloudflare Proxy می‌شود                    
5️⃣ خروجی JSON استاندارد برگردانده می‌شود                          

---

## 🌐 آدرس اصلی وب‌سرویس

https://currency.api-sina-free.workers.dev/

---

## 🔗 Endpoint ها

### 🔹 1. دریافت اطلاعات ارز دیجیتال

GET /

#### پارامترهای Query

| پارامتر | نوع | الزامی | توضیح |
|------|----|------|------|
| `crypto` | `string` | ✅ | نام یا نماد ارز (btc / bitcoin / eth / ...) |

---

### 🔹 2. دریافت لوگوی ارز (Proxy)

GET /logo/{SYMBOL}

**📌 مثال:**

/logo/BTC

---

## 📦 ساختار خروجی API

```json
{
  "channel": "string",
  "creator": "string",
  "list": [
    {
      "id": "number",
      "rank": "number",
      "name": "string",
      "iso": "string",
      "logo": "string",
      "price": "number",
      "price_rial": "number",
      "price_buy": "number",
      "price_sell": "number",
      "market_cap": "string",
      "daily_change_percent": "number"
    }
  ],
  "activ": 1,
  "time": "string"
}
```

---

# 🧪 نمونه درخواست ساده

```http
GET https://currency.api-sina-free.workers.dev/?crypto=btc
```

---

# 🧾 نمونه خروجی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "list": [
    {
      "id": 2,
      "rank": 1,
      "name": "Bitcoin",
      "iso": "BTC",
      "logo": "https://currency.api-sina-free.workers.dev/logo/BTC",
      "price": 87093.17,
      "price_rial": 114051920140,
      "price_buy": 115201637077,
      "price_sell": 114051920140,
      "market_cap": "2,246,477,303,803",
      "daily_change_percent": 0.71
    }
  ],
  "activ": 1,
  "time": "۱۴۰۴/۹/۲۸, ۱۸:۱۰:۱۱"
}
```

---

## ⚠️ مدیریت خطاها

| وضعیت | پیام |
|------|------|
| `400` | پارامتر `crypto` ارسال نشده |
| `404` | ارز موردنظر پیدا نشد |
| `500` | خطا در ارتباط با منبع |

### 🧾 نمونه خطا

```json
{
  "error": "ارز مورد نظر پیدا نشد"
```

---

# 💻 استفاده کامل (صفر تا صد) در Python

```py
import requests

API = "https://currency.api-sina-free.workers.dev/"

def full_crypto_info(symbol):
    res = requests.get(API, params={"crypto": symbol}, timeout=10)
    data = res.json()

    if data.get("activ") != 1:
        print("Service inactive")
        return

    coin = data["list"][0]

    print("Name:", coin["name"])
    print("Symbol:", coin["iso"])
    print("Rank:", coin["rank"])
    print("USD Price:", coin["price"])
    print("IRR Price:", coin["price_rial"])
    print("Buy:", coin["price_buy"])
    print("Sell:", coin["price_sell"])
    print("Market Cap:", coin["market_cap"])
    print("Daily Change:", coin["daily_change_percent"])
    print("BTC Value:", coin["price_bitcoin"])
    print("Logo URL:", coin["logo"])
    print("Update Time:", data["time"])

full_crypto_info("btc")
```

---

# 💻 نمونه استفاده کامل در Node.js (Backend / Frontend)

```javascript
const API = "https://currency.api-sina-free.workers.dev/";

async function loadCrypto(symbol) {
  const res = await fetch(`${API}?crypto=${symbol}`);
  const data = await res.json();

  if (data.activ !== 1) {
    alert("Service inactive");
    return;
  }

  const c = data.list[0];

  document.body.innerHTML = `
    <h2>${c.name} (${c.iso})</h2>
    <img src="${c.logo}" width="80">
    <p>USD: ${c.price}</p>
    <p>IRR: ${c.price_rial.toLocaleString()}</p>
    <p>Market Cap: ${c.market_cap}</p>
    <p>Change: ${c.daily_change_percent}%</p>
    <small>Updated: ${data.time}</small>
  `;
}

loadCrypto("btc");
```

---

# 🤖 استفاده صفر تا صد در ربات Rubika

```py
from rubpy import Client, filters
import requests

bot = Client(name="crypto_price_bot")
API = "https://currency.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip().lower()

    if not text.startswith("قیمت"):
        return

    symbol = text.replace("قیمت", "", 1).strip()
    if not symbol:
        return await message.reply("❗️ مثال صحیح:\nقیمت btc")

    try:
        res = requests.get(API, params={"crypto": symbol}, timeout=10)

        if res.status_code != 200:
            return await message.reply("❌ خطا در ارتباط با سرور")

        data = res.json()

        # بررسی فعال بودن سرویس
        if data.get("activ") != 1:
            return await message.reply("⚠️ سرویس موقتاً غیرفعال است")

        if not data.get("list"):
            return await message.reply("❌ ارز موردنظر پیدا نشد")

        coin = data["list"][0]

        # استفاده از تمام فیلدهای مهم خروجی
        text_reply = (
            f"🪙 *{coin['name']} ({coin['iso']})*\n\n"
            f"🏆 رتبه بازار: {coin['rank']}\n"
            f"💲 قیمت دلاری: `{coin['price_string_format']}$`\n"
            f"💰 قیمت ریالی: `{coin['price_rial']:,}` ریال\n"
            f"🟢 قیمت خرید: `{coin['price_buy']:,}`\n"
            f"🔴 قیمت فروش: `{coin['price_sell']:,}`\n"
            f"📊 ارزش بازار: `{coin['market_cap']}`\n"
            f"📉 تغییر ۲۴ساعت: `{coin['daily_change_percent']}%`\n"
            f"🪙 معادل بیت‌کوین: `{coin['price_bitcoin']}`\n\n"
            f"🕒 زمان بروزرسانی:\n`{data['time']}`\n\n"
            f"🖼 [مشاهده لوگو]({coin['logo']})\n\n"
            f"📡 {data['channel']}\n"
            f"👤 {data['creator']}"
        )

        await message.reply(text_reply, parse_mode="markdown")

    except Exception as e:
        await message.reply(f"❌ خطای غیرمنتظره:\n{e}")

bot.run()
```

---

# ⚙️ ویژگی‌ها

✅ بدون API Key                
✅ دریافت قیمت لحظه‌ای               
✅ پشتیبانی از نماد و نام ارز                  
✅ لوگوی Proxy‌شده                     
✅ سریع و پایدار                     
✅ مناسب Production                         
✅ RESTful کامل                       
✅ Cloudflare Workers


---

# 🎯 موارد استفاده

● ربات‌های قیمت ارز دیجیتال               
● سایت‌های کریپتویی                  
● داشبوردهای مالی                    
● اپلیکیشن‌های ترید                 
● ابزارهای مانیتورینگ بازار              
● پروژه‌های دانشجویی و حرفه‌ای                  


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                 
🗳 Rubika: https://rubika.ir/Sinabani_api                  
🔗 API Endpoint: https://currency.api-sina-free.workers.dev/                 

---

---

# 💰 Crypto Currency Price API
### Version: Excoino Proxy v1.0.0

**Crypto Currency Price API** is a fast, lightweight, and API-key-free service for  
📊 **retrieving real-time cryptocurrency prices**.

This API receives a **cryptocurrency name or symbol**, fetches its data from the trusted **Excoino** source,  
processes it, and returns a clean, standardized **JSON response**.

🔹 Hosted on **Cloudflare Workers**                      
🔹 Suitable for bots, websites, and applications                   
🔹 Includes a built-in **logo proxy** for cryptocurrencies              

---

## 🧠 How the API Works (Architecture)

1️⃣ The user sends a crypto name or symbol               
2️⃣ The Worker fetches data from Excoino              
3️⃣ The requested currency is filtered         
4️⃣ The logo URL is proxied via Cloudflare              
5️⃣ A standardized JSON response is returned             

---

## 🌐 Base URL

https://currency.api-sina-free.workers.dev/

---

## 🔗 Available Endpoints

### 🔹 1. Get Cryptocurrency Information

GET /

#### Query Parameters

| Parameter | Type | Required | Description |
|--------|------|----------|------------|
| `crypto` | `string` | ✅ Yes | Cryptocurrency name or symbol (btc / bitcoin / eth / ...) |

---

### 🔹 2. Get Cryptocurrency Logo (Proxy)

GET /logo/{SYMBOL}

**📌 Example:**

/logo/BTC

---

## 📦 API Response Structure

```json
{
  "channel": "string",
  "creator": "string",
  "list": [
    {
      "id": "number",
      "rank": "number",
      "name": "string",
      "name_locale": "string",
      "iso": "string",
      "logo": "string",
      "price": "number",
      "price_string_format": "string",
      "price_bitcoin": "string",
      "price_rial": "number",
      "price_buy": "number",
      "price_sell": "number",
      "market_cap": "string",
      "daily_change_percent": "number",
      "meta_data": "null | object",
      "admin_order": "number"
    }
  ],
  "activ": 1,
  "time": "string"
}
```

---

# 🧪 Example Request

```http
GET https://currency.api-sina-free.workers.dev/?crypto=btc
```

---

# 🧾 Example Response

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "list": [
    {
      "id": 2,
      "rank": 1,
      "name": "Bitcoin",
      "name_locale": "Bitcoin",
      "iso": "BTC",
      "logo": "https://currency.api-sina-free.workers.dev/logo/BTC",
      "price": 87093.17,
      "price_string_format": "87093.17",
      "price_bitcoin": "1.00000000",
      "price_rial": 114051920140,
      "price_buy": 115201637077,
      "price_sell": 114051920140,
      "market_cap": "2,246,477,303,803",
      "daily_change_percent": 0.71,
      "meta_data": null,
      "admin_order": 1
    }
  ],
  "activ": 1,
  "time": "1404/09/28, 18:10:11"
}
```

---

---

## ⚠️ Error Handling

| Status | Message |
|-------|---------|
| `400` | `crypto` parameter is missing |
| `404` | Cryptocurrency not found |
| `500` | Error communicating |

### 🧾 Error Example

```json
{
  "error": "Cryptocurrency not found"
}
```

---

# 💻 Full Usage Example (Python – End-to-End)

```py
import requests

BASE_URL = "https://currency.api-sina-free.workers.dev/"

def get_full_crypto_info(symbol):
    res = requests.get(
        BASE_URL,
        params={"crypto": symbol},
        timeout=10
    )

    if res.status_code != 200:
        print("Server Error")
        return

    data = res.json()

    if data.get("activ") != 1:
        print("Service is inactive")
        return

    coin = data["list"][0]

    print("Name:", coin["name"])
    print("Symbol:", coin["iso"])
    print("Rank:", coin["rank"])
    print("USD Price:", coin["price"])
    print("IRR Price:", coin["price_rial"])
    print("Buy Price:", coin["price_buy"])
    print("Sell Price:", coin["price_sell"])
    print("Market Cap:", coin["market_cap"])
    print("Daily Change:", coin["daily_change_percent"])
    print("BTC Equivalent:", coin["price_bitcoin"])
    print("Logo URL:", coin["logo"])
    print("Last Update:", data["time"])

get_full_crypto_info("btc")
```

---

# 💻 Full Usage Example (Node.js / JavaScript)

```javascript
const API = "https://currency.api-sina-free.workers.dev/";

async function fetchCrypto(symbol) {
  try {
    const res = await fetch(`${API}?crypto=${symbol}`);
    const data = await res.json();

    if (data.activ !== 1) {
      console.log("Service inactive");
      return;
    }

    const coin = data.list[0];

    console.log("Name:", coin.name);
    console.log("Symbol:", coin.iso);
    console.log("USD:", coin.price);
    console.log("IRR:", coin.price_rial);
    console.log("Market Cap:", coin.market_cap);
    console.log("Change:", coin.daily_change_percent);
    console.log("Logo:", coin.logo);
    console.log("Updated:", data.time);

  } catch (err) {
    console.error("Network Error:", err);
  }
}

fetchCrypto("eth");
```

---

# 🤖 Full Usage in Rubika Bot (End-to-End)

```py
from rubpy import Client, filters
import requests

bot = Client(name="crypto_price_bot")
API = "https://currency.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip().lower()

    if not text.startswith("price"):
        return

    symbol = text.replace("price", "", 1).strip()
    if not symbol:
        return await message.reply("Example: price btc")

    try:
        res = requests.get(API, params={"crypto": symbol}, timeout=10)
        data = res.json()

        if data.get("activ") != 1:
            return await message.reply("Service is temporarily unavailable")

        if not data.get("list"):
            return await message.reply("Cryptocurrency not found")

        coin = data["list"][0]

        await message.reply(
            f"🪙 *{coin['name']} ({coin['iso']})*\n\n"
            f"🏆 Market Rank: {coin['rank']}\n"
            f"💲 USD Price: `{coin['price_string_format']}$`\n"
            f"💰 IRR Price: `{coin['price_rial']:,}`\n"
            f"🟢 Buy: `{coin['price_buy']:,}`\n"
            f"🔴 Sell: `{coin['price_sell']:,}`\n"
            f"📊 Market Cap: `{coin['market_cap']}`\n"
            f"📉 24h Change: `{coin['daily_change_percent']}%`\n"
            f"🪙 BTC Value: `{coin['price_bitcoin']}`\n\n"
            f"🕒 Updated at:\n`{data['time']}`\n\n"
            f"🖼 [View Logo]({coin['logo']})\n\n"
            f"📡 {data['channel']}\n"
            f"👤 {data['creator']}",
            parse_mode="markdown"
        )

    except Exception as e:
        await message.reply(f"Unexpected Error:\n{e}")

bot.run()
```

---

# ⚙️ Features

✅ No API Key required                           
✅ Real-time cryptocurrency prices                     
✅ Supports name and symbol lookup                      
✅ Cloudflare-proxied logos                         
✅ Fast, lightweight, and stable                     
✅ Production-ready REST API                         
✅ Hosted on Cloudflare Workers                      


---

# 🎯 Use Cases

● Cryptocurrency price bots                  
● Crypto websites                        
● Financial dashboards                       
● Trading applications                         
● Market monitoring tools                   
● Educational and professional projects                


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                       
🗳 Rubika: https://rubika.ir/Sinabani_api                     
🔗 API Endpoint: https://currency.api-sina-free.workers.dev/
