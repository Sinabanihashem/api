from rubpy import Client, filters
import requests

bot = Client(name="sina_gold_pro")

API_URL = "https://gold.api-sina-free.workers.dev/gold"

def get_gold_data():
    try:
        res = requests.get(API_URL, timeout=5)
        return res.json()
    except:
        return None

def format_number(n):
    return f"{n:,}"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text in ["/help", "منو"]:
        return await message.reply(
            "💰 `قیمت طلا` → نمایش نرخ‌های اصلی\n"
            "📦 `جزئیات` → نمایش تمام نرخ‌ها + حباب‌ها\n"
            "🔄 `آپدیت` → بررسی آخرین زمان بروز رسانی\n"
            "ℹ️ `منبع` → نمایش منبع نرخ‌ها\n"
            , parse_mode="markdown"
        )

    elif text == "قیمت طلا":
        data = get_gold_data()
        if not data:
            return await message.reply("❗ خطا در دریافت اطلاعات.")
        
        await message.reply(
            f"💰 *قیمت لحظه‌ای طلا و سکه:*\n\n"
            f"🥇 طلای ۱۸ عیار: {format_number(data['gold_18_ayar'])} ریال\n"
            f"🏅 سکه امامی: {format_number(data['sekke_emami'])} ریال\n"
            f"🌓 نیم سکه: {format_number(data['nim_sekke'])} ریال\n"
            f"🌗 ربع سکه: {format_number(data['rob_sekke'])} ریال\n"
            f"\n⏱ بروزرسانی: {data['updated_at']}"
            , parse_mode="markdown"
        )

    elif text == "جزئیات":
        data = get_gold_data()
        if not data:
            return await message.reply("❗ خطا در دریافت اطلاعات.")

        await message.reply(
            f"📦 *جزئیات کامل قیمت‌ها:*\n\n"
            f"🥇 طلای ۱۸ عیار: {format_number(data['gold_18_ayar'])} ریال\n"
            f"🥇 طلای ۲۴ عیار: {format_number(data['gold_24_ayar'])} ریال\n"
            f"🟡 طلای دست دوم: {format_number(data['gold_second_hand'])} ریال\n"
            f"⚖️ مثقال طلا: {format_number(data['mesghal_tala'])} ریال\n"
            f"🔥 آبشده نقدی: {format_number(data['abshode_naghd'])} ریال\n"
            f"💹 آبشده معاملاتی: {format_number(data['abshode_moamelati'])} ریال\n\n"

            f"🏅 *قیمت انواع سکه:*\n"
            f"سکه امامی: {format_number(data['sekke_emami'])} ریال\n"
            f"سکه بهار آزادی: {format_number(data['sekke_bahar_azadi'])} ریال\n"
            f"نیم سکه: {format_number(data['nim_sekke'])} ریال\n"
            f"ربع سکه: {format_number(data['rob_sekke'])} ریال\n"
            f"سکه گرمی: {format_number(data['sekke_gerami'])} ریال\n\n"

            f"🎯 *حباب سکه‌ها:*\n"
            f"حباب امامی: {format_number(data['habab_emami'])} ریال\n"
            f"حباب بهار آزادی: {format_number(data['habab_bahar'])} ریال\n"
            f"حباب نیم سکه: {format_number(data['habab_nim'])} ریال\n"
            f"حباب ربع سکه: {format_number(data['habab_rob'])} ریال\n"
            f"حباب سکه گرمی: {format_number(data['habab_gerami'])} ریال\n\n"

            f"⏱ بروزرسانی: {data['updated_at']}\n"
            f"🔗 منبع: {data['source']}"
            , parse_mode="markdown"
        )

    elif text == "آپدیت":
        data = get_gold_data()
        if not data:
            return await message.reply("⛔ خطا در اتصال به سرور.")
        await message.reply(f"🔄 آخرین بروزرسانی: {data['updated_at']}")

    elif text == "منبع":
        data = get_gold_data()
        if not data:
            return await message.reply("⛔ اتصال برقرار نشد.")
        await message.reply(f"📌 منبع نرخ‌ها: {data['source']}")

bot.run()
