#Copyright ©️ 2021 xsvshacker. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [DATE_TIME Telegram userbot by xsvshacker] (https://github.com/Randi356/DATE_TIME_USERBOT-mod)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/Randi356/DATE_TIME_USERBOT-mod/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from lists_mod.quotes_mod import *
from lists_mod.emojis_mod import *
from lists_mod.image_mod import *
from lists_mod.image import *
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz
import asyncio
import random
import os

Date_Time_Userbot_mod=Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)

Time_Zone = os.environ["TIME_ZONE"]

async def main_mod():
    try:
        while True:
            if Date_Time_Userbot_mod.is_connected:
                Quotes_mod = random.choice(quotes_mod)
                Emojis_mod = random.choice(emojis_mod)
                Image_mod = random.choice(image_mod)
                TimeZone_mod = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))
                Time_mod = TimeZone_mod.strftime("%I:%M %p")
                Date_mod = TimeZone_mod.strftime("%b %d") 
                Image_mod = Image.open("image.jpg")
                Image_mod = Image.open("rendy.jpg")
                Image_font_mod = ImageFont.truetype("ds-digit.ttf", 360)
                Image_text_mod = f"{Time_mod}"
                Image_edit_mod = ImageDraw.Draw(Image_mod)
                Image_edit_mod.text((690, 550), Image_text_mod, (0, 255, 255), font = Image_font_mod)
                Image_mod.save("Image_final_mod.jpg")
                Image_mod.save("rendy_mod.jpg")
                Image_mod.save("{Image_mod}")
                await Date_Time_Userbot_mod.update_profile(bio = f"{Emojis_mod} {Quotes_mod}" , last_name = f"| ⏰ {Time_mod} | 📅 {Date_mod}")
                await Date_Time_Userbot_mod.set_profile_photo(photo="Image_final_mod.jpg")
                await Date.Time_Userbot_mod.set_profile_photo(photo="{Image_mod}")
                me = await Date_Time_Userbot_mod.get_me()
                photos = await Date_Time_Userbot_mod.get_profile_photos("me")
                try:
                    await Date_Time_Userbot_mod.delete_profile_photos(photos[1].file_id)
                except Exception:
                    pass        
                print("Profile Updated!")
            await asyncio.sleep(60)     
    except FloodWait as e:
        await asyncio.sleep(e.x)         

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_mod())
Date_Time_Userbot_mod.run()

#Copyright ©️ 2021 xsvshacker. All Rights Reserved
