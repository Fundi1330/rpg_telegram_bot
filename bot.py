from telegram.ext import *
import json
import random

key = {}

with open('config.json', 'r') as file:
    read = json.load(file)

key = read

def start(update, context):
    update.message.reply_text('Travel RPG Bot is a simple rpg bot')


stats = {'strenght': random.randint(1, 5), 'agility': random.randint(2, 7), 'endurance': random.randint(1,9)}

def stat(update, context):
    name = update.message.from_user.username
    with open('db.json', 'r') as db:
        info = dict(db.read())

    print(info)
    
    for k, v in info:
        if k == name:
            update.message.reply_text(f'Стати юзера: \n💪 Сила: {v["strenght"]}, \n🏇 Спритність: {v["agility"]}, \n🛡️ Витривалітсть: {v["endurance"]}')
    



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