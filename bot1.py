from telegram.ext import *
import json
import random
from telegram import *

key = {}

with open('config.json', 'r') as file:
    read = json.load(file)

key = read


def start(update, context):
    name = update.message.from_user.username
    stats = {"name": name, "strength": random.randint(1, 5), "agility": random.randint(2, 7),
             "endurance": random.randint(1, 9),"stat_points":7, "energy": 100}
    update.message.reply_text('Travel RPG Bot is a simple rpg bot')

    with open('db.json') as f:
        data = json.load(f)
        data['users'].append(stats)
        with open('db.json', 'w') as outfile:
            json.dump(data, outfile)

            random_img = random.randint(1, 2)
            if random_img == 1:
                random_img1 = random.randint(1, 2)
                if random_img1 == 1:
                    update.message.reply_photo(
                        photo=open(r"C:\Users\User\Pictures\Saved Pictures\photo-1511117833895-4b473c0b85d6.jpg", "rb"))
                else:
                    update.message.reply_photo(
                        photo=open(r"C:\Users\User\Pictures\Saved Pictures\Plane-taking-off-twilight-1024x684.jpg",
                                   "rb"))
            else:
                random_img2 = random.randint(1, 2)
                if random_img2 == 1:
                    update.message.reply_photo(
                        photo=open(r"C:\Users\User\Pictures\Saved Pictures\0x0.jpg", "rb"))
                else:
                    update.message.reply_photo(
                        photo=open(r"C:\Users\User\Pictures\Saved Pictures\ss_2ecaeff42c548d1200668869a8767.jpg",
                                   "rb"))


#stat_points = 7


def stat(update, context):
    with open('db.json', 'r') as db:
        info = json.load(db)


    name = update.message.from_user.username
    local_stats = {}

    for i in info['users']:
        if i['name'] == name:
            for k in i:

                local_stats[k] = i[k]

    update.message.reply_text(
        f'Стати юзера: \n💪 Сила: {local_stats["strength"]}, \n🏇 Спритність: {local_stats["agility"]}, \n🛡 Витривалітсть: {local_stats["endurance"]},\n Стат поінти:{local_stats["stat_points"]},\nЕнергія:{local_stats["energy"]} ')



Goat = {"strength": 33, "agility": 3, "endurance": 2, 'health': 10}
Trol = {"strength": 12, "agility": 1, "endurance": 2, 'health': 25}
Lizzard = {"strength": 13, "agility": 2, "endurance": 3, 'health': 20}

mountains = Goat, Trol, Lizzard
mountain_monster = random.choice(mountains)

Ork = {"strength": 2, "agility": 4, "endurance": 12, 'health': 35}
Wolf = {"strength": 1, "agility": 1, "endurance": 2, 'health': 25}
Kaban = {"strength": 3, "agility": 4, "endurance": 1, 'health': 20}

forest = Ork, Wolf, Kaban
forest_monster = random.choice(forest)
end_battle = False

mountain_monster_name = ''
forest_monster_name = ''

if mountain_monster == Goat:
    mountain_monster_name = 'Козла'
elif mountain_monster == Trol:
    mountain_monster_name = 'Троля'
else:
    mountain_monster_name = 'Ящіра'

if forest_monster == Ork:
    forest_monster_name = 'Орка'
elif forest_monster == Wolf:
    forest_monster_name = 'Вовка'
else:
    forest_monster_name = 'Кабана'


# stats = {"strength": random.randint(1, 5), "agility": random.randint(2, 7), "endurance": random.randint(1, 9)}
yes_list = []
user_move = True
user_health = 40

potion = 2

# stats = {"strength": random.randint(1, 5), "agility": random.randint(2, 7), "endurance": random.randint(1, 9)}
yes_list = []

def message(update, context):
    global user_move, user_health
    global yes_list
    global mountain_monster, mountain_monster_name, forest_monster, forest_monster_name
    mes = str(update.message.text).lower()


    with open('db.json', 'r') as db:
        info = json.load(db)

    db = info

    name = update.message.from_user.username
    local_stats = {}


    for i in db['users']:
        if i['name'] == name:
            for k in i:
                local_stats[k] = i[k]

    if local_stats["stat_points"] > 0:
        if mes == '1':
            local_stats["strength"] += 1
            local_stats["stat_points"] -= 1
            for i in info['users']:
                if i['name'] == name:
                    for k in i:
                        i[k] = local_stats[k]

                        with open("db.json", "w") as f:
                            json.dump(info, f)
        elif mes == '2':
            local_stats["agility"] += 1
            local_stats["stat_points"] -= 1
            for i in info['users']:
                if i['name'] == name:
                    for k in i:
                        i[k] = local_stats[k]

                        with open("db.json", "w") as f:
                            json.dump(info, f)
        elif mes == '3':
            local_stats["endurance"] += 1
            local_stats["stat_points"] -= 1
            for i in info['users']:
                if i['name'] == name:
                    for k in i:
                        i[k] = local_stats[k]

                        with open("db.json", "w") as f:
                            json.dump(info, f)
    else:
        update.message.reply_text('В тебе недостатньо скілл поінтів')


    if local_stats["energy"] > 10:
        yes_list.append(update.message.text)
        if mes == "гори":
            local_stats["energy"] -= 15
            update.message.reply_text(f"{name} ти натрапив на {mountain_monster_name}, хочеш втекти ?")


        if 'так' in yes_list:
            yes_list = []
            update.message.reply_text('Ти втік з гір')
        elif 'ні' in yes_list:
            yes_list = []
            fight_menu = [
                [
                    KeyboardButton('Атакувати'),
                    KeyboardButton('Захищатись'),
                    KeyboardButton('Випити зілля'),
                    KeyboardButton('Панікувати')
                ]
            ]
            update.message.reply_text('Ти почав бій! Що будеш робити?', reply_markup=ReplyKeyboardMarkup(fight_menu))

        elif 'Атакувати' in yes_list:

            if local_stats['strength'] > 1 and local_stats['strength'] < 5 and not mountain_monster[
                                                                                       'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(6, 8)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]  # якесь к1
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')
            elif local_stats['strength'] > 5 and local_stats['strength'] < 10 and not mountain_monster[
                                                                                        'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(11, 13)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')

            elif local_stats['strength'] > 10 and local_stats['strength'] < 15 and not mountain_monster[
                                                                                        'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(17, 21)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')
            elif local_stats['strength'] > 15 and local_stats['strength'] < 20 and not mountain_monster[
                                                                                        'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(23, 29)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')
            elif local_stats['strength'] > 20 and local_stats['strength'] < 25and not mountain_monster[
                                                                                        'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(29, 37)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')
            elif local_stats['strength'] > 25 and local_stats['strength'] < 30and not mountain_monster[
                                                                                        'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(35, 45)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')
            elif local_stats['strength'] > 30 and local_stats['strength'] < 35and not mountain_monster[
                                                                                        'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(45, 53)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')
        elif "Панікувати" in yes_list:
            user_move = True
            if mountain_monster['strength'] >= 33:  # Козел
                moster_damage = random.randint(12, 40)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health = user_health - moster_damage
                    update.message.reply_text(f'(чого ти нажав на цю кнопку??)Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))

            if mountain_monster['strength'] >= 2:  # Троль
                moster_damage = random.randint(2, 12)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health = user_health - moster_damage
                    update.message.reply_text(
                        f'(чого ти нажав на цю кнопку??)Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))

            if mountain_monster['strength'] >= 3:  # Ящір
                moster_damage = random.randint(3, 14)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health = user_health - moster_damage
                    update.message.reply_text(
                        f'(чого ти нажав на цю кнопку??)Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))

                else:
                    update.message.reply_text('Монстр промахнувся по тобі!')
        elif 'Захищатись' in yes_list:
            user_move = True
            if mountain_monster['strength'] >= 33:  # Козел
                moster_damage = random.randint(12, 40)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    moster_damage_1proz= moster_damage/100
                    first_num = moster_damage_1proz*80
                    second_num = moster_damage_1proz*50

                    hp_safe = random.randint[first_num, second_num]
                    chance2 = random.choices([1, 2], weights=[85, 15], k=1)[0]
                    if chance2 == 1:

                        user_health2 = user_health + hp_safe
                        past_hp = user_health + moster_damage

                        moster_dmg_safe = past_hp - user_health2
                        update.message.reply_text(
                            f'Проте тобі вдалося захиститись і монстр наніс тобі лише{moster_dmg_safe} урону')

                    else:
                        update.message.reply_text(
                            'ти якийсь не везучий,монстр вдарив по тобі зі сліпої точки та твій захист не спрацював!')
                else:
                    moster_damage = moster_damage*2
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}! Це вдвічі більше його нормального урону, схоже що він розізлився побачивши твій захист!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    moster_damage_1proz = moster_damage / 100
                    first_num = moster_damage_1proz * 80
                    second_num = moster_damage_1proz * 50

                    hp_safe = random.randint[first_num, second_num]
                    chance2 = random.choices([1, 2], weights=[85, 15], k=1)[0]
                    if chance2 == 1:

                        user_health2 = user_health + hp_safe
                        past_hp = user_health + moster_damage

                        moster_dmg_safe = past_hp - user_health2
                        update.message.reply_text(
                            f'Проте тобі вдалося захиститись і монстр наніс тобі лише{moster_dmg_safe} урону')

                    else:
                        update.message.reply_text(
                            'ти якийсь не везучий,монстр вдарив по тобі зі сліпої точки та твій захист не спрацював!')

            if mountain_monster['strength'] >= 2:  # Троль
                moster_damage = random.randint(2, 12)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    moster_damage_1proz = moster_damage / 100
                    first_num = moster_damage_1proz * 80
                    second_num = moster_damage_1proz * 50

                    hp_safe = random.randint[first_num, second_num]
                    chance2 = random.choices([1, 2], weights=[65, 35], k=1)[0]
                    if chance2 == 1:

                        user_health2 = user_health + hp_safe
                        past_hp = user_health + moster_damage

                        moster_dmg_safe = past_hp - user_health2
                        update.message.reply_text(
                            f'Проте тобі вдалося захиститись і монстр наніс тобі лише{moster_dmg_safe} урону')

                    else:
                        update.message.reply_text(
                            'ти якийсь не везучий,монстр вдарив по тобі зі сліпої точки та твій захист не спрацював!')
                else:
                    moster_damage = moster_damage/2
                    user_health -= moster_damage
                    update.message.reply_text(
                        f'Монстр наніс тобі {moster_damage}! Він налякався побачивши твою захисну стійку! ')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    moster_damage_1proz = moster_damage / 100
                    first_num = moster_damage_1proz * 80
                    second_num = moster_damage_1proz * 50

                    hp_safe = random.randint[first_num, second_num]
                    chance2 = random.choices([1, 2], weights=[85, 15], k=1)[0]
                    if chance2 == 1:
                        user_health2 = user_health + hp_safe
                        past_hp = user_health + moster_damage

                        moster_dmg_safe = past_hp - user_health2
                        update.message.reply_text(
                            f'Проте тобі вдалося захиститись і монстр наніс тобі лише{moster_dmg_safe} урону')



            if mountain_monster['strength'] >= 3:  # Ящір
                moster_damage = random.randint(3, 14)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    moster_damage_1proz = moster_damage / 100
                    first_num = moster_damage_1proz * 80
                    second_num = moster_damage_1proz * 50

                    hp_safe = random.randint[first_num, second_num]
                    chance2 = random.choices([1, 2], weights=[65, 35], k=1)[0]
                    if chance2 == 1:

                        user_health2 = user_health + hp_safe
                        past_hp = user_health + moster_damage

                        moster_dmg_safe = past_hp - user_health2
                        update.message.reply_text(
                            f'Проте тобі вдалося захиститись і монстр наніс тобі лише{moster_dmg_safe} урону')

                    else:
                        update.message.reply_text(
                            'ти якийсь не везучий,монстр вдарив по тобі зі сліпої точки та твій захист не спрацював!')
                else:
                    moster_damage = moster_damage/2
                    user_health -= moster_damage
                    update.message.reply_text(
                        f'Монстр наніс тобі {moster_damage}! Він налякався побачивши твою захисну стійку! ')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    moster_damage_1proz = moster_damage / 100
                    first_num = moster_damage_1proz * 80
                    second_num = moster_damage_1proz * 50

                    hp_safe = random.randint[first_num, second_num]
                    chance2 = random.choices([1, 2], weights=[85, 15], k=1)[0]
                    if chance2 == 1:
                        user_health2 = user_health + hp_safe
                        past_hp = user_health + moster_damage

                        moster_dmg_safe = past_hp - user_health2
                        update.message.reply_text(
                            f'Проте тобі вдалося захиститись і монстр наніс тобі лише{moster_dmg_safe} урону')

        elif 'Випити зілля' in yes_list:
            user_move = True
            if mountain_monster['strength'] >= 330:  # Козел
                moster_damage = random.randint(12, 40)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    hp_safe = random[10, 20]
                    user_health = user_health + hp_safe

                    update.message.reply_text(f'ти відновив{hp_safe} хп')

            if mountain_monster['strength'] >= 12:  # Троль
                moster_damage = random.randint(2, 12)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    hp_safe = random[10, 20]
                    user_health = user_health + hp_safe

                    update.message.reply_text(f'ти відновив{hp_safe} хп')

            if mountain_monster['strength'] >= 13:  # Ящір
                moster_damage = random.randint(3, 14)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    hp_safe = random[10, 20]
                    user_health = user_health + hp_safe

                    update.message.reply_text(f'ти відновив{hp_safe} хп')

            # Ти точно впевнений що це іф стоїть на правельному рядку?
            if mountain_monster['health'] <= 0:
                user_move = True
                Goat = {"strength": 33, "agility": 3, "endurance": 2, 'health': 10}
                Trol = {"strength": 2, "agility": 1, "endurance": 2, 'health': 25}
                Lizzard = {"strength": 3, "agility": 2, "endurance": 3, 'health': 20}
                update.message.reply_text('Ти виграв битву!', reply_markup='')

        # ._.

        if mes == "ліс":
            update.message.reply_text(f"{name} ти натрапив на {forest_monster_name}!")

        # ._.
    else:
        update.message.reply_text('У вас недостатньо енергії')


def add_points(update, context):
        with open('db.json', 'r') as db:
            info = json.load(db)

        name = update.message.from_user.username
        local_stats = {}


        for i in info['users']:
            if i['name'] == name:
                for k in i:
                    local_stats[k] = i[k]

        if local_stats["stat_points"] > 0:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Яку з характеристик ти хочеш покращити? 1.Сила, 2.Спритність, 3.Витривалість (Введи число)')
        else:
            update.message.reply_text('В тебе недостатньо скілл поінтів')


def location(update, context):
    update.message.reply_text('Куди ви хочете піти подорожувати сьогодні? Ліс/Гори')


def music(update, context):
    keyboard = [
        [InlineKeyboardButton('Skyrim', callback_data='1')],
        [InlineKeyboardButton('Black Wolwes Inn', callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Вибери музику, яку хочеш слухати', reply_markup=reply_markup)


def callback(update, context):
    name = update.message.from_user.username
    local_stats = {}
    with open('db.json', 'r') as db:
        info = json.load(db)

    for i in info['users']:
        if i['name'] == name:
            for k in i:
                local_stats[k] = i[k]

    query = update.callback_query
    answer = query.data

    if answer == '1':
        with open('music/skyrim.mp3', 'rb') as music:
            sound = music.read()
        query.message.reply_voice(sound)
    elif answer == '2':
        with open('music/inn.mp3', 'rb') as inn:
            bw = inn.read()
        query.message.reply_voice(bw)

    # update.message.reply_text('hello11deadaf')

    def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
        name = update.message.from_user.username
        local_stats = {}
        with open('db.json', 'r') as db:
            info = json.load(db)

        for i in info['users']:
            if i['name'] == name:
                for k in i:
                    local_stats[k] = i[k]

        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, header_buttons)
        if footer_buttons:
            menu.append(footer_buttons)
        return menu

    if local_stats["energy"] > 10:
        button_list = []
        lis_horu = ["ліс", "гори"]

        for i in lis_horu:
            button_list.append(InlineKeyboardButton(i, callback_data=i))
            reply_markup = InlineKeyboardMarkup(
                build_menu(button_list, n_cols=1))  # n_cols = 1 is for single column and mutliple rows
        update.message.reply_text('Куди ви хочете піти подорожувати сьогодні? ', reply_markup=reply_markup)

    # def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    #
    #     menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    #     if header_buttons:
    #         menu.insert(0, header_buttons)
    #     if footer_buttons:
    #         menu.append(footer_buttons)
    #     return menu

    # def callback_handler_Parara(update, context):
    #     global energy
    #     button_list = []
    #     handler = update.callback_query
    #     answer = handler.data
    #     if answer == "гори":
    #         print("ти вибрав гори")
    #         yes_no = ["так", "ні"]
    #         for b in yes_no:
    #             print(type(b))
    #             name = handler.message.from_user.username
    #             button_list.append(InlineKeyboardButton(b, callback_data=b))
    #             print(button_list)
    #             reply_markup = InlineKeyboardMarkup(
    #                 str(button_list))  # n_cols = 1 is for single column and mutliple rows
    #         energy -= 15
    #         handler.message.reply_text(f"{name} ти натрапив на {mountain_monster_name}, хочеш втекти ?",
    #                                    reply_markup=reply_markup)
    #         if answer == 'так':
    #             handler.message.reply_text('Ти втік з гір')
    #         elif answer == 'ні':
    #             print("дойшло до цього ні")


def error(update, context):
    print(f'Update {update} caused error {context.error}')


def help(update, context):
    update.message.reply_text('''
Привіт👋, це Travel RPG Bot🏞
\nЯкщо хочеш перевірити✅ свої характеристики пропиши /stat
\nЯкщо хочеш додати➕ поінти до характеристик тоді пропиши /addpoints
\nЩоб розпочати свою подорож🚊 пропиши /location
\nЩоб дізнатися трохи більше😎 пропиши /start 
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
    dp.add_handler(CommandHandler('music', music))
    dp.add_handler(MessageHandler(filters=Filters.text, callback=message))
    # dp.add_handler(CallbackQueryHandler(callback_handler_Parara))

    dp.add_handler(CallbackQueryHandler(callback))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    print('Bot is started')
