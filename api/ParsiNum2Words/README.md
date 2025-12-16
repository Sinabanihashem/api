# ParsiNum2Words API version : 1.0.0

وب‌سرویس **ParsiNum2Words API** یک سرویس کاربردی برای **تبدیل عدد به حروف فارسی** است 🇮🇷  
این API به توسعه‌دهندگان اجازه می‌دهد با ارسال یک عدد (به‌صورت رشته)،  
نمایش متنی آن عدد را به **حروف فارسی استاندارد** دریافت کنند — **بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس

https://number.api-sina-free.workers.dev

---

## 📥 روش‌های استفاده

### 1️⃣ تبدیل عدد با GET

```http
GET https://number.api-sina-free.workers.dev/{number}
```

**🔹 مثال:**

```http
GET https://number.api-sina-free.workers.dev/12345
```

---

# 2️⃣ تبدیل عدد با POST

```http
POST https://number.api-sina-free.workers.dev/convert
```

**🔹 Body (JSON):**

```json
{
  "number": "987654321"
}
```

---

## 📦 خروجی وب‌سرویس

خروجی این API در هر دو روش **GET** و **POST** به‌صورت **JSON استاندارد** برگردانده می‌شود.

### 🔹 خروجی درخواست GET

در هنگام ارسال درخواست GET، پاسخ وب‌سرویس شامل ساختار زیر است:

| کلید | نوع | توضیح |
|-----|-----|-------|
| `input` | `string` | عددی که به API ارسال شده است |
| `output` | `string` | عدد تبدیل‌شده به حروف فارسی |


---

# 🧾 نمونه خروجی (GET)

```json
{
  "input": "12345",
  "output": "دوازده هزار و سیصد و چهل و پنج"
}
```

---

# 🧾 نمونه خروجی (POST)

```json
{
  "input": "987654321",
  "output": "نهصد و هشتاد و هفت میلیون و ششصد و پنجاه و چهار هزار و سیصد و بیست و یک"
}
```

---

# ⚙️ ویژگی‌ها

✅ پشتیبانی از اعداد بسیار بزرگ
✅ پشتیبانی از اعداد مثبت و منفی
✅ ورودی به‌صورت string برای جلوگیری از محدودیت عددی
✅ خروجی متنی استاندارد فارسی
✅ کاملاً RESTful
✅ بدون نیاز به API Key


---

# 💻 نمونه استفاده در Python

```py
import requests

url = "https://number.api-sina-free.workers.dev/123456789"
response = requests.get(url)

print(response.json())
```

---

# 💻 نمونه استفاده در Node.js / JavaScript

```js
import fetch from "node-fetch";

const url = "https://number.api-sina-free.workers.dev/98765";

fetch(url)
  .then(res => res.json())
  .then(data => console.log(data));
```

---

# 🌐 استفاده در مرورگر

فقط عدد را در انتهای آدرس بنویس 👇

https://number.api-sina-free.workers.dev/123456

📦 خروجی به‌صورت JSON نمایش داده می‌شود و شامل عدد به حروف فارسی است.


---

# 🎯 کاربردها

● فاکتور و سیستم‌های مالی

● تولید متن رسمی

● ربات‌ها و اپلیکیشن‌ها

● تبدیل مبلغ عددی به حروف



---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                      
🗳 Rubika: https://rubika.ir/Sinabani_api                
🔗 Endpoint: https://number.api-sina-free.workers.dev

---

---

# 🔢 ParsiNum2Words API version : 1.0.0

**ParsiNum2Words API** is a lightweight and practical web service for **converting numbers into Persian (Farsi) words** 🇮🇷  
This API allows developers to send a number (as a string) and receive its **standard Persian textual representation** — **No API Key required** 🚀

---

## 🌐 Service Base URL

https://number.api-sina-free.workers.dev

---

## 📥 Usage Methods

### 1️⃣ Convert Number using GET

```http
GET https://number.api-sina-free.workers.dev/{number}
```

**🔹 Example:**

```http
GET https://number.api-sina-free.workers.dev/12345
```

---

# 2️⃣ Convert Number using POST

```http
POST https://number.api-sina-free.workers.dev/convert
```

**🔹 Request Body (JSON):**

```json
{
  "number": "987654321"
}
```

---

## 📦 API Response Structure

### Output for GET request

When you make a GET request to the service, the response will contain the following structure:

| Key    | Type   | Description                                           |
|--------|--------|-------------------------------------------------------|
| `input`  | `string` | The input number that was provided                    |
| `output` | `string` | The input number converted into Persian words         |


---

# 🧾 Sample Response (GET)

```json
{
  "input": "12345",
  "output": "دوازده هزار و سیصد و چهل و پنج"
}
```

---

# 🧾 Sample Response (POST)

```json
{
  "input": "987654321",
  "output": "نهصد و هشتاد و هفت میلیون و ششصد و پنجاه و چهار هزار و سیصد و بیست و یک"
}
```

---

# ⚙️ Features

✅ Supports very large numbers
✅ Supports positive and negative numbers
✅ Input as string to avoid numeric limitations
✅ Standard Persian textual output
✅ Fully RESTful API
✅ No API Key required


---

# 💻 Python Example

```py
import requests

url = "https://number.api-sina-free.workers.dev/123456789"
response = requests.get(url)

print(response.json())
```

---

# 💻 Node.js / JavaScript Example

```js
import fetch from "node-fetch";

const url = "https://number.api-sina-free.workers.dev/98765";

fetch(url)
  .then(res => res.json())
  .then(data => console.log(data));
```

---

# 🌐 Browser Usage

Simply append the number to the URL 👇

https://number.api-sina-free.workers.dev/123456

📦 The response will be displayed in JSON format and contains the number written in Persian words.


---

# 🎯 Use Cases

● Financial systems and invoices

● Official text generation

● Bots and messaging platforms

● Converting numeric amounts to written form



---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                 
🗳 Rubika: https://rubika.ir/Sinabani_api                    
🔗 Endpoint: https://number.api-sina-free.workers.dev
