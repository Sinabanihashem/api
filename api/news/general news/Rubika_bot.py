from rubpy import Client, filters
import requests

bot = Client(name="sina_news_bot")

API_URL = "https://news.api-sina-free.workers.dev/news"

def get_news():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "اخبار":
        data = get_news()
        if not data:
            return await message.reply("❌ خطا در دریافت اخبار")

        news_list = data.get("news", [])
        if not news_list:
            return await message.reply("📭 خبری یافت نشد.")

        result = "📰 *آخرین اخبار روز:*\n\n"
        for item in news_list:
            result += f"🔸 {item['title']}\n🔗 {item['link']}\n\n"

        await message.reply(result[:4000], parse_mode="markdown")

bot.run()
