import random
import asyncio

from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import ADS_MODE, LOGGER_ID
from AnonXMusic import app
from AnonXMusic.utils.database import get_served_chats


ad = """
๏ ᴛʜɪs ɪs <a href=https://t.me/JerryTwoBot> ˹ᴊᴇʀʀʏ ᴛᴡᴏ ʙᴏᴛ˼ </a>

➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs. 

 Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.
"""
butt = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/LeviXMusicBot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def keep_running():
    if ADS_MODE:
        try:
            chats = []
            schats = await get_served_chats()
            for chat in schats:
                chats.append(int(chat["chat_id"]))
            random.shuffle(chats)
            for x in chats:
                if x == LOGGER_ID:
                    continue
                if x == -1001686672798:
                    continue
                try:
                    sent = await app.send_photo(
                        chat_id=x,
                        photo="https://graph.org/file/053681272a7bfc013963a.jpg",
                        caption=ad,
                        reply_markup=butt,
                    )

                except FloodWait as fw:
                    flood_time = int(fw.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue
        except:
            pass


scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(keep_running, trigger="cron", hour=10, minute=59)
scheduler.start()
