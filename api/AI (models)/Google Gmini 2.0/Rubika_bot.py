from rubpy import Client, filters
import requests

bot = Client(name="sina_gemini_bot")
API_URL = "https://gemini.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not text.startswith("جمنای"):
        return

    query = text.replace("جمنای", "", 1).strip()
    if not query:
        return await message.reply("❗️ لطفاً یک متن وارد کنید.")

    try:
        res = requests.get(f"{API_URL}?text={query}", timeout=15)
        data = res.json()

        if "answer" in data:
            await message.reply(
                f"🤖 *پاسخ Gemini:*\n\n{data['answer']}",
                parse_mode="markdown"
            )
        else:
            await message.reply("⚠️ پاسخی دریافت نشد.")
    except Exception as e:
        await message.reply(f"❌ خطای ارتباط با سرور:\n{e}")

bot.run()
