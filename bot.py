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
stat_points = 7

def stat(update, context):
    update.message.reply_text(f'Стати юзера: \n💪 Сила: {stats["strenght"]}, \n🏇 Спритність: {stats["agility"]}, \n🛡 Витривалітсть: {stats["endurance"]},\n Стат поінти:{stat_points}')

    # name = update.message.from_user.username
    # with open('db.json', 'r') as db:
    #     info = dict(db.read())

    # print(info)
    
    # for k, v in info:
    #     if k == name:
    #         update.message.reply_text(f'Стати юзера: \n💪 Сила: {v["strenght"]}, \n🏇 Спритність: {v["agility"]}, \n🛡️ Витривалітсть: {v["endurance"]}')
    # if stat_points > 0:
    #     update.message.reply_text("У тебе є вільні стат поінти, хочеш їх використати?")
    #     user_message = str(text).lower()
    #     if user_message in ('так', 'ага'):
    #         update.message.reply_text("Що ви хочете підвищити? Введіть номер: 1.Сила, 2.Спритність, 3.Витривалість")
    #     if user_message == 1:
    #             stats["strenght"] += 1
    #     elif user_message == 2:
    #             stats["agility"] += 1
    #     elif user_message == 3:
    #             stats["endurance"] += 1
    #     else:
    #             update.message.reply_text("ви ввели не введіть число від 1 до 3")
    # return 'I do not understand you!'
def sample_responses(input_text):
    global stat_points
    user_message = input_text
    
    if user_message == 1:
        stats["strenght"] += 1
        stat_points -= 1
    elif user_message == 2:
        stats["agility"] += 1
        stat_points -= 1
    elif user_message == 3:
        stats["endurance"] += 1
        stat_points -= 1

def add_points(update, context):
    if stat_points > 0:
        update.message.reply_text('Яку з характеристик ти хочеш покращити? 1.Сила, 2.Спритність, 3.Витривалість')
        text = str(update.message.text).lower()
        if text == '/addpoint':
            text = str(update.message.text).lower()
        sample_responses(text)
    else:
        update.message.reply_text('В тебе недостатньо скілл поінтів')



def error(update, context):
    print(f'Update {update} caused error {context.error}')

def help(update, context):
    update.message.reply_text('''
Привіт👋, це Travel RPG Bot🏞
Якщо хочеш перевірити✅/додати➕ свої характеристики пропиши /stat
''')

def main():
    updater = Updater(key['key'], use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stat', stat))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('addpoints', add_points))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()