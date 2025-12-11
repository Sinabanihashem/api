from rubpy import Client, filters
import requests

bot = Client(name="sina_car_bot")
API_URL = "https://car.api-sina-free.workers.dev/cars?type=all"

def get_cars():
    try:
        res = requests.get(API_URL, timeout=5)
        return res.json().get("cars", [])
    except:
        return []

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "قیمت خودرو":
        cars = get_cars()
        if not cars:
            return await message.reply("❗ خطا در دریافت اطلاعات.")

        output = "🚗 *قیمت لحظه‌ای خودروها:*\n\n"
        for c in cars[:10]:
            output += (
                f"🏷 *{c['name']}*\n"
                f"• برند: {c['brand']}\n"
                f"• بازار: {c['market_price']}\n"
                f"• تغییر: {c['change_percent']} ({c['change_value']})\n"
                f"• بروزرسانی: {c['last_update']}\n\n"
            )

        await message.reply(output, parse_mode="markdown")

bot.run()
