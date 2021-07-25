from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import filters


HOME_TEXT = "💖 **Hi [{}](tg://user?id={})**,\n\nI'm **PÎSTÂ MÚSÎC ẞø†** \nI Can Play Music In Channels & Groups 24x7 Nonstop!\n\n**😉 Happy Streaming 😉**\n\n**Type `/help` To Get Help Menu**\n\n**Currently I am under a private vc music player ⏩**\n\n** To add me take permission from [Owner](https://t.me/backup_pista123)**"
HELP = """•The commands I currently support are:
⚜️ /play - __Plays the replied audio file or YouTube video through link.__
⚜️ /pause - __Pause Voice Chat Music.__
⚜️ /resume - __Resume Voice Chat Music.__
⚜️ /skip - __Skips the current Music Playing In Voice Chat.__
⚜️ /stop - __Clears The Queue as well as ends Voice Chat Music.__
⚜️ /song (song name) - __To search song and send song directly.__
⚜️ /yt (song name) - To search song from youtube and play directly 
⚜️ /help - __Shows the help Menu
"""

@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('💫 OWNER', url='https://t.me/PISTA_XD'),
        InlineKeyboardButton('🏘️ Group', url='https://t.me/RIDERIANS'),
    ],
    [
        InlineKeyboardButton('⚙️ Another Music Bot ⚙️', url='https://t.me/music_robo2_bot'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)

@Client.on_message(filters.command("play"))
async def start(_, message: Message):
    await message.reply_text(
        f"""This Command Can Only Be Used In Group Or Channel"""

