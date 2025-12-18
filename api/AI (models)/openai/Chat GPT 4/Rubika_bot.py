from rubpy import Client, filters
import requests

bot = Client(name="sina_gpt4_bot")

API_URL = "https://gpt4.api-sina-free.workers.dev/gpt4"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not text.startswith("هوش"):
        return

    query = text.replace("هوش", "", 1).strip()
    if not query:
        return await message.reply("❗️ لطفاً یک متن وارد کنید.")

    try:
        res = requests.get(f"{API_URL}?text={query}", timeout=15)
        data = res.json()

        if "result" in data:
            await message.reply(f"🤖 *پاسخ GPT-4:*\n\n{data['result']}", parse_mode="markdown")
        else:
            await message.reply("⚠️ خطا در دریافت پاسخ.")
    except Exception as e:
        await message.reply(f"❌ خطای ارتباط با سرور:\n{e}")

bot.run()
