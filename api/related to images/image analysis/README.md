# 🔍 SinaImageOCR — نسخه 1.0.0

SinaImageOCR یک سرویس سریع و سبک برای استخراج متن از تصاویر است (OCR).  
شما می‌توانید تصویر خود را **ارسال فایل** کنید یا **لینک مستقیم تصویر** بدهید و سرویس متن موجود در تصویر را برایتان بازگرداند.  
این API بدون هیچ کلید دسترسی و بدون نیاز به تنظیمات پیچیده قابل استفاده است.

---

## 🌐 آدرس درخواست

**ارسال فایل تصویر (POST)**

https://image-analysis.api-sina-free.workers.dev/

**ارسال لینک مستقیم تصویر (GET)**

https://image-analysis.api-sina-free.workers.dev/?url=`<IMAGE_URL>`

---

## 🔎 پارامترهای ورودی

| پارامتر | توضیح | ضرورات |
|--------|--------|--------|
| image | فایل تصویر (PNG, JPG, JPEG, WEBP, GIF) | اجباری (برای POST) |
| url | لینک مستقیم تصویر | اجباری (برای GET) |

---

## 📦 خروجی JSON

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "success": true,
  "language": "fa",
  "text": "متن استخراج شده از تصویر"
}
```

---

### توضیح فیلدهای خروجی

| فیلد      | نوع داده | توضیح                                                                 |
|-----------|---------|------------------------------------------------------------------------|
| channel   | string  | ثابت: `@Sinabani_api`                                                 |
| creator   | string  | ثابت: `@Sinabanis`                                                    |
| success   | boolean | وضعیت موفقیت عملیات (true = موفق، false = ناموفق)                     |
| language  | string  | زبان متن استخراج شده (`fa` / `en` / `mixed` / `unknown`)              |
| text      | string  | متن استخراج شده از تصویر                                               |

---

**🧪 نمونه درخواست**

POST با فایل

```bash
curl -X POST -F "image=@test.png" https://image-analysis.api-sina-free.workers.dev/
```

GET با لینک تصویر

```http
https://image-analysis.api-sina-free.workers.dev/?url=https://example.com/test.png
```

---

# 💻 نمونه استفاده در Python
```py
import requests

# حالت فایل
with open("test.png", "rb") as f:
    res = requests.post("https://image-analysis.api-sina-free.workers.dev/", files={"image": f})

print(res.json())

# حالت لینک
url = "https://image-analysis.api-sina-free.workers.dev/?url=https://example.com/test.png"
res = requests.get(url)
print(res.json())
```

---

# 🤖 نمونه ربات روبیکا (Python)
```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_ocr_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    txt = message.text.strip()

    if txt.startswith("ocr "):
        arg = txt.replace("ocr ", "")
        if arg.startswith("http"):
            link = f"https://image-analysis.api-sina-free.workers.dev/?url={arg}"
            res = requests.get(link).json()
        else:
            with open(arg, "rb") as f:
                res = requests.post("https://image-analysis.api-sina-free.workers.dev/", files={"image": f}).json()

        await message.reply_text(f"Extracted Text:\n{res.get('text','No text found')}")

bot.run()
```

---

# 🎯 ویژگی‌های سرویس

● دریافت تصویر از فایل یا لینک مستقیم

● پشتیبانی از PNG، JPG، JPEG، WEBP، GIF

● تشخیص خودکار زبان متن (فارسی / انگلیسی / ترکیبی)

● خروجی JSON با اطلاعات ثابت channel و creator

● بدون نیاز به API Key

● سریع و سبک


---

# 👤 Developer

mir sina banihashem
📍 Hosted on Cloudflare Workers
🛠 Rubika: https://rubika.ir/Sinabani_api
🔗 Endpoint: https://image-analysis.api-sina-free.workers.dev/

---
---

# 🔍 SinaImageOCR — Version 1.0.0

SinaImageOCR is a fast and lightweight service for extracting text from images (OCR).  
You can **upload your image** or provide a **direct image URL**, and the service will return the text contained in the image.  
This API requires no access key and no complicated setup.

---

## 🌐 Request URL

**Upload image file (POST)**

```http
https://image-analysis.api-sina-free.workers.dev/
```

**Direct image URL (GET)**

```http
https://image-analysis.api-sina-free.workers.dev/?url=<IMAGE_URL>
```

---

## 🔎 Input Parameters

| Parameter | Description | Required |
|-----------|------------|---------|
| image     | Image file (PNG, JPG, JPEG, WEBP, GIF) | Required (for POST) |
| url       | Direct image URL | Required (for GET) |

---

## 📦 JSON Output

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "success": true,
  "language": "fa",
  "text": "Extracted text from the image"
}
```

---

### Output Fields Description

| Field     | Data Type | Description |
|-----------|-----------|------------|
| channel   | string    | Fixed: `@Sinabani_api` |
| creator   | string    | Fixed: `@Sinabanis` |
| success   | boolean   | Operation success status (true = successful, false = failed) |
| language  | string    | Detected text language (`fa` / `en` / `mixed` / `unknown`) |
| text      | string    | Extracted text from the image |

---

# 🧪 Example Requests

**POST with file**

```curl -X POST -F "image=@test.png" https://image-analysis.api-sina-free.workers.dev/```

**GET with image URL**

```https://image-analysis.api-sina-free.workers.dev/?url=https://example.com/test.png```


---

# 💻 Python Example

```py
import requests

# File upload
with open("test.png", "rb") as f:
    res = requests.post("https://image-analysis.api-sina-free.workers.dev/", files={"image": f})

print(res.json())

# Direct URL
url = "https://image-analysis.api-sina-free.workers.dev/?url=https://example.com/test.png"
res = requests.get(url)
print(res.json())
```

---

# 🤖 Rubika Bot Example (Python)

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_ocr_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    txt = message.text.strip()

    if txt.startswith("ocr "):
        arg = txt.replace("ocr ", "")
        if arg.startswith("http"):
            link = f"https://image-analysis.api-sina-free.workers.dev/?url={arg}"
            res = requests.get(link).json()
        else:
            with open(arg, "rb") as f:
                res = requests.post("https://image-analysis.api-sina-free.workers.dev/", files={"image": f}).json()

        await message.reply_text(f"Extracted Text:\n{res.get('text','No text found')}")

bot.run()
```

---

# 🎯 Service Features

● Accepts image from file upload or direct URL

● Supports PNG, JPG, JPEG, WEBP, GIF

● Automatic language detection (Persian / English / Mixed)

● JSON output with fixed channel and creator fields

● No API key required

● Fast and lightweight


---

# 👤 Developer

mir sina banihashem
📍 Hosted on Cloudflare Workers
🛠 Rubika: https://rubika.ir/Sinabani_api
🔗 Endpoint: https://image-analysis.api-sina-free.workers.dev/
