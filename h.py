import os
import re
from transition import Translation
import time
import cloudscraper
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os import environ

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import aiohttp
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram.errors import UserNotParticipant, UserBannedInChannel 

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
CRYPT = 'ajRmMzd2ZEdxL055ZC9vMHlwNGZwZUE4Zm9MSzFUVDRETU9ESm4xU1lqcz0%3D'
#API_KEY = environ.get('API_KEY')

bot = Client('LinkByPass bot',
             api_id= "1543212",
             api_hash= "d47de4b25ddf79a08127b433de32dc84",
             bot_token= "5462389029:AAEtTZT0mopLzVGM45SUmKHIFto_nEjc48M")


@bot.on_message(filters.command('start'))
async def start(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("**Your Banned**")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Join Update Channel**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("HELP", callback_data = "ghelp"),
                        InlineKeyboardButton("ABOUT", callback_data = "about"),
                        InlineKeyboardButton("CLOSE", callback_data = "close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
            )

@bot.on_message(filters.command('help'))
async def help(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("**Your Banned**")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Join Update Channel**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.HELP_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ABOUT', callback_data = "about"),
                    InlineKeyboardButton('CLOSE', callback_data = "close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
            )

@bot.on_message(filters.command('about'))
async def about(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("**Your Banned**")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Join Update Channel**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(
        text= Translation.ABOUT_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('HELP', callback_data = "ghelp"),
                    InlineKeyboardButton('CLOSE', callback_data = "close")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
            )

#@bot.on_message(filters.regex(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+"))
@bot.on_message(filters.command('bpp'))
async def link_handler(bot, message):
 # link = message.matches[0].group(0)
  l = message.text.split(' ', 1)

  if len(l) == 1:
        return await message.reply_text('Send Any GdTOT Link')
  link = l[1]
  mess = await message.reply_text("**Bypassing...⏳**",quote=True)
  if 'gdtot' in link:
    try:
        short_link = await gplinks(link)
      #  mess = await message.reply_text("**Bypassing...⏳**",quote=True)
        await mess.edit_text(f"**Bypassed URL** : {short_link} \n\n ©cc: {message.from_user.mention}",disable_web_page_preview=True)
    except Exception as e:
        await mess.edit_text(f"**Error** : {e}")
  elif 'droplink.co' in link:
     try:
        short_link = await droplink(link)
     #   mess = await message.reply_text("**Bypassing...⏳**",quote=True)
        await mess.edit_text(f"**Bypassed URL** : {short_link} \n\n ©cc: {message.from_user.mention}",disable_web_page_preview=True)
     except Exception as e:
        await mess.edit_text(f"**Error** : {e}")
  elif 'rocklinks.net' in link:
     try:
        short_link = await rocklink_bypass(link)
      #  mess = await message.reply_text("**Bypassing...⏳**",quote=True)
        await mess.edit_text(f"**Bypassed URL** : {short_link} \n\n ©cc: {message.from_user.mention}",disable_web_page_preview=True)
     except Exception as e:
        await mess.edit_text(f"**Error** : {e}")
  elif 'hubdrive.cc' in link:
     try:
        short_link = await hubdrive_bypass(link)
     #   mess = await message.reply_text("**Bypassing...⏳**",quote=True)
        await mess.edit_text(f"**Bypassed URL** : {short_link} \n\n ©cc: {message.from_user.mention}",disable_web_page_preview=True)

# GpLinksOld
async def gplinks_bypass1(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'

    res = client.head(url)
    header_loc = res.headers['location']
    param = header_loc.split('postid=')[-1]
    req_url = f'{p.scheme}://{p.netloc}/{param}'

    p = urlparse(header_loc)
    ref_url = f'{p.scheme}://{p.netloc}/'

    h = { 'referer': ref_url }
    res = client.get(req_url, headers=h, allow_redirects=False)

    bs4 = BeautifulSoup(res.content, 'html.parser')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    h = {
        'referer': ref_url,
        'x-requested-with': 'XMLHttpRequest',
    }
    time.sleep(10)
    res = client.post(final_url, headers=h, data=data)
    try:
        return res.json()['url'].replace('\/','/')
    except: 
        return "An Error Occured "



async def adfly(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    res = client.get(url).text
    out = {'error': False, 'src_url': url}
    try:
        ysmm = re.findall("ysmm\s+=\s+['|\"](.*?)['|\"]", res)[0]
    except:
        out['error'] = True
        return out
    url = decrypt_url(ysmm)
    if re.search(r'go\.php\?u\=', url):
        url = b64decode(re.sub(r'(.*?)u=', '', url)).decode()
    elif '&dest=' in url:
        url = unquote(re.sub(r'(.*?)dest=', '', url))
    out['bypassed_url'] = url
    return out
# -------------------------------------------

@bot.on_callback_query()
async def button(bot, update):
    if update.data == "start":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("HELP", callback_data = "ghelp"),
                        InlineKeyboardButton("ABOUT", callback_data = "about"),
                        InlineKeyboardButton("CLOSE", callback_data = "close")
                ]
            ]
        ))
    elif update.data == "ghelp":
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ABOUT', callback_data = "about"),
                    InlineKeyboardButton('CLOSE', callback_data = "close")
                ]
            ]
        ))
    elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('HELP', callback_data = "ghelp"),
                    InlineKeyboardButton('CLOSE', callback_data = "close")
                ]
            ]
        ))
    elif update.data == "close":
        await update.message.delete()
        try:
            await update.message.reply_to_message.delete()
        except:
            pass
   
    else:
       pass



bot.run()
