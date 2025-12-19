from rubpy import Client, filters
import requests

bot = Client(name="crypto_price_bot")
API = "https://currency.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip().lower()

    if not text.startswith("قیمت"):
        return

    symbol = text.replace("قیمت", "", 1).strip()
    if not symbol:
        return await message.reply("❗️ مثال صحیح:\nقیمت btc")

    try:
        res = requests.get(API, params={"crypto": symbol}, timeout=10)

        if res.status_code != 200:
            return await message.reply("❌ خطا در ارتباط با سرور")

        data = res.json()

        # بررسی فعال بودن سرویس
        if data.get("activ") != 1:
            return await message.reply("⚠️ سرویس موقتاً غیرفعال است")

        if not data.get("list"):
            return await message.reply("❌ ارز موردنظر پیدا نشد")

        coin = data["list"][0]

        # استفاده از تمام فیلدهای مهم خروجی
        text_reply = (
            f"🪙 *{coin['name']} ({coin['iso']})*\n\n"
            f"🏆 رتبه بازار: {coin['rank']}\n"
            f"💲 قیمت دلاری: `{coin['price_string_format']}$`\n"
            f"💰 قیمت ریالی: `{coin['price_rial']:,}` ریال\n"
            f"🟢 قیمت خرید: `{coin['price_buy']:,}`\n"
            f"🔴 قیمت فروش: `{coin['price_sell']:,}`\n"
            f"📊 ارزش بازار: `{coin['market_cap']}`\n"
            f"📉 تغییر ۲۴ساعت: `{coin['daily_change_percent']}%`\n"
            f"🪙 معادل بیت‌کوین: `{coin['price_bitcoin']}`\n\n"
            f"🕒 زمان بروزرسانی:\n`{data['time']}`\n\n"
            f"🖼 [مشاهده لوگو]({coin['logo']})\n\n"
            f"📡 {data['channel']}\n"
            f"👤 {data['creator']}"
        )

        await message.reply(text_reply, parse_mode="markdown")

    except Exception as e:
        await message.reply(f"❌ خطای غیرمنتظره:\n{e}")

bot.run()
