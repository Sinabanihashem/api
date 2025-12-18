# 💎 Sina-Gemini API version : 1.0.0

وب‌سرویس **Sina-Gemini** یک سرویس چت هوشمند مبتنی بر مدل قدرتمند  
**Google Gemini 2.0 Flash (Experimental)** است 🤖⚡  
این API با دریافت یک متن، پاسخ را به‌صورت **سریع، هوشمند و قابل استفاده** برمی‌گرداند —  
**بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://gemini.api-sina-free.workers.dev/

---

## 🔹 ورودی‌های وب‌سرویس

| پارامتر | نوع | توضیح |
|-------|----|------|
| `text` | `string` | متنی که می‌خواهید Gemini به آن پاسخ دهد |

---

## 📦 خروجی وب‌سرویس

| پارامتر | نوع | توضیح |
|--------|----|------|
| `channel` | `string` | کانال رسمی توسعه‌دهنده |
| `creator` | `string` | نام یا آیدی توسعه‌دهنده |
| `answer` | `string` | پاسخ تولیدشده توسط Gemini |

---

## 🧪 نمونه درخواست

```http
GET https://gemini.api-sina-free.workers.dev/?text=سلام%20هوش%20مصنوعی
```

---

# 🧾 نمونه خروجی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "answer": "سلام! 😊 خوشحالم که باهات صحبت می‌کنم. چطور می‌تونم کمکت کنم؟"
}
```

---

# ⚙️ ویژگی‌ها

✅ پاسخ‌دهی بسیار سریع (Flash Model)                         
✅ مبتنی بر Google Gemini 2.0                      
✅ پشتیبانی کامل از زبان فارسی                         
✅ مناسب برای ربات‌ها و اپلیکیشن‌ها                      
✅ بدون نیاز به API Key                        
✅ RESTful و سبک                     
✅ میزبانی‌شده روی Cloudflare Workers


---

# 💻 نمونه استفاده در Node.js / JavaScript

```javascript
import fetch from "node-fetch";

const API_URL = "https://gemini.api-sina-free.workers.dev/";
const text = "هوش مصنوعی چیست؟";

fetch(`${API_URL}?text=${encodeURIComponent(text)}`)
  .then(res => res.json())
  .then(data => {
    console.log("🤖 Gemini Answer:", data.answer);
    console.log("👤 Creator:", data.creator);
    console.log("📡 Channel:", data.channel);
  })
  .catch(err => {
    console.error("❌ API Error:", err);
  });
```

---

# 💻 نمونه استفاده در Python

```py
import requests

url = "https://gemini.api-sina-free.workers.dev/?text=هوش%20مصنوعی%20چیست؟"
res = requests.get(url, timeout=15)
data = res.json()

print("👤 Creator:", data["creator"])
print("📡 Channel:", data["channel"])
print("🤖 Gemini Answer:", data["answer"])
```

---

# 🤖 نمونه استفاده در ربات‌های Rubika

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_gemini_bot")
API_URL = "https://gemini.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not text.startswith("جمنای"):
        return

    query = text.replace("جمنای", "", 1).strip()
    if not query:
        return await message.reply("❗️ لطفاً یک متن وارد کنید.")

    try:
        res = requests.get(f"{API_URL}?text={query}", timeout=15)
        data = res.json()

        if "answer" in data:
            await message.reply(
                f"🤖 *پاسخ Gemini:*\n\n{data['answer']}",
                parse_mode="markdown"
            )
        else:
            await message.reply("⚠️ پاسخی دریافت نشد.")
    except Exception as e:
        await message.reply(f"❌ خطای ارتباط با سرور:\n{e}")

bot.run()
```

---

# 🎯 کاربردها

● ربات‌های گفت‌وگو
● پاسخ‌گویی هوشمند کاربران
● دستیار هوش مصنوعی
● تولید متن و ایده
● استفاده در پروژه‌های شخصی و تجاری


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                               
🗳 Rubika: https://rubika.ir/Sinabani_api                       
🔗 Endpoint: https://gemini.api-sina-free.workers.dev/

---

---

# 💎 Sina-Gemini API  
### Version : 1.0.0

**Sina-Gemini API** is a smart and fast chat service powered by  
**Google Gemini 2.0 Flash (Experimental)** 🤖⚡  

This API receives a text input and returns an **intelligent, ready-to-use response**,  
perfect for **bots, applications, and AI assistants** —  
**No API Key required** 🚀

---

## 🌐 Service Endpoint

https://gemini.api-sina-free.workers.dev/

---

## 🔹 Input Parameters

| Parameter | Type | Description |
|----------|------|-------------|
| `text` | `string` | The text you want Gemini to respond to |

---

## 📦 API Response

| Parameter | Type | Description |
|----------|------|-------------|
| `channel` | `string` | Official developer channel |
| `creator` | `string` | Developer ID |
| `answer` | `string` | Response generated by Gemini |

---

## 🧪 Sample Request

```http
GET https://gemini.api-sina-free.workers.dev/?text=Hello
```

---

# 🧾 Sample Response

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "answer": "Hello! 👋 How can I help you today?"
}
```

---

# ⚙️ Features

✅ Powered by Google Gemini 2.0 Flash                     
✅ Ultra-fast response time                 
✅ Multi-language support                     
✅ No API Key required                  
✅ Fully RESTful                    
✅ Lightweight and scalable.                  
✅ Hosted on Cloudflare Workers


---

# 💻 Usage Example (Node.js / JavaScript)

```javascript
import fetch from "node-fetch";

const API_URL = "https://gemini.api-sina-free.workers.dev/";
const text = "What is artificial intelligence?";

fetch(`${API_URL}?text=${encodeURIComponent(text)}`)
  .then(res => res.json())
  .then(data => {
    console.log("🤖 Gemini Answer:", data.answer);
    console.log("👤 Creator:", data.creator);
    console.log("📡 Channel:", data.channel);
  })
  .catch(err => {
    console.error("❌ API Error:", err);
  });
```

---

# 💻 Usage Example (Python)

```py
import requests

url = "https://gemini.api-sina-free.workers.dev/?text=What%20is%20AI?"
response = requests.get(url, timeout=15)
data = response.json()

print("👤 Creator:", data["creator"])
print("📡 Channel:", data["channel"])
print("🤖 Gemini Answer:", data["answer"])
```

---

# 🤖 Example Usage in Chat Bots

This API is suitable for integration with messaging platforms
such as Telegram, Rubika, or any custom chatbot backend.

Flow:

1. Receive user message


2. Send text to Sina-Gemini API


3. Return answer to the user




---

# 🎯 Use Cases

● Intelligent chatbots
● AI assistants
● Automated customer support
● Text generation
● Educational and personal projects


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                          
🗳 Rubika: https://rubika.ir/Sinabani_api                 
🔗 Endpoint: https://gemini.api-sina-free.workers.dev/
