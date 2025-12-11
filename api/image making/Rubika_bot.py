from rubpy import Client, filters
import requests

bot = Client(name="sina_image_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    txt = message.text.strip()

    if txt.startswith("عکس "):
        prompt = txt.replace("عکس ", "")
        link = f"https://image.api-sina-free.workers.dev/generate?text={prompt}"

        img = requests.get(link).content
        await message.reply_photo(photo=img)

bot.run()
