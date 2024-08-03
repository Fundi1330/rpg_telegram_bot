from telegram import Update
from telegram.ext import ContextTypes
from config import current_config

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = current_config.get('help_message')

    await context.bot.send_message(update.effective_chat.id, text=help_message)