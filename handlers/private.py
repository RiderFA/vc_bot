from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import filters


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
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
•I Can Play Music In Channels & Groups 24x7 Nonstop!
•Currently I am under a private vc music player ⏩
•To add me take permission from [Owner](https://t.me/Pista_Xd)
•Type `/help` To Get List Of Command That I Support 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/Riderians"
                    ),
                    InlineKeyboardButton(
                        "⚙ HELP ⚙", callback_data="HELP"
                    ),
                    InlineKeyboardButton(
                        "Owner 👑", url="https://t.me/backup_Pista123"
                    )
                ]
            ]
        )
    )
@Client.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text(HELP)

@Client.on_message(filters.command("play"))
async def play(_, message: Message):
    await message.reply_text(
        f"""This Command Can Only Be Used In Group Or Channel """)

from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os

# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command(['song']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply(f"**🔎 Searching For** `{query}`")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[PÎSTÂ MÚSÎC ẞø†]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**Found Literary Noting. Please Try Another Song or Use Correct Spelling!**')
            return
    except Exception as e:
        m.edit(
            "**Enter Song Name with Command!**"
        )
        print(str(e))
        return
    m.edit(f"🔥 **Uploading Song**  `{query}` !")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🏷 <b>Title:</b> <a href="{link}">{title}</a>\n⏳ <b>Duration:</b> <code>{duration}</code>\n👀 <b>Views:</b> <code>{views}</code>\n'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
        message.delete()
    except Exception as e:
        m.edit('**An Error Occured. Please Report This To [PISTA OP](https://t.me/PISTA_XD) !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
