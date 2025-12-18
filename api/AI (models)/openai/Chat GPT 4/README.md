# 🤖 Sina-GPT4 API version : 1.0.0

وب‌سرویس **Sina-GPT4** یک سرویس چت هوشمند با مدل **Chat GPT 4** است. 🤖💬  
این API با دریافت یک متن از کاربر، پاسخ را به‌صورت **هوشمند و قابل استفاده** برمی‌گرداند —  
**بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://gpt4.api-sina-free.workers.dev/gpt4

---

## 🔹 ورودی‌های وب‌سرویس

| پارامتر | نوع | توضیح |
|-------|----|------|
| `text` | `string` | متنی که می‌خواهید GPT-4 به آن پاسخ دهد |

---

## 📦 خروجی وب‌سرویس

| پارامتر | نوع | توضیح |
|--------|----|------|
| `Channels` | `string` | لینک کانال‌های رسمی توسعه‌دهنده |
| `Developed By` | `string` | نام یا آیدی توسعه‌دهنده |
| `result` | `string` | پاسخ تولیدشده توسط GPT-4 |
| `Result` | `string` | نسخه تکراری پاسخ (برای سازگاری با برخی بات‌ها) |

---

## 🧪 نمونه درخواست

```http
GET https://gpt4.api-sina-free.workers.dev/gpt4?text=سلام%20عزیزم
```

---

# 🧾 نمونه خروجی

```json
{
  "Channels": "in Rubika @Sinabani_api in Telegram @Sinabanis_api",
  "Developed By": "@Sinabanis",
  "result": "سلام! چطور می‌توانم به شما کمک کنم؟ اگر سوالی داری، راحت بپرس 😊",
  "Result": "سلام! چطور می‌توانم به شما کمک کنم؟ اگر سوالی داری، راحت بپرس 😊"
}
```

---

# ⚙️ ویژگی‌ها

✅ پاسخ‌دهی هوشمند مبتنی بر GPT-4           
✅ پشتیبانی کامل از زبان فارسی                
✅ مناسب برای ربات‌ها و اپلیکیشن‌ها             
✅ بدون نیاز به API Key                   
✅ کاملاً RESTful                        
✅ پاسخ سریع و سبک                      


---

## 💻 نمونه استفاده در Node.js / جاوااسکریپت

```javascript
import fetch from "node-fetch";

const API_URL = "https://gpt4.api-sina-free.workers.dev/gpt4";
const text = "حال شما چطوره؟";

fetch(`${API_URL}?text=${encodeURIComponent(text)}`)
  .then(res => res.json())
  .then(data => {
    console.log("🤖 پاسخ GPT-4:", data.result);
    console.log("👤 توسعه‌دهنده:", data["Developed By"]);
    console.log("📡 کانال‌ها:", data.Channels);
  })
  .catch(err => {
    console.error("❌ خطا در اتصال به API:", err);
  });
```

---

# 💻 نمونه استفاده در Python

```py
import requests

url = "https://gpt4.api-sina-free.workers.dev/gpt4?text=حال%20شما%20چطوره؟"
res = requests.get(url)
data = res.json()

print("👤 Developer:", data["Developed By"])
print("📡 Channels:", data["Channels"])
print("🤖 GPT-4 Answer:", data["result"])
```

---

# 🤖 استفاده در ربات‌ها (Rubika)

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_gpt4_bot")

API_URL = "https://gpt4.api-sina-free.workers.dev/gpt4"

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

        if "result" in data:
            await message.reply(f"🤖 *پاسخ GPT-4:*\n\n{data['result']}", parse_mode="markdown")
        else:
            await message.reply("⚠️ خطا در دریافت پاسخ.")
    except Exception as e:
        await message.reply(f"❌ خطای ارتباط با سرور:\n{e}")

bot.run()
```

---

# 🎯 کاربردها

● ربات‌های گفت‌وگو (Chat Bots)

● پاسخ‌گویی هوشمند کاربران

● هوش مصنوعی متنی

● دستیار هوش مصنوعی در پروژه‌ها



---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                 
🗳 Rubika: https://rubika.ir/Sinabani_api                 
🔗 Endpoint: https://gpt4.api-sina-free.workers.dev/gpt4

---

---

# 🤖 Sina-GPT4 API version : 1.0.0

**Sina-GPT4 API** is an intelligent chat service based on **GPT-4** 🤖💬  
This API receives a text from the user and returns a **smart, response**, ready for integration into **bots and applications** —  
**No API Key required** 🚀

---

## 🌐 Service Endpoint

https://gpt4.api-sina-free.workers.dev/gpt4

---

## 🔹 Input Parameters

| Parameter | Type | Description |
|----------|------|------------|
| `text`     | `string` | The text you want GPT-4 to respond to |

---

## 📦 API Response

| Parameter     | Type   | Description |
|---------------|--------|-------------|
| `Channels`      | `string` | Official developer channels |
| `Developed By`  | `string` | Developer name or ID |
| `result`        | `string` | Response generated by GPT-4 |
| `Result`        | `string` | Duplicate of `result` for compatibility with some bots |

---

## 🧪 Sample Request

```http
GET https://gpt4.api-sina-free.workers.dev/gpt4?text=Hello
```

---

# 🧾 Sample Response

```json
{
  "Channels": "in Rubika @Sinabani_api in Telegram @Sinabanis_api",
  "Developed By": "@Sinabanis",
  "result": "Hello! How can I help you today? Feel free to ask any question 😊",
  "Result": "Hello! How can I help you today? Feel free to ask any question 😊"
}
```

---

# ⚙️ Features

✅ GPT-4 powered intelligent responses                  
✅ Full support for all languages                            
✅ Suitable for bots and applications                   
✅ No API Key required                
✅ Fully RESTful                     
✅ Lightweight and fast              


---

# 💻 Sample Usage in Python

```py
import requests

url = "https://gpt4.api-sina-free.workers.dev/gpt4?text=How are you?"
res = requests.get(url)
data = res.json()

print("👤 Developer:", data["Developed By"])
print("📡 Channels:", data["Channels"])
print("🤖 GPT-4 Answer:", data["result"])
```

---

# 💻 Sample Usage in Node.js / JavaScript

```javascript
import fetch from "node-fetch";

const API_URL = "https://gpt4.api-sina-free.workers.dev/gpt4";
const text = "How are you today?";

fetch(`${API_URL}?text=${encodeURIComponent(text)}`)
  .then(res => res.json())
  .then(data => {
    console.log("🤖 GPT-4 Answer:", data.result);
    console.log("👤 Developer:", data["Developed By"]);
    console.log("📡 Channels:", data.Channels);
  })
  .catch(err => {
    console.error("❌ Error while connecting to API:", err);
  });
```

---

# 🤖 Sample Usage in Rubika Bots

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_gpt4_bot")
API_URL = "https://gpt4.api-sina-free.workers.dev/gpt4"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not text.startswith("GPT"):
        return

    query = text.replace("GPT", "", 1).strip()
    if not query:
        return await message.reply("❗️ Please enter a text to send to GPT-4.")

    try:
        res = requests.get(f"{API_URL}?text={query}", timeout=15)
        data = res.json()

        if "result" in data:
            await message.reply(f"🤖 *GPT-4 Response:*\n\n{data['result']}", parse_mode="markdown")
        else:
            await message.reply("⚠️ Error: No response received.")
    except Exception as e:
        await message.reply(f"❌ Connection error:\n{e}")

bot.run()
```

---

# 🎯 Use Cases

● Intelligent chatbots

● Automated user support

● Persian text generation

● AI assistants in applications


---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                    
🗳 Rubika: https://rubika.ir/Sinabani_api                
🔗 Endpoint: https://gpt4.api-sina-free.workers.dev/gpt4
