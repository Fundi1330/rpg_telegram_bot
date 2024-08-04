from telegram.ext import ApplicationBuilder,  CallbackQueryHandler, CommandHandler, ConversationHandler, MessageHandler, filters
from os import environ
import logging
from commands import start, music, music_query_handler, help, stats, \
                     last_name, LAST_NAME, first_name, FIRST_NAME, cancel


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
token = environ.get('TELEGRAM_BOT_API_TOKEN')

def main():
    
    app = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    music_handler = CommandHandler('music', music)
    stats_handler = CommandHandler('stats', stats)
    music_callback_handler = CallbackQueryHandler(music_query_handler)

    start_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            FIRST_NAME: [MessageHandler(filters.TEXT, first_name)],
            LAST_NAME: [MessageHandler(filters.TEXT, last_name)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handlers([start_handler, music_handler, music_callback_handler, help_handler,
                      stats_handler])

    app.run_polling()




if __name__ == '__main__':
    main()
    print('Bot has started')