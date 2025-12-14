from rubpy import Client, filters
import requests

bot = Client(name="sina_sports_news_bot")

API_URL = "https://sports.api-sina-free.workers.dev/sports"

def get_sports_news():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "اخبار ورزشی":
        data = get_sports_news()
        if not data:
            return await message.reply("❌ خطا در دریافت اخبار ورزشی")

        news_list = data.get("data", [])
        if not news_list:
            return await message.reply("📭 خبری یافت نشد.")

        result = "⚽ *آخرین اخبار ورزشی:*\n\n"
        for item in news_list:
            result += f"🔸 {item['title']}\n"
            if item.get("sub_title"):
                result += f"▫️ {item['sub_title']}\n"
            if item["media"].get("video"):
                result += f"🎥 ویدیو: {item['media']['video']}\n"
            result += "\n"

        await message.reply(result[:4000], parse_mode="markdown")

bot.run()
