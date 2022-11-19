import random

from telegram.ext import *
import json
from emoji import *

key = {}

with open('config.json', 'r') as file:
    read = json.load(file)

key = read

def start(update, context):
    update.message.reply_text('Travel RPG Bot is a simple rpg bot')



def stat(update, context):

       stats = emojize(":flexed_biceps: Сила:",random.randint(1,5),
                             "\n:horse_racing: Спритність:",random.randint(2,7),
                             "\n:shield: Витривалість:",random.randint(1,9),
                      )
       update.message.reply_text(f'Стати юзера: {stats}')



def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(key['key'], use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stat', stat))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()