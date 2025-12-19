from rubpy import Client, filters
import requests

bot = Client(name="sina_photo_text_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.startswith("عکس "):
        content = text.replace("عکس ", "").strip()
        if not content:
            return await message.reply("❗ لطفاً یک متن وارد کنید")

        image_url = f"https://photo-text.api-sina-free.workers.dev/{content}"
        await message.reply_photo(image_url, caption="🖼 تصویر ساخته شد")

bot.run()
