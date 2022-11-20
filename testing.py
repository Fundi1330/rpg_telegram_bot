from telegram.ext import *
import json
import random

key = {}

with open('config.json', 'r') as file:
    read = json.load(file)

key = read


def start(update, context):
    update.message.reply_text('Travel RPG Bot is a simple rpg bot')

with open('db.json', 'r') as file:
    db = json.load(file)

stat_points = 7
energy = 100

def stat(update, context):
    name = update.message.from_user.username
    local_stats = {}
    for i in db:
        if i == name:
            for с in dict(db[i]):
                local_stats[с] = db[i][с]
                update.message.reply_text(
                    f'Стати юзера: \n💪 Сила: {local_stats["strenght"]}, \n🏇 Спритність: {local_stats["agility"]},'
                    f' \n🛡 Витривалітсть: {local_stats["endurance"]},\n Стат поінти:{stat_points}')

        elif i != name:
            stats = {'strenght': random.randint(1, 5), 'agility': random.randint(2, 7),
                     'endurance': random.randint(1, 9)}

            update.message.reply_text(f'Стати юзера: \n💪 Сила: {stats["strenght"]}, '
                                      f'\n🏇 Спритність: {stats["agility"]}, \n🛡 Витривалітсть: {stats["endurance"]},'
                                      f'\n Стат поінти:{stat_points}')
            temporary_dict = dict[name]=stats
            json_object = json.dumps(local_stats, indent = 2)
            with open("db.json", "w") as outfile:
                outfile.write(json_object)
            print(temporary_dict)


    print(local_stats, "Thinking...")


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



def location(update, context):
    update.message.reply_text('Куди ви хочете піти подорожувати сьогодні? Ліс/Гори')



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
    dp.add_handler(MessageHandler(filters=Filters.text, callback=message))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    print('Bot is started')