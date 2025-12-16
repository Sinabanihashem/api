from rubpy import Client, filters
import requests

bot = Client(name="sina_story_bot")

API_URL = "https://dastan.api-sina-free.workers.dev"

def get_story():
    try:
        res = requests.get(API_URL, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "داستان":
        data = get_story()
        if not data or not data.get("status"):
            return await message.reply("❌ خطا در دریافت داستان")

        await message.reply(
            f"📖 *داستان رندوم:*\n\n{data['result']}",
            parse_mode="markdown"
        )

bot.run()
