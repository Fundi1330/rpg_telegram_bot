from telegram.ext import *
import json
import random

key = {}

with open('config.json', 'r') as file:
    read = json.load(file)

key = read


def start(update, context):
    update.message.reply_text('Travel RPG Bot is a simple rpg bot')


stat_points = 7
energy = 100


def stat(update, context):
    update.message.reply_text(
        f'Стати юзера: \n💪 Сила: {stats["strenght"]}, \n🏇 Спритність: {stats["agility"]}, \n🛡 Витривалітсть: {stats["endurance"]},\n Стат поінти:{stat_points}')



Goat = {"strength": 33, "agility": 3, "endurance": 2}
Trol = {"strength": 2, "agility": 1, "endurance": 2}
Lizzard = {"strength": 3, "agility": 2, "endurance": 3}

mountains = Goat, Trol, Lizzard

mountain_monster = (random.choice(mountains))

forest = "Орк", "Вовк", "Кабан"

Ork = {"strength": 2, "agility": 4, "endurance": 12}
Wolf = {"strength": 1, "agility": 1, "endurance": 2}
Kaban = {"strength": 3, "agility": 4, "endurance": 1}
forest_monster = (random.choice(forest))

stats = {"strenght": random.randint(1, 5), "agility": random.randint(2, 7), "endurance": random.randint(1, 9)}

def message(update, context):
    global stat_points
    global energy
    name = update.message.from_user.username
    mes = str(update.message.text).lower()
    if stat_points > 0:
        if mes == '1':
            stats["strenght"] += 1
            stat_points -= 1
        elif mes == '2':
            stats["agility"] += 1
            stat_points -= 1
        elif mes == '3':
            stats["endurance"] += 1
            stat_points -= 1
    else:
        update.message.reply_text('В тебе недостатньо скілл поінтів')
    
    # user_agility = stats["agility"]
    # user_strenght = stats["strenght"]
    # user_endurance = stats["endurance"]

    # mountin_monster_agility = mountain_monster["agility"]
    # mountin_monster_strenght = mountain_monster["strenght"]
    # mountin_monster_endurance = mountain_monster["endurance"]
    mountain_monster_name = ''

    if mountain_monster == Goat:
        mountain_monster_name = 'Козла'
    elif mountain_monster_name == Trol:
        mountain_monster_name = 'Троля'
    else:
        mountain_monster_name = 'Ящіра'

    if energy > 10:
        if mes == "гори":
            energy -= 15
            mes2 = str(update.message.text).lower()
            update.message.reply_text(f"{name} ти натрапив на {mountain_monster_name}, хочеш втекти ?")
            if mes2 == 'так':
                update.message.reply_text('Ти втік з гір')
                return 'Ти втік з гір'
            elif mes2 == 'ні' or 'гори':
                num = stats["agility"] // mountain_monster["agility"]
                stats["strenght"] * num
                mountain_monster["endurance"] - stats["strenght"]

                num = mountain_monster["agility"] // stats["agility"]
                stats["strenght"] * num
                stats["endurance"] - mountain_monster["strenght"]

                if stats["endurance"] >= 0:
                    update.message.reply_text("Ви програли.")
                elif mountain_monster["endurance"] == 0:
                    update.message.reply_text("Ви виграли!")
        # ._.

        elif mes == "ліс":
            update.message.reply_text(f"{name} ти натрапив на {forest_monster}!")
            num = stats["agility"] // forest_monster["agility"]
            stats["strenght"] * num
            forest_monster["endurancce"] -= stats["strenght"]

            num = forest_monster["agility"] // stats["agility"]
            stats["strenght"] * num
            stats["endurance"] -= forest_monster["strenght"]

            if stats['endurance'] == 0:
                update.message.reply_text("Ви програли.")
            elif forest_monster['endurance'] == 0:
                update.message.reply_text("Ви виграли!")
        # ._.
    else:
        update.message.reply_text('У вас недостатньо енергії')


def add_points(update, context):
    if stat_points > 0:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Яку з характеристик ти хочеш покращити? 1.Сила, 2.Спритність, 3.Витривалість (Введи число)')
    else:
        update.message.reply_text('В тебе недостатньо скілл поінтів')





# Це по ідеї мала би бути система тої бійні і ше зверху якісь монстри
# Але._. Там все ще є та сама помилка. Хоч я і переробила
# def map(update, context):
#     mes2 = str(update.message.text).lower
#     name = update.message.from_user.username

#     # ._.
#     # if energy > 10:
#     #     if mes2 == "гори":
#     #         update.message.reply_text(f"{name} ти натрапив на {mountain_monster}, хочеш втекти ?")

#     #         num = stats["agility"] // mountain_monster["agility"]
#     #         stats['strenght'] * num
#     #         mountain_monster["endurancce"] -= stats["strenght"]

#     #         num = mountain_monster["agility"] // stats["agility"]
#     #         stats["strenght"] * num
#     #         stats["endurance"] -= mountain_monster["strenght"]

#     #         if stats['endurance'] == 0:
#     #             update.message.reply_text("Ви програли.")
#     #         elif mountain_monster['endurance'] == 0:
#     #             update.message.reply_text("Ви виграли!")
#     #     # ._.

#     #     elif mes2 == "ліс":
#     #         update.message.reply_text(f"{name} ти натрапив на {forest_monster}!")
#     #         num = stats["agility"] // forest_monster["agility"]
#     #         stats['strenght'] * num
#     #         forest_monster["endurancce"] -= stats["strenght"]

#     #         num = forest_monster["agility"] // stats["agility"]
#     #         stats["strenght"] * num
#     #         stats["endurance"] -= forest_monster["strenght"]

#     #         if stats['endurance'] == 0:
#     #             update.message.reply_text("Ви програли.")
#     #         elif forest_monster['endurance'] == 0:
#     #             update.message.reply_text("Ви виграли!")
#     #     # ._.
#     # else:
#     #     update.message.reply_text('У вас недостатньо енергії')


def location(update, context):
    update.message.reply_text('Куди ви хочете піти подорожувати сьогодні? Ліс/Гори')


# def map(update, context):
#    name = update.message.from_user.username
#    global mountain_monster
#    global forest_monster                                  ото всьо ахілея

#    mes2 = str(update.message.text).lower
#    if mes2 == "гори":
#        context.bot.send_message(chat_id=update.effective_chat.id,
#                                 text=f"{name}ти натрапив на{mountain_monster}!")

#    elif mes2 == "ліс":
#        context.bot.send_message(chat_id=update.effective_chat.id,
#                                 text=f"{name}ти натрапив на{forest_monster}!")


# def locations(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id,
#                             text='Куди ви хочете піти подорожувати сьогодні? Ліс/Гори')
#    map(update,context)
#    if text == "гори":
#        def mountaine(update, context):
#            update.message.reply_text(f"Ви натрапили на {mountain_monster}!")
#            update.message.reply_text(f"{name}, Продовжувати бій чи все-таки втекти?")
#            text = str(update.message.text).lower
#            if text ==  1:                                                      і то теж ахілея
#    elif text =="ліс":
#        def forest(update, context):
#            update.message.reply_text(f"Ви натрапили на {forest_monster}!")


# name = update.message.from_user.username
# with open('db.json', 'r') as db:
#     info = dict(db.read())

# print(info)                                     а це всьо вже було в ришітці

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


# def sample_responses(input_text):
#     global stat_points
#     user_message = input_text
#     if user_message == 1:
#         stats["strenght"] += 1
#         stat_points -= 1
#     elif user_message == 2:
#         stats["agility"] += 1
#         stat_points -= 1
#     elif user_message == 3:
#         stats["endurance"] += 1
#         stat_points -= 1
def error(update, context):
    print(f'Update {update} caused error {context.error}')


def help(update, context):
    update.message.reply_text('''
Привіт👋, це Travel RPG Bot🏞
Якщо хочеш перевірити✅/додати➕ свої характеристики пропиши /stat
''')


# ._.
def main():
    updater = Updater(key['key'], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stat', stat))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('addpoints', add_points))
    dp.add_handler(CommandHandler('location', location))
    dp.add_handler(MessageHandler(filters=Filters.text, callback = message))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    print('Bot is started')
