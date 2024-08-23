import random
import asyncio

from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import ADS_MODE, LOGGER_ID
from AnonXMusic import app
from AnonXMusic.utils.database import get_served_chats


ad = """
๏ Pᴀɪᴅ Pʀᴏᴍᴏᴛɪᴏɴ ᴀᴠᴀɪʟᴀʙʟᴇ ᴠɪᴀ ᴍᴜsɪᴄ ʙᴏᴛs

➻ Pʀᴏᴍᴏᴛᴇ ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘs, ᴄᴏʟᴏᴜʀ ᴛʀᴀᴅɪɴɢ ɢᴀᴍᴇs, ᴄʜᴀɴɴᴇʟs, ʙᴇᴛᴛɪɴɢ ᴀᴅs ᴏʀ ᴀɴʏᴛʜɪɴɢ. 
๏ ᴅᴀɪʟʏ , ᴡᴇᴇᴋʟʏ , ᴍᴏɴᴛʜʟʏ ᴘʟᴀɴs ᴀᴠᴀɪʟᴀʙʟᴇ. 

➻ ғᴏʀ Pʀᴏᴍᴏᴛɪᴏɴ ᴄᴏɴᴛᴀᴄᴛ - @JerryOwner
"""
butt = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="๏ ᴍᴏʀᴇ ɪɴꜰᴏ? ᴛᴀᴘ ʜᴇʀᴇ ๏", url="https://t.me/JerryUpdates")
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
                        photo="https://graph.org/file/e6804ba93926b1ed20a5e.jpg",
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
scheduler.add_job(keep_running, trigger="cron", hour=13, minute=30)
scheduler.start()
