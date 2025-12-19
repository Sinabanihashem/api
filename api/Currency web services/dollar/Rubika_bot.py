from rubpy import Client, filters
import requests
from datetime import datetime

bot = Client(name="sina_dollar_bot")

API_URL = "https://dollar.api-sina-free.workers.dev/dollar"

@bot.on_message_updates(filters.text)
async def main(message):
    text = message.text.strip()

    if text in ["دلار", "Dollar", "dollar", "د‌لار"]:
        try:
            response = requests.get(API_URL, timeout=5)
            response.raise_for_status()
            data = response.json()

            if "price_toman" not in data:
                await message.reply("خطا در دریافت اطلاعات")
                return

            price_toman = data["price_toman"]
            price_rial = data["price_rial"]
            updated_at = data["updated_at"]
            creator = data.get("creator", "@Sinabani_api")
            source = data.get("source", "tgju.org")

            time_str = datetime.fromisoformat(updated_at.replace("Z", "+00:00")).strftime("%Y/%m/%d - %H:%M:%S")

            reply_text = (
                f"💸 قیمت لحظه‌ای دلار آزاد 🇮🇷\n"
                f"💰 به تومان: {price_toman:,} تومان\n"
                f"💵 به ریال: {int(price_rial):,} ریال\n"
                f"⏰ بروزرسانی: {time_str}\n"
                f"🌐 منبع: {source}\n"
                f"👤 توسعه‌دهنده: {creator}"
            )

            await message.reply(reply_text)

        except requests.exceptions.Timeout:
            await message.reply(" سرور پاسخ نمی‌دهد، لطفاً دوباره تلاش کنید.")
        except requests.exceptions.ConnectionError:
            await message.reply(" اتصال اینترنت برقرار نیست.")
        except Exception as e:
            await message.reply(f" خطا\n{e}")

bot.run()
