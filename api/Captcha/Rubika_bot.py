from rubpy import Client, filters
import requests
import tempfile
import os
import base64

bot = Client(name="sina")
captcha_data = {}

@bot.on_message_updates(filters.text)
async def main(message):
    text = message.text.strip()
    user_id = getattr(message, "user_guid", None)
    if not user_id:
        return

    if text.lower() == "کپچا":
        res = requests.get("https://captcha.api-sina-free.workers.dev/captcha")
        data = res.json()
        image_data = base64.b64decode(data["captcha_base64"].split(",")[1])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp.write(image_data)
            tmp_path = tmp.name
        captcha_data[user_id] = data["captcha_id"]
        await message.reply_photo(photo=tmp_path, caption="کپچا شما آماده است!\nبرای بررسی، بنویس:\nبررسی <کد>")
        os.remove(tmp_path)
        return

    if text.lower().startswith("بررسی "):
        if user_id not in captcha_data:
            await message.reply("اول با دستور «کپچا» یک تصویر جدید بگیر.")
            return
        code = text.split()[1]
        captcha_id = captcha_data[user_id]
        res = requests.get(f"https://captcha.api-sina-free.workers.dev/captcha/verify?captcha_id={captcha_id}&user_input={code}")
        data = res.json()
        await message.reply(data["message"])
        del captcha_data[user_id]

bot.run()
