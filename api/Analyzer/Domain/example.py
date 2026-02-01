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
