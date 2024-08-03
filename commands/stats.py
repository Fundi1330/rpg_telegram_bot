import random
from telegram import Update
from telegram.ext import ContextTypes
from config import current_config
from database.utils import User

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    user_stats = User.get_stats(user_id)

    stats_message: str = current_config.get('stats_message').format(
        strength=user_stats[2], agility=user_stats[3], stamina=user_stats[4], 
        stat_points=user_stats[5], energy=user_stats[6]
    )

    await context.bot.send_message(update.effective_chat.id, text=stats_message)