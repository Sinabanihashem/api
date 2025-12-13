# 🚧 SinaCaptchaAPI version : 1.0.0

وب‌سرویس **SinaCaptchaAPI** یک سرویس آنلاین برای **تولید و اعتبارسنجی کپچا** است 🔐  
این API با هر درخواست، یک **کپچای ۴ رقمی** تولید می‌کند و تصویر آن را به‌صورت **Base64** برمی‌گرداند  
همچنین امکان **بررسی صحت پاسخ کاربر** نیز فراهم شده است — **بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://captcha.api-sina-free.workers.dev/captcha

---

## 📥 ورودی‌های وب‌سرویس

### 🔹 1. تولید کپچا
این درخواست **ورودی ندارد**

### 🔹 2. بررسی کپچا

| پارامتر | نوع | توضیح |
|--------|-----|--------|
| `captcha_id` | `string` | شناسه کپچا که هنگام تولید دریافت شده |
| `user_input` | `string` | کدی که کاربر از تصویر کپچا وارد کرده |

---

## 📦 خروجی‌های وب‌سرویس

### 🔹 خروجی تولید کپچا

| کلید | نوع | توضیح |
|-----|-----|--------|
| `creator` | `string` | شناسه توسعه‌دهنده |
| `captcha_id` | `string` | شناسه منحصر به‌فرد کپچا |
| `captcha_base64` | `string` | تصویر کپچا به‌صورت Base64 |

### 🔹 خروجی بررسی کپچا

| کلید | نوع | توضیح |
|-----|-----|--------|
| `ok` | `boolean` | وضعیت صحت پاسخ (true / false) |
| `message` | `string` | پیام توضیحی نتیجه بررسی |

---

## 🧪 نمونه درخواست‌ها

### دریافت کپچا (Base64 JSON)

`GET` https://captcha.api-sina-free.workers.dev/captcha

### بررسی کپچا

`GET` https://captcha.api-sina-free.workers.dev/captcha/verify?captcha_id=<captcha_id>&user_input=1234

---

## 🧾 نمونه خروجی تولید کپچا

```json
{
  "creator": "@Sinabani_api",
  "captcha_id": "e8a1f5c8-2d4b-4f0d-8f4d-123456789abc",
  "captcha_base64": "data:image/png;base64,iVBORw0KUgAA..."
}
```

---

# 🧾 نمونه خروجی بررسی کپچا

```json
{
  "ok": true,
  "message": "کپچا صحیح است."
}
```

---

# 💻 نمونه استفاده در Python

```py
import requests

# Generate Captcha
res = requests.get("https://captcha.api-sina-free.workers.dev/captcha")
data = res.json()

print("👤 Creator:", data["creator"])
print("📝 Captcha ID:", data["captcha_id"])
print("🖼 Captcha Base64:", data["captcha_base64"])

# Verify Captcha
captcha_id = data["captcha_id"]
user_input = "1234"

verify = requests.get(
    f"https://captcha.api-sina-free.workers.dev/captcha/verify?captcha_id={captcha_id}&user_input={user_input}"
)

print(verify.json())
```

---

# 🤖 استفاده در ربات‌ها / Rubika




---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers              
🗳 Rubika: https://rubika.ir/Sinabani_api                
🔗 Endpoint: https://captcha.api-sina-free.workers.dev/captcha

---

---


# 🚧 SinaCaptchaAPI version : 1.0.0

**SinaCaptchaAPI** is an online service for **generating and validating CAPTCHA images** 🔐  
With each request, it generates a **4-digit CAPTCHA**, returns the image as **Base64**,  
and provides an endpoint to **verify the user’s input** — **No API key required** 🚀

---

## 🌐 API Endpoint

https://captcha.api-sina-free.workers.dev/captcha

---

## 📥 API Inputs

### 🔹 1. Generate CAPTCHA
This request **does not require any input parameters**

### 🔹 2. Verify CAPTCHA

| Parameter | Type | Description |
|----------|------|-------------|
| `captcha_id` | `string` | CAPTCHA ID received during generation |
| `user_input` | `string` | Code entered by the user from the CAPTCHA image |

---

## 📦 API Outputs

### 🔹 CAPTCHA Generation Response

| Key | Type | Description |
|-----|------|-------------|
| `creator` | `string` | Developer identifier |
| `captcha_id` | `string` | Unique CAPTCHA identifier |
| `captcha_base64` | `string` | CAPTCHA image encoded in Base64 |

### 🔹 CAPTCHA Verification Response

| Key | Type | Description |
|-----|------|-------------|
| `ok` | `boolean` | Validation status (true / false) |
| `message` | `string` | Descriptive verification message |

---

## 🧪 Sample Requests

### Get CAPTCHA (Base64 JSON)

`GET` https://captcha.api-sina-free.workers.dev/captcha

### Verify CAPTCHA

`GET` https://captcha.api-sina-free.workers.dev/captcha/verify?captcha_id=<captcha_id>&user_input=1234

---

## 🧾 Sample CAPTCHA Generation Response

```json
{
  "creator": "@Sinabani_api",
  "captcha_id": "e8a1f5c8-2d4b-4f0d-8f4d-123456789abc",
  "captcha_base64": "data:image/png;base64,iVBORw0KUgAA..."
}
```

---

# 🧾 Sample CAPTCHA Verification Response

```json
{
  "ok": true,
  "message": "CAPTCHA is valid."
}
```

---

# 💻 Python Usage Example

```py
import requests

# Generate CAPTCHA
res = requests.get("https://captcha.api-sina-free.workers.dev/captcha")
data = res.json()

print("👤 Creator:", data["creator"])
print("📝 Captcha ID:", data["captcha_id"])
print("🖼 Captcha Base64:", data["captcha_base64"])

# Verify CAPTCHA
captcha_id = data["captcha_id"]
user_input = "1234"

verify = requests.get(
    f"https://captcha.api-sina-free.workers.dev/captcha/verify?captcha_id={captcha_id}&user_input={user_input}"
)

print(verify.json())
```

---

# 🤖 Usage in Bots (Rubika / Chatbots)



---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                 
🗳 Rubika: https://rubika.ir/Sinabani_api            
🔗 Endpoint: https://captcha.api-sina-free.workers.dev/captcha
