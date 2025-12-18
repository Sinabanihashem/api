# 🧠 DeepSeek API
### version : DeepSeek V3.1 Nex N1

وب‌سرویس **DeepSeek API** یک سرویس گفت‌وگوی هوشمند مبتنی بر **مدل قدرتمند DeepSeek V3.1 Nex N1** است 🤖💬  
این API با دریافت یک متن از کاربر، پاسخ هوشمند، دقیق و انسان‌گونه را به‌صورت **متنی** برمی‌گرداند —  
**بدون نیاز به API Key برای کاربران نهایی** 🚀

این سرویس روی **Cloudflare Workers** میزبانی شده و سرعت بالا، پایداری و مصرف منابع پایین را تضمین می‌کند.

---

## 🌐 آدرس وب‌سرویس

https://deepseek-v3.api-sina-free.workers.dev/

---

## 🔹 ورودی‌های وب‌سرویس

| پارامتر | نوع | توضیح |
|--------|----|------|
| `text` | `string` | متنی که می‌خواهید هوش مصنوعی DeepSeek به آن پاسخ دهد |

---

## 📦 خروجی وب‌سرویس

| پارامتر | نوع | توضیح |
|--------|----|------|
| `channel` | `string` | آیدی یا لینک کانال رسمی توسعه‌دهنده |
| `creator` | `string` | نام یا آیدی توسعه‌دهنده |
| `answer` | `string` | پاسخ تولیدشده توسط مدل DeepSeek V3.1 Nex N1 |

---

## 🧪 نمونه درخواست

```http
GET https://deepseek-v3.api-sina-free.workers.dev/?text=اسمت%20چیه؟
```

---

# 🧾 نمونه خروجی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "answer": "من DeepSeek V3.1 Nex N1 هستم؛ یک مدل هوش مصنوعی پیشرفته که برای پاسخ‌گویی دقیق، سریع و هوشمند طراحی شده‌ام 😊"
}
```

---

# ⚙️ ویژگی‌ها

✅ پاسخ‌دهی هوشمند با مدل DeepSeek V3.1 Nex N1                      
✅ درک قوی زبان فارسی و انگلیسی                              
✅ مناسب برای ربات‌ها، وب‌اپ‌ها و اپلیکیشن‌ها                       
✅ بدون نیاز به API Key                     
✅ کاملاً RESTful                          
✅ سبک، سریع و پایدار                            
✅ اجراشده روی Cloudflare Workers


---

# 💻 نمونه استفاده در Python

```py
import requests

text = "هوش مصنوعی یعنی چی؟"
url = f"https://deepseek-v3.api-sina-free.workers.dev/?text={text}"

res = requests.get(url, timeout=15)
data = res.json()

print("👤 Creator:", data["creator"])
print("📡 Channel:", data["channel"])
print("🧠 Answer:", data["answer"])
```

---

# 💻 نمونه استفاده در Node.js / JavaScript

```javascript
import fetch from "node-fetch";

const text = "هوش مصنوعی یعنی چی؟";
const url = `https://deepseek-v3.api-sina-free.workers.dev/?text=${encodeURIComponent(text)}`;

fetch(url)
  .then(res => res.json())
  .then(data => {
    console.log("🧠 Answer:", data.answer);
    console.log("👤 Creator:", data.creator);
    console.log("📡 Channel:", data.channel);
  })
  .catch(err => {
    console.error("❌ Error:", err);
  });
```

---

# 🤖 استفاده در ربات‌ها (Rubika)

```py
from rubpy import Client, filters
import requests

bot = Client(name="deepseek_v31_bot")

API_URL = "https://deepseek-v3.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not text.startswith("هوش"):
        return

    query = text.replace("هوش", "", 1).strip()
    if not query:
        return await message.reply("❗️ لطفاً یک متن وارد کنید.")

    try:
        res = requests.get(f"{API_URL}?text={query}", timeout=15)
        data = res.json()
        await message.reply(
            f"🧠 *پاسخ DeepSeek V3.1 Nex N1:*\n\n{data['answer']}",
            parse_mode="markdown"
        )
    except Exception as e:
        await message.reply(f"❌ خطا در ارتباط با سرور:\n{e}")

bot.run()
```

---

# 🎯 کاربردها

● ربات‌های گفت‌وگوی هوشمند
● پاسخ‌دهی خودکار کاربران
● دستیار هوش مصنوعی
● سیستم‌های پشتیبانی آنلاین
● اپلیکیشن‌های AI و چت
● پردازش و تولید متن در تمامی زبان‌ها


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                     
🗳 Rubika: https://rubika.ir/Sinabani_api                
🔗 Endpoint: https://deepseek-v3.api-sina-free.workers.dev/

---

---

# 🧠 DeepSeek API
### version : DeepSeek V3.1 Nex N1

**DeepSeek API** is an intelligent conversational web service powered by the  
**DeepSeek V3.1 Nex N1 model** 🤖💬  
This API receives a user text and returns a **smart, accurate, human-like response** in plain text —  
**No API Key required for end users** 🚀

The service is hosted on **Cloudflare Workers**, ensuring high speed, stability, and low latency.

---

## 🌐 Service Endpoint

https://deepseek-v3.api-sina-free.workers.dev/

---

## 🔹 Input Parameters

| Parameter | Type | Description |
|----------|------|------------|
| `text` | `string` | The text you want the DeepSeek AI to respond to |

---

## 📦 API Response

| Parameter | Type | Description |
|----------|------|------------|
| `channel` | `string` | Official developer channel ID |
| `creator` | `string` | Developer name or ID |
| `answer` | `string` | Response generated by the DeepSeek V3.1 Nex N1 model |

---

## 🧪 Sample Request

```http
GET https://deepseek-v3.api-sina-free.workers.dev/?text=What%20is%20your%20name%3F
```

---

# 🧾 Sample Response

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "answer": "I am DeepSeek V3.1 Nex N1, an advanced AI model designed to provide fast, accurate, and intelligent responses 😊"
}
```

---

# ⚙️ Features

✅ Intelligent responses powered by DeepSeek V3.1 Nex N1                  
✅ Strong understanding of English and Persian                    
✅ Ideal for bots, websites, and applications                  
✅ No API Key required                     
✅ Fully RESTful API                      
✅ Fast, lightweight, and reliable               
✅ Powered by Cloudflare Workers


---

# 💻 Sample Usage in Python

```py
import requests

text = "What is artificial intelligence?"
url = f"https://deepseek-v3.api-sina-free.workers.dev/?text={text}"

res = requests.get(url, timeout=15)
data = res.json()

print("👤 Creator:", data["creator"])
print("📡 Channel:", data["channel"])
print("🧠 Answer:", data["answer"])
```

---

# 💻 Sample Usage in Node.js / JavaScript

```javascript
import fetch from "node-fetch";

const text = "What is artificial intelligence?";
const url = `https://deepseek-v3.api-sina-free.workers.dev/?text=${encodeURIComponent(text)}`;

fetch(url)
  .then(res => res.json())
  .then(data => {
    console.log("🧠 Answer:", data.answer);
    console.log("👤 Creator:", data.creator);
    console.log("📡 Channel:", data.channel);
  })
  .catch(err => {
    console.error("❌ Error:", err);
  });
```

---

# 🤖 Sample Usage in Bots (Rubika)

```py
from rubpy import Client, filters
import requests

bot = Client(name="deepseek_v31_bot")

API_URL = "https://deepseek-v3.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not text.startswith("AI"):
        return

    query = text.replace("AI", "", 1).strip()
    if not query:
        return await message.reply("❗️ Please enter a text.")

    try:
        res = requests.get(f"{API_URL}?text={query}", timeout=15)
        data = res.json()
        await message.reply(
            f"🧠 *DeepSeek V3.1 Nex N1 Response:*\n\n{data['answer']}",
            parse_mode="markdown"
        )
    except Exception as e:
        await message.reply(f"❌ Server connection error:\n{e}")

bot.run()
```

---

# 🎯 Use Cases

● Intelligent chatbots
● Automated user support
● AI-powered assistants
● Conversational AI systems
● Text generation and analysis
● Multi-language AI applications


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                               
🗳 Rubika: https://rubika.ir/Sinabani_api                     
🔗 Endpoint: https://deepseek-v3.api-sina-free.workers.dev/
