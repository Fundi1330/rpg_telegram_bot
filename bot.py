from telegram.ext import *
import json

key = {}

with open('config.json', 'r') as file:
    read = json.load(file)

key = read

def start(update, context):
    update.message.reply_text('Travel RPG Bot is a simple rpg bot')

def main():
    updater = Updater(key['key'], use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()