from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from EmikoRobot import pbot
from EmikoRobot.utils.errors import capture_err
from EmikoRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/98d3f13f27f77695b925e.jpg",
        caption=f"""✨ **Hey I'm Flicks Robot** 

**╭┈╾────────────── ·﻿ ﻿ ﻿· ﻿ ·﻿ ﻿ ﻿· ﻿✦**
**┊┊    ⟨ 😶‍🌫 INFORMATION BOT 😶‍🌫 ⟩**
**┊┊╾────────────── ·﻿ ﻿ ﻿· ﻿ ·﻿ ﻿ ﻿· ﻿✦**
**┊┊╾───────────••───────╮
**┊┊👨🏻‍💻 Owner : [Skyzo](t.me/XFLSkyzo)**
**┊┊🗃️ Ver Pyrogram :** `{z}`
**┊┊📚 Features  : Music, Manager**
**┊┊🐉 Ver Python :** `{y()}`
**╰┈╾──────••────────────╯**

**Click Button Here For More Information.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Github", url="https://github.com/ridho17-ind"), 
                    InlineKeyboardButton(
                        "Support", url="https://t.me/flicksrobotsupport")
                ]
            ]
        ),
        disable_web_page_preview=True
    )
