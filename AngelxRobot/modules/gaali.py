import random
import asyncio
from pyrogram import filters
from AngelxRobot import pbot as FallenRobot

COMRADE_STRINGS = [
    "https://t.me/team_comradex...",
    "https://t.me/kadalora_kadalai...",
    "https://t.me/comrade_robotz…!...",
    "https://t.me/comrade_botz ...",
    "https://t.me/comrade_network …...",
    "https://t.me/about_bobby…",
    "https://t.me/love_u_bobby...",
    "https://t.me/bobby_x_world...",
    "https://t.me/bobby_x_factory...",
    "https://t.me/Ulla_vanthu_uruttu...",
    "https://t.me/SiVaMaYaMm...",
    "https://t.me/comrade_robotz...",
]


@AngelxRobot.on_message(filters.command("gaali"))
async def lel(bot, message):
    ran = random.choice(GAALI_STRINGS)
    await bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)


__mod_name__ = "Cᴏᴍʀᴀᴅᴇ😈"

__help__ = """

ᴍᴀᴋᴇs ᴀ GAALI ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.

❍ /comrade *:* ᴍᴀᴋᴇs GAALI ɪғ ʏᴏᴜ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ

 """
