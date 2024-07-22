from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from AnonXMusic import app
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.core.userbot import assistants
from AnonXMusic.utils.database import get_active_chats


@app.on_message(
    filters.command("respondtostatuschecker") & filters.private & ~BANNED_USERS
)
async def respond(_, message: Message):
    get = await bot_sys_stats()
    assnum = ""
    for x in assistants:
        assnum += "✨ "
    active_vc = len(await get_active_chats())
    await message.reply_text(f"{get[0]}~{get[1]}~{active_vc}~{assnum}")
