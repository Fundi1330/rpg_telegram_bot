import random
from telegram import Update
from telegram.ext import ContextTypes
from config import current_config, db

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    db.usertable.insert([user_id])

    

    welcome_message = current_config.get('welcome_message')

    await context.bot.send_message(update.effective_chat.id, text=welcome_message)