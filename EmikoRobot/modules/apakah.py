import random
from EmikoRobot.events import register
from EmikoRobot import telethn

APAKAH_STRING = ["Iya 😅", 
                 "Tidak 🤦🏻", 
                 "Mungkin 🗿", 
                 "Mungkin Tidak 🤭", 
                 "Bisa Jadi 🤣", 
                 "Mungkin Iya 🤔",
                 "Tidak Mungkin 😏",
                 "YNTKTS 😐",
                 "Pala Bapak Kau Pecah Anj 😡",
                 "Apa iya? 😒",
                 "Tanya Aja Sama Mamak Kau Tuh Puki 😑"
                 "Betul 😁",
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan Saya Pertanyaan Tolol 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
