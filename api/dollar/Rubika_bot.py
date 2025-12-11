from rubpy import Client, filters
import requests
from datetime import datetime

bot = Client(name="sina_dollar_bot")
API_URL = "https://dollar.api-sina-free.workers.dev/dollar"

@bot.on_message_updates(filters.text)
async def main(message):
    if message.text.strip() in ["دلار", "dollar", "Dollar"]:
        try:
            data = requests.get(API_URL, timeout=5).json()

            price_toman = data["price_toman"]
            price_rial = data["price_rial"]
            updated_at = data["updated_at"]
            source = data.get("source", "tgju.org")

            time_str = datetime.fromisoformat(updated_at.replace("Z", "+00:00")).strftime("%Y/%m/%d - %H:%M:%S")

            await message.reply(
                f"💸 قیمت لحظه‌ای دلار آزاد:\n\n"
                f"💰 تومان: {price_toman:,}\n"
                f"💵 ریال: {int(price_rial):,}\n\n"
                f"⏱ بروزرسانی: {time_str}\n"
                f"🌐 منبع: {source}"
            )

        except:
            await message.reply("⚠️ خطا در دریافت اطلاعات.")

bot.run()
