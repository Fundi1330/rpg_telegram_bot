from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import current_config
from os import path
from json import loads
import logging
from mutagen.mp3 import MP3

music_path = path.join(current_config.get('assets_dir'), current_config.get('music_dir'))
music_data_path = path.join(music_path, 'data.json')

def read_music_data():
   
    with open(music_data_path, 'r') as music_data:
        music_data_dict: dict = loads(music_data.read())

    return music_data_dict

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    music_data = read_music_data()
    for title in music_data.keys():
        keyboard.append([InlineKeyboardButton(title, callback_data=title)])

    reply_markup = InlineKeyboardMarkup(keyboard)

    select_music_message = current_config.get('select_music_message')

    await context.bot.send_message(chat_id=update.effective_chat.id, text=select_music_message, reply_markup=reply_markup)

async def music_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    music_title = query.data

    query_music = read_music_data().get(music_title)

    with open(f'{music_path}/{query_music}', 'rb') as music_file:
        music = music_file.read()
        music_duration = MP3(music_file).info.length
        await context.bot.send_voice(chat_id=update.effective_chat.id, voice=music, duration=music_duration, caption=music_title)