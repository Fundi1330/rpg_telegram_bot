from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from config import current_config, db
from random import randint
from database.utils import User

FIRST_NAME, LAST_NAME = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    db.usertable.insert([user_id])

    db.statstable.insert([user_id, randint(1, 5), randint(3, 6), randint(1, 9), 0, 100])

    welcome_message = current_config.get('welcome_message')
    first_name_message = current_config.get('first_name_message')

    await context.bot.send_message(update.effective_chat.id, text=welcome_message)

    await context.bot.send_message(update.effective_chat.id, text=first_name_message)

    return FIRST_NAME

async def first_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    last_name_message = current_config.get('last_name_message')
    await context.bot.send_message(update.effective_chat.id, text=last_name_message)

    user_id = update.effective_user.id
    first_name = update.effective_message.text
    user = db.usertable.get_first(user_id)

    if user[2] != None and user[3] != None:
        return ConversationHandler.END
    
    db.usertable.update(user_id, first_name=first_name)


    return LAST_NAME

async def last_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    last_name = update.effective_message.text
    db.usertable.update(user_id, last_name=last_name)

    after_auth_message = current_config.get('after_auth_message').format(name=User.get_full_name(user_id))
    await context.bot.send_message(chat_id=update.effective_chat.id, text=after_auth_message)
    

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass