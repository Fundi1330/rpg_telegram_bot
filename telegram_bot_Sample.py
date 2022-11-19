# 1. Install python-telegram-bot
from telegram.ext import *
# import telegram.ext
# 2. Open Telegram app
# 3. Search BotFather
# 4. Click on him
# 5. Click START
# 6. Write /newbot
# 7. Enter bot name
# 8. Enter username that has ends with suffix -bot
# 9. Copy your token API
# 10. Start writing your cod


# name Py_3
# username py_3_my_bot
# API 5856235274:AAFZWlZhwTsY3mlf_kc9lwELO5CdQ381PMA

KEY_API = '5856235274:AAFZWlZhwTsY3mlf_kc9lwELO5CdQ381PMA'


def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ('hello', 'hi'):
        return 'Hey ! How are you'

    return 'I do not understand you!'


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text)
    update.message.reply_text(response)


def contact(update, context):
    phone_number = '123 321 111'
    update.message.reply_text(f'My phone number is: {phone_number}')


def start_command(update, context):
    update.message.reply_text('Type something here...')


def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(KEY_API, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('phone', contact))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
