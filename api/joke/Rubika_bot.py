from rubpy import Client, filters
import requests

bot = Client(name="sina_joke_bot")

JOK_URL = "https://jok.api-sina-free.workers.dev/jok"
FAN_URL = "https://jok.api-sina-free.workers.dev/fantezi"

def fetch(url):
    try:
        return requests.get(url, timeout=5).json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "جوک":
        data = fetch(JOK_URL)
        if not data:
            return await message.reply("❌ خطا در دریافت جوک")
        await message.reply(f"😂 {data['result']}")

    elif text == "جوک فانتزی":
        data = fetch(FAN_URL)
        if not data:
            return await message.reply("❌ خطا در دریافت جوک فانتزی")
        await message.reply(f"🎭 {data['result']}")

bot.run()
