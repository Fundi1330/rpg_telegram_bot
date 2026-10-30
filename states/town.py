from telegram.ext import ConversationHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from config import config
from commands.stats import stats

TOWN = 2

async def town(update: Update, context: ContextTypes.DEFAULT_TYPE):
    town_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📋Go to information board', callback_data='t_board'),
                InlineKeyboardButton('💰Sell stuff to traders', callback_data='t_trade')
            ],
            [
                InlineKeyboardButton('✈️Begin your new journey!', callback_data='t_journey'),
                InlineKeyboardButton('📜See your stats', callback_data='t_stats')
            ],
        ]
    )

    select_action_in_town_message = config.select_action_in_town_message

    await context.bot.send_message(chat_id=update.effective_chat.id, text=select_action_in_town_message, reply_markup=town_keyboard)

async def town_callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()
    query_data = query.data

    if query_data == 't_board':
        board_message = config.board_message

        await context.bot.send_message(chat_id=update.effective_chat.id, text=board_message)
    elif query_data == 't_trade':
        pass
        # return TRADE
    elif query_data == 't_stats':
        await stats(update, context)
    elif query_data == 't_journey':
        pass
        # return JOURNEY
    
    return TOWN