# 🌐 DomainAnalyzerAPI — نسخه 1.0.0

وب‌سرویس **DomainAnalyzerAPI** یک API قدرتمند، سریع و کاملاً رایگان برای **آنالیز کامل دامنه و IP** است.  
این سرویس بدون نیاز به API Key، اطلاعات بسیار کاملی شامل:

- 🔍 DNS Lookup
- 📄 WHOIS دامنه
- 🌍 WHOIS و موقعیت جغرافیایی IP
- ☁️ تشخیص CDN (مانند Cloudflare)
- 🛡 بررسی Proxy / VPN / TOR
- 📡 اطلاعات ASN، ISP، تایم‌زون، Fraud Score

را در قالب یک خروجی JSON منظم ارائه می‌دهد.

اگر برای **ربات، پنل مدیریتی، ابزار امنیتی یا مانیتورینگ دامنه** دنبال یک API کامل هستی، این وب‌سرویس دقیقاً برای همینه ⚡

---

## 🌐 آدرس وب‌سرویس

| توضیح | لینک |
|------|------|
| آنالیز کامل دامنه | https://abolfazlzarei.sbs/domain/?action=analyze&domain=example.com |

---

## 🔎 پارامترهای ورودی

| پارامتر | نوع | اجباری | توضیح |
|--------|-----|--------|-------|
| `action` | string | ✅ | مقدار ثابت `analyze` |
| `domain` | string | ✅ | دامنه موردنظر (بدون http/https) |

### 📌 مثال:
```http
?action=analyze&domain=tabairan.com
```

---

## 📦 ساختار کلی پاسخ

```json
{
  "creator": "string",
  "channel": "string",
  "data": {
    "dns_lookup": {},
    "domain_whois": {},
    "ip_whois": {},
    "ip_location": {}
  }
}
```

---

🧩 توضیح کامل بخش‌های خروجی


---

## 🔹 DNS Lookup

این بخش وظیفه بررسی وضعیت DNS دامنه و استخراج اطلاعات مرتبط با NameServerها و IP اصلی دامنه را بر عهده دارد.

### 📦 ساختار خروجی

| فیلد | نوع | توضیح |
|----|----|------|
| ok | boolean | نشان‌دهنده موفق بودن عملیات |
| results.domain | string | نام دامنه آنالیزشده |
| results.ip | string | آدرس IP متصل به دامنه |
| results.dns | array | لیست NameServerها و رکوردهای مرتبط (NS / PTR) |

### 📌 کاربردها
- تشخیص استفاده از CDN (مانند Cloudflare)
- بررسی NameServerهای دامنه
- استخراج IP اصلی دامنه

---

## 🔹 Domain WHOIS

این بخش اطلاعات ثبت دامنه را از پایگاه‌های WHOIS استخراج می‌کند و شامل جزئیات مالکیت، رجیسترار و وضعیت دامنه است.

### 📦 ساختار خروجی

| فیلد | نوع | توضیح |
|----|----|------|
| domain | string | نام دامنه |
| domain_id | string | شناسه یکتای دامنه |
| status | string | وضعیت دامنه در ICANN |
| create_date | string | تاریخ ثبت دامنه |
| update_date | string | آخرین بروزرسانی |
| expire_date | string | تاریخ انقضای دامنه |
| domain_age | number | عمر دامنه (برحسب روز) |
| whois_server | string | سرور WHOIS |
| registrar | object | اطلاعات رجیسترار |
| registrant | object | اطلاعات مالک دامنه |
| admin | object | اطلاعات مدیر دامنه |
| tech | object | اطلاعات فنی دامنه |
| nameservers | array | NameServerهای ثبت‌شده |

### 📌 کاربردها
- بررسی اعتبار دامنه
- تشخیص دامنه‌های تازه‌ثبت‌شده
- تحلیل مالکیت دامنه

---

## 🔹 IP WHOIS

این بخش اطلاعات شبکه‌ای و مالکیتی مربوط به آدرس IP دامنه را نمایش می‌دهد.

### 📦 ساختار خروجی

| فیلد | نوع | توضیح |
|----|----|------|
| ip | string | آدرس IP |
| type | string | IPv4 یا IPv6 |
| continent | string | قاره |
| country | string | کشور |
| region | string | استان / ایالت |
| city | string | شهر |
| latitude | number | عرض جغرافیایی |
| longitude | number | طول جغرافیایی |
| isp | string | ارائه‌دهنده اینترنت |
| org | string | سازمان مالک IP |
| asn | number | شماره Autonomous System |
| timezone | object | اطلاعات تایم‌زون |
| flag | object | پرچم کشور |

### 📌 کاربردها
- شناسایی محل سرور
- تشخیص دیتاسنتر یا ISP
- تحلیل مالکیت

---

## 🔹 IP Location & Security

این بخش اطلاعات پیشرفته موقعیت‌یابی و وضعیت امنیتی IP را ارائه می‌دهد.

### 📦 ساختار خروجی

| فیلد | نوع | توضیح |
|----|----|------|
| usage_type | string | نوع استفاده (CDN / Hosting / Residential) |
| address_type | string | Anycast یا Unicast |
| is_proxy | boolean | بررسی پراکسی بودن IP |
| is_vpn | boolean | بررسی VPN |
| is_tor | boolean | بررسی شبکه TOR |
| is_data_center | boolean | دیتاسنتر بودن IP |
| fraud_score | number | امتیاز ریسک (۰ کم‌خطر ← ۱۰۰ پرخطر) |
| net_speed | string | سرعت شبکه |
| ads_category | string | دسته‌بندی تبلیغاتی |
| time_zone_info | object | اطلاعات زمانی محلی |

### 📌 کاربردها
- افزایش امنیت ربات‌ها و وب‌سایت‌ها
- شناسایی IPهای مشکوک
- جلوگیری از تقلب و سوءاستفاده

---

# 🧪 نمونه درخواست

```http
GET https://abolfazlzarei.sbs/domain/?action=analyze&domain=tabairan.com
```

---

# 🧾 نمونه خروجی

```json
{
    "creator": "@SBCS_IR",
    "channel": "@NingaCode",
    "data": {
        "dns_lookup": {
            "ok": true,
            "results": {
                "domain": "tabairan.com",
                "ip": "173.245.59.114",
                "dns": [
                    "gabe.ns.cloudflare.com",
                    "dns.cloudflare.com",
                    "gabe.ns.cloudflare.com",
                    "ptr.atlas.tbns.ir"
                ]
            }
        },
        "domain_whois": {
            "domain": "tabairan.com",
            "domain_id": "2092063745_DOMAIN_COM-VRSN",
            "status": "http:\/\/www.icann.org\/epp#clientTransferProhibited",
            "create_date": "2017-01-22T04:55:23Z",
            "update_date": "2025-01-16T06:58:29Z",
            "expire_date": "2027-01-22T07:55:23Z",
            "domain_age": 3297,
            "whois_server": "whois.apiname.com",
            "registrar": {
                "iana_id": "1601",
                "name": "Atak Domain",
                "url": "http:\/\/apiname.com"
            },
            "registrant": {
                "name": "Privacy Protect",
                "organization": "n\/a",
                "street_address": "10, Smriti Chowk,",
                "city": "Dehra Dun",
                "region": "Tripura",
                "zip_code": "457490",
                "country": "IN",
                "phone": "+91.828195652",
                "fax": "+91.00",
                "email": "domain@privacyprotect.biz"
            },
            "admin": {
                "name": "Privacy Protect",
                "organization": "n\/a",
                "street_address": "10, Smriti Chowk,",
                "city": "Dehra Dun",
                "region": "Tripura",
                "zip_code": "457490",
                "country": "IN",
                "phone": "+91.828195652",
                "fax": "+91.00",
                "email": "domain@privacyprotect.biz"
            },
            "tech": {
                "name": "Privacy Protect",
                "organization": "n\/a",
                "street_address": "10, Smriti Chowk,",
                "city": "Dehra Dun",
                "region": "Tripura",
                "zip_code": "457490",
                "country": "IN",
                "phone": "+91.828195652",
                "fax": "+91.00",
                "email": "domain@privacyprotect.biz"
            },
            "billing": {
                "name": "",
                "organization": "",
                "street_address": "",
                "city": "",
                "region": "",
                "zip_code": "",
                "country": "",
                "phone": "",
                "fax": "",
                "email": ""
            },
            "nameservers": [
                "no name server"
            ]
        },
        "ip_whois": {
            "ok": true,
            "result": {
                "ip": "173.245.59.114",
                "type": "IPv4",
                "continent": "North America",
                "continent_code": "NA",
                "country": "United States",
                "country_code": "US",
                "region": "California",
                "region_code": "CA",
                "city": "San Francisco",
                "latitude": 37.718128,
                "longitude": -122.4343849,
                "is_eu": false,
                "postal": "94102",
                "calling_code": "1",
                "capital": "Washington D.C.",
                "borders": "CA,MX",
                "flag": {
                    "img": "https:\/\/cdn.ipwhois.io\/flags\/us.svg",
                    "emoji": "🇺🇸",
                    "emoji_unicode": "U+1F1FA U+1F1F8"
                },
                "connection": {
                    "asn": 13335,
                    "org": "Cloudflare, Inc.",
                    "isp": "Cloudflare, Inc.",
                    "domain": "cloudflare.com"
                },
                "timezone": {
                    "id": "America\/Los_Angeles",
                    "abbr": "PST",
                    "is_dst": false,
                    "offset": -28800,
                    "utc": "-08:00",
                    "current_time": "2026-02-01T09:07:47-08:00"
                }
            }
        },
        "ip_location": {
            "ip": "173.245.59.114",
            "country_code": "US",
            "country_name": "United States of America",
            "region_name": "California",
            "district": "City and County of San Francisco",
            "city_name": "San Francisco",
            "latitude": 37.77493,
            "longitude": -122.41942,
            "zip_code": "94107",
            "time_zone": "-08:00",
            "asn": "13335",
            "as": "CloudFlare Inc",
            "as_info": {
                "as_number": "13335",
                "as_name": "CloudFlare Inc",
                "as_domain": "cloudflare.com",
                "as_usage_type": "CDN",
                "as_cidr": "173.245.59.0\/24"
            },
            "isp": "CloudFlare Inc.",
            "domain": "cloudflare.com",
            "net_speed": "T1",
            "idd_code": "1",
            "area_code": "415",
            "weather_station_code": "USCA0987",
            "weather_station_name": "San Francisco",
            "mcc": "-",
            "mnc": "-",
            "mobile_brand": "-",
            "elevation": 14,
            "usage_type": "CDN",
            "address_type": "Anycast",
            "ads_category": "IAB19-11",
            "ads_category_name": "Data Centers",
            "continent": {
                "name": "North America",
                "code": "NA",
                "hemisphere": [
                    "north",
                    "west"
                ],
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "country": {
                "name": "United States of America",
                "alpha3_code": "USA",
                "numeric_code": 840,
                "demonym": "Americans",
                "flag": "https:\/\/cdn.ip2location.io\/assets\/img\/flags\/us.png",
                "capital": "Washington, D.C.",
                "total_area": 9826675,
                "population": 339665118,
                "currency": {
                    "code": "USD",
                    "name": "United States Dollar",
                    "symbol": "$"
                },
                "language": {
                    "code": "EN",
                    "name": "English"
                },
                "tld": "us",
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "region": {
                "name": "California",
                "code": "US-CA",
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "city": {
                "name": "San Francisco",
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "time_zone_info": {
                "olson": "America\/Los_Angeles",
                "current_time": "2026-02-01T09:07:47-08:00",
                "gmt_offset": -28800,
                "is_dst": false,
                "abbreviation": "PST",
                "dst_start_date": "2026-03-08",
                "dst_end_date": "2026-11-01",
                "sunrise": "07:11",
                "sunset": "17:34"
            },
            "geotargeting": {
                "metro": "807"
            },
            "is_proxy": false,
            "fraud_score": 3,
            "proxy": {
                "last_seen": 1,
                "proxy_type": "DCH",
                "threat": "-",
                "provider": "-",
                "is_vpn": false,
                "is_tor": false,
                "is_data_center": true,
                "is_public_proxy": false,
                "is_web_proxy": false,
                "is_web_crawler": false,
                "is_residential_proxy": false,
                "is_consumer_privacy_network": false,
                "is_enterprise_private_network": false,
                "is_spammer": false,
                "is_scanner": false,
                "is_botnet": false,
                "is_bogon": false
            }
        }
    }
}
```

---

# 💻 نمونه استفاده در Python

```py
import requests

domain = "tabairan.com"
url = f"https://abolfazlzarei.sbs/domain/?action=analyze&domain={domain}"

res = requests.get(url)
data = res.json()["data"]

print("🌐 Domain:", domain)
print("📡 IP:", data["dns_lookup"]["results"]["ip"])
print("🏢 Registrar:", data["domain_whois"]["registrar"]["name"])
print("☁️ ISP:", data["ip_whois"]["isp"])
print("📍 Country:", data["ip_whois"]["country"])
print("🛡 Fraud Score:", data["ip_location"]["fraud_score"])
```

---

# 🤖 نمونه استفاده در ربات‌ها (روبیکا)

```py
from rubpy import Client, filters
import requests

bot = Client(name="domain_analyzer_bot")

def analyze_domain(domain):
    url = f"https://abolfazlzarei.sbs/domain/?action=analyze&domain={domain}"
    try:
        res = requests.get(url, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.startswith("دامنه"):
        domain = text.replace("دامنه", "").strip()

        if not domain:
            return await message.reply("❗ لطفاً نام دامنه را وارد کنید.\nمثال:\nدامنه tabairan.com")

        data = analyze_domain(domain)
        if not data or "data" not in data:
            return await message.reply("❌ خطا در دریافت اطلاعات دامنه.")

        d = data["data"]

        output = (
            f"🌐 *آنالیز دامنه*\n\n"
            f"🔹 دامنه: `{domain}`\n"
            f"📡 IP: `{d['dns_lookup']['results']['ip']}`\n"
            f"🏢 Registrar: {d['domain_whois']['registrar']['name']}\n"
            f"📍 کشور: {d['ip_whois']['country']}\n"
            f"☁️ ISP: {d['ip_whois']['isp']}\n"
            f"🛡 Fraud Score: {d['ip_location']['fraud_score']}\n"
            f"⏳ عمر دامنه: {d['domain_whois']['domain_age']} روز"
        )

        await message.reply(output, parse_mode="markdown")

bot.run()
```

---

# 🎯 مزایای DomainAnalyzerAPI

⚡ سرعت بسیار بالا

❌ بدون API Key

🌍 آنالیز دقیق دامنه و IP

☁️ تشخیص Cloudflare و CDN

🛡 بررسی Proxy، VPN، TOR

📊 مناسب ربات‌ها و ابزارهای امنیتی


---

# 👤 Developer

Mir Sina Banihashem / Abolfazl Zarei

📡 Hosted on: Cloudflare / Linux Server

🔗 Endpoint: https://abolfazlzarei.sbs/domain

📢 Channel: @NingaCode / @Sinabani_api

🧑‍💻 Creator: @SBCS_IR

-‐-

---

# 🌐 DomainAnalyzerAPI — Version 1.0.0

**DomainAnalyzerAPI** is a fast, powerful, and completely free API designed for **full domain and IP analysis**.  
This service requires **no API Key** and provides detailed technical, network, and security-related information in a single JSON response.

It is ideal for use in **bots, security tools, monitoring systems, SEO tools, and network analysis platforms**.

---

## 🚀 Features

- 🔍 DNS Lookup & NameServer detection  
- 📄 Domain WHOIS information  
- 🌍 IP WHOIS & ownership data  
- ☁️ CDN & Cloudflare detection  
- 📡 ASN, ISP & network details  
- 🕒 Timezone & geolocation  
- 🛡 Proxy, VPN, TOR & Fraud detection  

---

## 🌐 API Endpoint

| Description | URL |
|------------|-----|
| Full domain analysis | https://abolfazlzarei.sbs/domain/?action=analyze&domain=example.com |

---

## 🔎 Query Parameters

| Parameter | Type | Required | Description |
|----------|------|----------|-------------|
| `action` | string | ✅ Yes | Must be set to `analyze` |
| `domain` | string | ✅ Yes | Target domain name (without http/https) |

### ✅ Example

```http
?action=analyze&domain=tabairan.com
```

---

## 📦 Response Overview

The API returns a JSON object with the following structure:

```json
{
  "creator": "string",
  "channel": "string",
  "data": {
    "dns_lookup": {},
    "domain_whois": {},
    "ip_whois": {},
    "ip_location": {}
  }
}
```

---

## 🔹 DNS Lookup

This section is responsible for checking the domain DNS status and extracting information related to NameServers and the main IP address of the domain.

### 📦 Response Structure

| Field | Type | Description |
|------|------|-------------|
| ok | boolean | Indicates whether the operation was successful |
| results.domain | string | Analyzed domain name |
| results.ip | string | Resolved IP address of the domain |
| results.dns | array | List of NameServers and related DNS records (NS / PTR) |

### 📌 Use Cases
- Detect CDN usage (e.g. Cloudflare)
- Inspect domain NameServers
- Retrieve the main IP address of a domain

---

## 🔹 Domain WHOIS

This section retrieves domain registration information from WHOIS databases, including ownership, registrar, and domain status details.

### 📦 Response Structure

| Field | Type | Description |
|------|------|-------------|
| domain | string | Domain name |
| domain_id | string | Unique domain identifier |
| status | string | ICANN domain status |
| create_date | string | Domain registration date |
| update_date | string | Last update date |
| expire_date | string | Domain expiration date |
| domain_age | number | Domain age (in days) |
| whois_server | string | WHOIS server |
| registrar | object | Registrar information |
| registrant | object | Domain owner information |
| admin | object | Administrative contact |
| tech | object | Technical contact |
| nameservers | array | Registered NameServers |

### 📌 Use Cases
- Verify domain legitimacy
- Detect newly registered domains
- Analyze domain ownership details

---

## 🔹 IP WHOIS

This section provides network-level and ownership information related to the domain’s IP address.

### 📦 Response Structure

| Field | Type | Description |
|------|------|-------------|
| ip | string | IP address |
| type | string | IPv4 or IPv6 |
| continent | string | Continent |
| country | string | Country |
| region | string | Region / State |
| city | string | City |
| latitude | number | Latitude |
| longitude | number | Longitude |
| isp | string | Internet Service Provider |
| org | string | Organization owning the IP |
| asn | number | Autonomous System Number |
| timezone | object | Timezone information |
| flag | object | Country flag details |

### 📌 Use Cases
- Identify server location
- Distinguish data centers from ISPs
- Analyze IP ownership

---

## 🔹 IP Location & Security

This section delivers advanced geolocation and security-related information about the IP address.

### 📦 Response Structure

| Field | Type | Description |
|------|------|-------------|
| usage_type | string | Usage type (CDN / Hosting / Residential) |
| address_type | string | Anycast or Unicast |
| is_proxy | boolean | Proxy detection status |
| is_vpn | boolean | VPN detection status |
| is_tor | boolean | TOR network detection |
| is_data_center | boolean | Indicates data center IP |
| fraud_score | number | Risk score (0 = low risk, 100 = high risk) |
| net_speed | string | Network speed category |
| ads_category | string | Advertising category |
| time_zone_info | object | Local time and timezone data |

### 📌 Use Cases
- Improve bot and website security
- Detect suspicious or abusive IPs
- Prevent fraud and automated attacks

---

# 🧪 Sample Request

```http
GET https://abolfazlzarei.sbs/domain/?action=analyze&domain=tabairan.com
```

---

🧾 Sample Response

```json
{
    "creator": "@SBCS_IR",
    "channel": "@NingaCode",
    "data": {
        "dns_lookup": {
            "ok": true,
            "results": {
                "domain": "tabairan.com",
                "ip": "173.245.59.114",
                "dns": [
                    "gabe.ns.cloudflare.com",
                    "dns.cloudflare.com",
                    "gabe.ns.cloudflare.com",
                    "ptr.atlas.tbns.ir"
                ]
            }
        },
        "domain_whois": {
            "domain": "tabairan.com",
            "domain_id": "2092063745_DOMAIN_COM-VRSN",
            "status": "http:\/\/www.icann.org\/epp#clientTransferProhibited",
            "create_date": "2017-01-22T04:55:23Z",
            "update_date": "2025-01-16T06:58:29Z",
            "expire_date": "2027-01-22T07:55:23Z",
            "domain_age": 3297,
            "whois_server": "whois.apiname.com",
            "registrar": {
                "iana_id": "1601",
                "name": "Atak Domain",
                "url": "http:\/\/apiname.com"
            },
            "registrant": {
                "name": "Privacy Protect",
                "organization": "n\/a",
                "street_address": "10, Smriti Chowk,",
                "city": "Dehra Dun",
                "region": "Tripura",
                "zip_code": "457490",
                "country": "IN",
                "phone": "+91.828195652",
                "fax": "+91.00",
                "email": "domain@privacyprotect.biz"
            },
            "admin": {
                "name": "Privacy Protect",
                "organization": "n\/a",
                "street_address": "10, Smriti Chowk,",
                "city": "Dehra Dun",
                "region": "Tripura",
                "zip_code": "457490",
                "country": "IN",
                "phone": "+91.828195652",
                "fax": "+91.00",
                "email": "domain@privacyprotect.biz"
            },
            "tech": {
                "name": "Privacy Protect",
                "organization": "n\/a",
                "street_address": "10, Smriti Chowk,",
                "city": "Dehra Dun",
                "region": "Tripura",
                "zip_code": "457490",
                "country": "IN",
                "phone": "+91.828195652",
                "fax": "+91.00",
                "email": "domain@privacyprotect.biz"
            },
            "billing": {
                "name": "",
                "organization": "",
                "street_address": "",
                "city": "",
                "region": "",
                "zip_code": "",
                "country": "",
                "phone": "",
                "fax": "",
                "email": ""
            },
            "nameservers": [
                "no name server"
            ]
        },
        "ip_whois": {
            "ok": true,
            "result": {
                "ip": "173.245.59.114",
                "type": "IPv4",
                "continent": "North America",
                "continent_code": "NA",
                "country": "United States",
                "country_code": "US",
                "region": "California",
                "region_code": "CA",
                "city": "San Francisco",
                "latitude": 37.718128,
                "longitude": -122.4343849,
                "is_eu": false,
                "postal": "94102",
                "calling_code": "1",
                "capital": "Washington D.C.",
                "borders": "CA,MX",
                "flag": {
                    "img": "https:\/\/cdn.ipwhois.io\/flags\/us.svg",
                    "emoji": "🇺🇸",
                    "emoji_unicode": "U+1F1FA U+1F1F8"
                },
                "connection": {
                    "asn": 13335,
                    "org": "Cloudflare, Inc.",
                    "isp": "Cloudflare, Inc.",
                    "domain": "cloudflare.com"
                },
                "timezone": {
                    "id": "America\/Los_Angeles",
                    "abbr": "PST",
                    "is_dst": false,
                    "offset": -28800,
                    "utc": "-08:00",
                    "current_time": "2026-02-01T09:07:47-08:00"
                }
            }
        },
        "ip_location": {
            "ip": "173.245.59.114",
            "country_code": "US",
            "country_name": "United States of America",
            "region_name": "California",
            "district": "City and County of San Francisco",
            "city_name": "San Francisco",
            "latitude": 37.77493,
            "longitude": -122.41942,
            "zip_code": "94107",
            "time_zone": "-08:00",
            "asn": "13335",
            "as": "CloudFlare Inc",
            "as_info": {
                "as_number": "13335",
                "as_name": "CloudFlare Inc",
                "as_domain": "cloudflare.com",
                "as_usage_type": "CDN",
                "as_cidr": "173.245.59.0\/24"
            },
            "isp": "CloudFlare Inc.",
            "domain": "cloudflare.com",
            "net_speed": "T1",
            "idd_code": "1",
            "area_code": "415",
            "weather_station_code": "USCA0987",
            "weather_station_name": "San Francisco",
            "mcc": "-",
            "mnc": "-",
            "mobile_brand": "-",
            "elevation": 14,
            "usage_type": "CDN",
            "address_type": "Anycast",
            "ads_category": "IAB19-11",
            "ads_category_name": "Data Centers",
            "continent": {
                "name": "North America",
                "code": "NA",
                "hemisphere": [
                    "north",
                    "west"
                ],
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "country": {
                "name": "United States of America",
                "alpha3_code": "USA",
                "numeric_code": 840,
                "demonym": "Americans",
                "flag": "https:\/\/cdn.ip2location.io\/assets\/img\/flags\/us.png",
                "capital": "Washington, D.C.",
                "total_area": 9826675,
                "population": 339665118,
                "currency": {
                    "code": "USD",
                    "name": "United States Dollar",
                    "symbol": "$"
                },
                "language": {
                    "code": "EN",
                    "name": "English"
                },
                "tld": "us",
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "region": {
                "name": "California",
                "code": "US-CA",
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "city": {
                "name": "San Francisco",
                "translation": {
                    "lang": null,
                    "value": null
                }
            },
            "time_zone_info": {
                "olson": "America\/Los_Angeles",
                "current_time": "2026-02-01T09:07:47-08:00",
                "gmt_offset": -28800,
                "is_dst": false,
                "abbreviation": "PST",
                "dst_start_date": "2026-03-08",
                "dst_end_date": "2026-11-01",
                "sunrise": "07:11",
                "sunset": "17:34"
            },
            "geotargeting": {
                "metro": "807"
            },
            "is_proxy": false,
            "fraud_score": 3,
            "proxy": {
                "last_seen": 1,
                "proxy_type": "DCH",
                "threat": "-",
                "provider": "-",
                "is_vpn": false,
                "is_tor": false,
                "is_data_center": true,
                "is_public_proxy": false,
                "is_web_proxy": false,
                "is_web_crawler": false,
                "is_residential_proxy": false,
                "is_consumer_privacy_network": false,
                "is_enterprise_private_network": false,
                "is_spammer": false,
                "is_scanner": false,
                "is_botnet": false,
                "is_bogon": false
            }
        }
    }
}
```

---

# 💻 Python Example

```py
import requests

domain = "tabairan.com"
url = f"https://abolfazlzarei.sbs/domain/?action=analyze&domain={domain}"

res = requests.get(url)
data = res.json()["data"]

print("Domain:", domain)
print("IP:", data["dns_lookup"]["results"]["ip"])
print("Registrar:", data["domain_whois"]["registrar"]["name"])
print("ISP:", data["ip_whois"]["isp"])
print("Fraud Score:", data["ip_location"]["fraud_score"])
```

---

# 🎯 Why DomainAnalyzerAPI?

⚡ Fast and lightweight

❌ No API Key required

🌍 Accurate domain & IP analysis

☁️ CDN and Cloudflare detection

🛡 Proxy, VPN, TOR & fraud checks

🤖 Perfect for bots and automation



---

# 👤 Developer

Mir Sina Banihashem / Abolfazl Zarei
📡 Hosted on: Cloudflare / Linux Server
🔗 Endpoint: https://abolfazlzarei.sbs/domain/
📢 Channel: @NingaCode / @Sinabani_api
🧑‍💻 Creator: @SBCS_IR
