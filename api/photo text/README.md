# 🖼️ PhotoTextAPI version : 1.0.0

وب‌سرویس **PhotoTextAPI** یک API ساده، سریع و خلاقانه برای **تولید تصویر از متن** است 🎨  
با ارسال یک متن در URL، یک تصویر **PNG** با **پس‌زمینه‌ی رندوم** و متن در **مرکز تصویر** دریافت می‌کنید  
این سرویس از **زبان فارسی و انگلیسی** پشتیبانی می‌کند — **بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://photo-text.api-sina-free.workers.dev/{text}

---

## 📥 ورودی وب‌سرویس

| پارامتر | نوع | توضیح |
|--------|-----|--------|
| `text` | `string` | متنی که باید داخل تصویر نمایش داده شود |

📌 متن مستقیماً در مسیر URL قرار می‌گیرد

---

## 🧪 نمونه درخواست‌ها

### مثال ساده
`GET` https://photo-text.api-sina-free.workers.dev/Hello

### مثال فارسی
`GET` https://photo-text.api-sina-free.workers.dev/سلام

---

## 📦 خروجی وب‌سرویس

| ویژگی | توضیح |
|------|------|
| فرمت خروجی | PNG |
| Content-Type | image/png |
| پس‌زمینه | رنگ رندوم در هر درخواست |
| متن | قرار گرفته در مرکز تصویر |
| زبان | پشتیبانی از فارسی و انگلیسی |

---

## 📸 توضیح خروجی

📷 نتیجه درخواست، یک **تصویر PNG** است که:
- پس‌زمینه آن به‌صورت رندوم انتخاب می‌شود
- رنگ متن به‌صورت هوشمند و متضاد انتخاب می‌شود
- متن دقیقاً در مرکز تصویر قرار می‌گیرد

---

## 💻 نمونه استفاده در Python

```py
import requests

url = "https://photo-text.api-sina-free.workers.dev/Hello"
response = requests.get(url)

with open("hello.png", "wb") as f:
    f.write(response.content)

print("🖼 تصویر ذخیره شد")
```

---

# 💻 نمونه استفاده در JavaScript / Node.js

```js
import fetch from "node-fetch";
import fs from "fs";

const url = "https://photo-text.api-sina-free.workers.dev/Hello";

fetch(url)
  .then(res => res.arrayBuffer())
  .then(buf => fs.writeFileSync("hello.png", Buffer.from(buf)))
  .then(() => console.log("🖼 تصویر ذخیره شد"));
```

---

# 🤖 استفاده در ربات‌ها / Rubika

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_photo_text_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.startswith("عکس "):
        content = text.replace("عکس ", "").strip()
        if not content:
            return await message.reply("❗ لطفاً یک متن وارد کنید")

        image_url = f"https://photo-text.api-sina-free.workers.dev/{content}"
        await message.reply_photo(image_url, caption="🖼 تصویر ساخته شد")

bot.run()
```

---

# 🌐 استفاده در مرورگر

کافیست آدرس زیر را در مرورگر باز کنید 👇
https://photo-text.api-sina-free.workers.dev/test

📷 خروجی: تصویر PNG با متن test در مرکز تصویر


---

# 🔧 جزئیات فنی

بخش	توضیح

● Backend	FastAPI (Python)
● Image Engine	Pillow (PIL)
● Output Format	PNG
● Protocol	REST
● Content-Type	image/png



---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                  
🗳 Rubika: https://rubika.ir/Sinabani_api                     
🔗 Endpoint: https://photo-text.api-sina-free.workers.dev

---

---

# 🖼️ PhotoTextAPI version : 1.0.0

**PhotoTextAPI** is a simple, fast, and creative API for **generating images from text** 🎨  
By sending a text string in the URL, you receive a **PNG image** with a **random background color** and the text **centered in the image**  
This service supports **both English and Persian texts** — **No API key required** 🚀

---

## 🌐 API Endpoint

https://photo-text.api-sina-free.workers.dev/{text}

---

## 📥 API Input

| Parameter | Type | Description |
|----------|------|-------------|
| `text` | `string` | The text to be rendered inside the image |

📌 The text is passed directly in the URL path

---

## 🧪 Sample Requests

### Simple Example
`GET` https://photo-text.api-sina-free.workers.dev/Hello

### Persian Example
`GET` https://photo-text.api-sina-free.workers.dev/سلام

---

## 📦 API Output

| Feature | Description |
|-------|-------------|
| `Output` `format` | PNG |
| `Content-Type` | image/png |
| `Background` | Random color per request |
| `Text` `position` | Centered |
| `Language` `support` | English & Persian |

---

## 📸 Output Description

📷 The response is a **PNG image** where:
- The background color is randomly generated
- The text color is automatically chosen for better contrast
- The text is perfectly centered in the image

---

## 💻 Python Usage Example

```py
import requests

url = "https://photo-text.api-sina-free.workers.dev/Hello"
response = requests.get(url)

with open("hello.png", "wb") as f:
    f.write(response.content)

print("🖼 Image saved")
```

---

# 💻 JavaScript / Node.js Usage Example

```js
import fetch from "node-fetch";
import fs from "fs";

const url = "https://photo-text.api-sina-free.workers.dev/Hello";

fetch(url)
  .then(res => res.arrayBuffer())
  .then(buf => fs.writeFileSync("hello.png", Buffer.from(buf)))
  .then(() => console.log("🖼 Image saved!"));
```

---

# 🤖 Usage in Bots / Rubika

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_photo_text_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.startswith("image "):
        content = text.replace("image ", "").strip()
        if not content:
            return await message.reply("❗ Please provide a text")

        image_url = f"https://photo-text.api-sina-free.workers.dev/{content}"
        await message.reply_photo(image_url, caption="🖼 Image generated")

bot.run()
```

---

# 🌐 Browser Usage

Simply open the following URL in your browser 👇
https://photo-text.api-sina-free.workers.dev/test

📷 Output: A PNG image with the text test centered in the image

---

# 🔧 Technical Details

Component	Description

● Backend	FastAPI (Python)
● Image Engine	Pillow (PIL)
● Output Format	PNG
● Protocol	REST
● Content-Type	image/png

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                  
🗳 Rubika: https://rubika.ir/Sinabani_api                    
🔗 Endpoint: https://photo-text.api-sina-free.workers.dev
