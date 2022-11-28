from telegram.ext import *
import json
import random
from telegram import *

key = {}

with open('config.json', 'r') as file:
    read = json.load(file)

key = read

# ---------------------------------------------------------------------------- #
#                                 Example Text                                 #
# ---------------------------------------------------------------------------- #
def start(update, context):
    name = update.message.from_user.username

    stats = {"name": name, "strength": random.randint(1, 5), "agility": random.randint(2, 7), "endurance": random.randint(1, 9), "energy": 100, "health": 40}

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

    # with open('db.json') as f:
    #     data = json.load(f)
    # name = update.message.from_user.username
    # local_stats = {}
    # for i in data["users"]:
    #     for b in i:
    #         if name is None:
    #             num_lib = []
    #             for v in data["users"]:
    #                 num_lib+= v
    #             biggest_num = max(num_lib)
    #             norm_num = (int(biggest_num)) + 1
    #             numero = str(norm_num)

    #             data["users"][numero] = {name: True}
    #             with open("db.json", "w") as f:
    #                 json.dump(data, f, indent=4)
    #         else:
    #             for a in b:
    #                 local_stats[name] = a

    update.message.reply_text(
        f'Стати юзера: \n💪 Сила: {local_stats["strength"]}, \n🏇 Спритність: {local_stats["agility"]}, \n🛡 Витривалітсть: {local_stats["endurance"]},\n Стат поінти:{local_stats["stat_points"]},\nЕнергія:{local_stats["energy"]} ')


    # with open('db.json') as f:
    #     data = json.load(f)
    # name = update.message.from_user.username
    # local_stats = {}
    # for i in data["users"]:
    #     for b in i:
    #         if name is None:
    #             num_lib = []
    #             for v in data["users"]:
    #                 num_lib+= v
    #             biggest_num = max(num_lib)
    #             norm_num = (int(biggest_num)) + 1
    #             numero = str(norm_num)
    #
    #             data["users"][numero] = {name: True}
    #             with open("db.json", "w") as f:
    #                 json.dump(data, f, indent=4)
    #         else:
    #             for a in b:
    #                 local_stats[name] = a

    #
    # db = info
    # data = {}
    # sup = {}
    #
    # name = update.message.from_user.username
    # local_stats = {}
    # stats = {'strength': random.randint(1, 5), 'agility': random.randint(2, 7), 'endurance': random.randint(1, 9)}
    #
    # for i in db:
    #     for b in i:
    #         if b == name:
    #             for k in dict(db[b]):
    #                 local_stats[k] = db[b][k]
    #             update.message.reply_text(f'Стати @{name}: \n💪 Сила: {local_stats["strength"]}, \n🏇 Спритність: {local_stats["agility"]}, \n🛡 Витривалітсть: {local_stats["endurance"]},\n 🌟Стат поінти:{stat_points}')
    #         elif name not in db:
    #             sup.update({name: stats})
    #             data.update({"users":sup})
    #             update.message.reply_text(f'Стати @{name}: \n💪 Сила: {data["strength"]}, \n🏇 Спритність: {data["agility"]}, \n🛡 Витривалітсть: {data["endurance"]},\n🌟 Стат поінти:{stat_points}')
    #             with open("db.json", "w") as outfile:
    #                 json.dump(data, outfile, indent=4,)


# я ще в школі варіант з гет і нон попробую ._.


Goat = {"strength": 33, "agility": 3, "endurance": 2, 'health': 10}
Trol = {"strength": 2, "agility": 1, "endurance": 2, 'health': 25}
Lizzard = {"strength": 3, "agility": 2, "endurance": 3, 'health': 20}

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
 
words_list = []
user_move = True

potion = 2
 
yes_list = []
 

def message(update, context):
    global energy
    global user_move, user_health
 
    global words_list
    global mountain_monster, mountain_monster_name, forest_monster, forest_monster_name, Goat, Trol, Lizzard, Wolf, Kaban, Ork
 
    global yes_list
    global mountain_monster, mountain_monster_name, forest_monster, forest_monster_name
 
    mes = str(update.message.text).lower()
    name = update.message.from_user.username

    # forest_monster = random.choice(forest)
    # mountain_monster = random.choice(mountains)

    # if stat_points > 0:
    #     # if mes == '1':
    #     #     stats["strength"] += 1
    #     #     stat_points -= 1
    #     # elif mes == '2':
    #     #     stats["agility"] += 1
    #     #     stat_points -= 1
    #     # elif mes == '3':
    #     #     stats["endurance"] += 1
    #     #     stat_points -= 1
    # else:
    #     update.message.reply_text('В тебе недостатньо скілл поінтів')

    # user_agility = stats["agility"]
    # user_strength = stats["strength"]
    # user_endurance = stats["endurance"]

    # mountin_monster_agility = mountain_monster["agility"]
    # mountin_monster_strength = mountain_monster["strength"]
    # mountin_monster_endurance = mountain_monster["endurance"]
    with open('db.json', 'r') as db:
        info = json.load(db)

    db = info

    name = update.message.from_user.username
    local_stats = {}


    for i in db['users']:
        if i['name'] == name:
            for k in i:
                local_stats[k] = i[k]
 
                
    if energy > 10 and not user_health <= 0:
        words_list.append(update.message.text)
 

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

    # with open('db.json', 'r') as db:
    #     info = json.load(db)
    #
    # for i in info['users']:
    #     if i['name'] == name:
    #         for k in i:
    #             i[k] = local_stats[k]
    #         print(i)

    if local_stats["energy"] > 10:
        yes_list.append(update.message.text)
 
        if mes == "гори":
            local_stats["energy"] -= 15
            update.message.reply_text(f"{name} ти натрапив на {mountain_monster_name}, хочеш втекти ?")

            # if update.message.text != 'гори':
            #     words_list.append(update.message.text)

            # if update.message.text not in words_list:
            #     words_list.append(update.message.text)

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
            if local_stats['strength'] > 5 and local_stats['strength'] < 10 and not mountain_monster[
                                                                                        'health'] <= 0 and user_move == True:
                user_move = False
                damage = random.randint(11, 13)
                chance = random.choices([1, 2], weights=[65, 35], k=1)[0]
                if chance == 1:
                    mountain_monster['health'] = mountain_monster['health'] - damage
                    update.message.reply_text(f'Ти наніс {damage} урону монстру')
                else:
                    update.message.reply_text('Ти промахнувся по монстру')
        elif "Панікувати" in yes_list:
            user_move = True
            if mountain_monster['strength'] >= 33:  # Козел
                moster_damage = random(4, 33)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health = user_health - moster_damage
                    update.message.reply_text(f'(чого ти нажав на цю кнопку??)Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))

            if mountain_monster['strength'] >= 2:  # Троль
                moster_damage = random(2, 12)
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
                moster_damage = random(3, 14)
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
                moster_damage = random(4, 33)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))

                    hp_safe = random[10, 20]
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

            if mountain_monster['strength'] >= 2:  # Троль
                moster_damage = random(2, 12)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    hp_safe = random[
                        10, 20]  # було б класно якщо захист можна було робити в процентах до урону відповідного монстра
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

            if mountain_monster['strength'] >= 3:  # Ящір
                moster_damage = random(3, 14)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                if chance == 1:
                    user_health -= moster_damage
                    update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
                    update.message.reply_photo(
                        photo=open(
                            r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                            "rb"))
                    hp_safe = random[
                        10, 20]  # було б класно якщо захист можна було робити в процентах до урону відповідного монстра
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

        elif 'Випити зілля' in yes_list:
            user_move = True
            if mountain_monster['strength'] >= 330:  # Козел
                moster_damage = random(40, 330)
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

            if mountain_monster['strength'] >= 20:  # Троль
                moster_damage = random(2, 12)
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

            if mountain_monster['strength'] >= 30:  # Ящір
                moster_damage = random(3, 14)
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

        elif mes == "ліс":
            update.message.reply_text(f"{name} ти натрапив на {forest_monster_name}!")
            energy -= 15
            # num = stats["agility"] // forest_monster["agility"]
            # stats["strength"] * num
            # forest_monster["endurancce"] - stats["strength"]

            # num = forest_monster["agility"] // stats["agility"]
            # stats["strength"] * num
            # stats["endurance"] - forest_monster["strength"]

            # if stats['endurance'] == 0:
            #     update.message.reply_text("Ви програли.")
            # elif forest_monster['endurance'] == 0:
            #     update.message.reply_text("Ви виграли!")
        elif mes == 'місто':
            city_buttons = [
                [
                    KeyboardButton('Піти до церкви')
                ]   
            ]
            button = ReplyKeyboardMarkup(city_buttons)
            update.message.reply_text('Ви прибули в місто, що хочете робити?', reply_markup = button)
        if 'Піти до церкви' in words_list:
            words_list = []
            church_buttons = [
                [
                    KeyboardButton('Помолитись')
                ]
            ]
            update.message.reply_text('Вибери що будеш робити?', reply_markup = ReplyKeyboardMarkup(church_buttons))
        elif 'Помолитись' in words_list:
            words_list = []
            buff = random.choice('health', 'strength')
            text = ''
            if buff == 'health':
                text = "+ 10 до здоров'я"
                buffed_health = local_stats['health'] + 10
                new_stats = local_stats
                for i in db['users']:
                    if i['name'] == name:
                        for k in i:
                            new_stats['health'] = buffed_health
                
                with open('db.json', 'w') as db:
                    json.dump(new_stats)
            else:
                local_stats['strength'] = local_stats['strength'] + 5
                text = '+ 5 до сили'
            update.message.reply_text(f'Ти помолився й отримав бафф: {text}')
        elif 'так' in words_list: 
            words_list = []
            update.message.reply_text('Ти втік з гір')
            mountain_monster = random.choice(mountains)
        elif 'ні' in words_list:
            words_list = []
            fight_menu = [
                [
                    KeyboardButton('Атакувати'),
                    KeyboardButton('Захищатись')
                    # KeyboardButton('Випити зілля')
                ]   
            ]
            update.message.reply_text('Ти почав бій! Що будеш робити?', reply_markup = ReplyKeyboardMarkup(fight_menu))
        
        elif 'Атакувати' in words_list:
            words_list = []
            
            if local_stats['strength'] > 1 and local_stats['strength'] < 5 and not mountain_monster['health']  <= 0 and user_move == True:
                user_move = False
                damage = random.randint(6, 8)
                chance = random.choices([1, 2], weights = [65, 35], k = 1)[0] #якесь к1

            elif local_stats['strength'] > 5 and local_stats['strength'] < 10 and not mountain_monster['health']  <= 0 and user_move == True:
                user_move = False
                damage = random.randint(9, 13)
                chance = random.choices([1, 2], weights = [65, 35], k = 1)[0] #якесь к1
            
            elif local_stats['strength'] > 10 and local_stats['strength'] < 17 and not mountain_monster['health']  <= 0 and user_move == True:
                user_move = False
                damage = random.randint(15, 22)
                chance = random.choices([1, 2], weights = [65, 35], k = 1)[0] #якесь к1

            elif local_stats['strength'] > 20 and not mountain_monster['health']  <= 0 and user_move == True:
                user_move = False
                damage = random.randint(int(local_stats['health'] / 1.5), int(local_stats['health'] / 1.5) + 7)
                chance = random.choices([1, 2], weights = [65, 35], k = 1)[0] #якесь к1
            if chance == 1:
                mountain_monster['health'] = mountain_monster['health'] - damage
                update.message.reply_text(f'Ти наніс {damage} урону монстру')
            else:
                update.message.reply_text('Ти промахнувся по монстру')

            user_move = True
            if mountain_monster['strength'] >= 33:              #Козел
                moster_damage = random.randint(12, 17)
                monster_chance = random.choices([1, 2], weights = [75, 25], k = 1)[0] #якесь к1

            if mountain_monster['strength'] >= 2:  # Троль
                moster_damage = random.randint(5, 12)
                monster_chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1

            if mountain_monster['strength'] >= 3:  # Ящір
                moster_damage = random.randint(3, 7)
                monster_chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1

            if monster_chance == 1:
                user_health = user_health - moster_damage
                update.message.reply_text(
                    f'Монстр наніс тобі {moster_damage}!')
                # update.message.reply_photo(
                #     photo=open(
                #         r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
                    #         "rb"))
            else:
                update.message.reply_text('Монстр промахнувся по тобі!')
        elif 'Захищатись' in words_list:
            words_list = []
            user_move = False
            if mountain_monster['strength'] >= 33:              #Козел
                moster_damage = random.randint(12, 17)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                hp_safe= random.randint(10,20)
                

            elif mountain_monster['strength'] >= 2:              #Троль
                moster_damage = random.randint(2, 12)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                hp_safe = random.randint(3,7)

            elif mountain_monster['strength'] >= 3:              #Ящір
                moster_damage = random.randint(3, 14)
                chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
                hp_safe = random.randint(4, 9) #було б класно якщо захист можна було робити в процентах до урону відповідного монстра

            if chance == 1:
                user_health -= moster_damage
                update.message.reply_text(f'Твій захист не спрацював, монстр наніс тобі {moster_damage}!')
                # update.message.reply_photo(
                #     photo=open(
                #         r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg","rb"))   
            else:   
                user_health2 = user_health + hp_safe
                past_hp = user_health + moster_damage

                moster_dmg_safe= past_hp - user_health2
                update.message.reply_text(f'Тобі вдалося захиститись і монстр наніс лише {moster_dmg_safe} урону')
        # ._.
    else:
        update.message.reply_text('У вас недостатньо енергії')
        
        # elif 'Випити зілля' in words_list:
        #     words_list = []
        #     user_move = True
        #     if mountain_monster['strength'] >= 33:              #Козел
        #         moster_damage = random.randint(33, 40)
        #         chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
        #         if chance == 1:
        #             user_health -= moster_damage
        #             update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
        #             # update.message.reply_photo(
        #             #     photo=open(
        #             #         r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg","rb"))
        #             hp_safe =  random.randint(10,20)
        #             user_health =user_health+ hp_safe

        #             update.message.reply_text(f'ти відновив{hp_safe} хп')

        #     elif mountain_monster['strength'] >= 2:  # Троль
        #         moster_damage = random.randint(2, 12)
        #         chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
        #         if chance == 1:
        #             user_health -= moster_damage
        #             update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
        #             # update.message.reply_photo(
        #             #     photo=open(
        #             #         r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
        #             #         "rb"))
        #             hp_safe =  random.randint(10, 20)
        #             user_health = user_health + hp_safe

        #             update.message.reply_text(f'ти відновив{hp_safe} хп')

        #     elif mountain_monster['strength'] >= 3:  # Ящір
        #         moster_damage = random.randint(3, 14)
        #         chance = random.choices([1, 2], weights=[75, 25], k=1)[0]  # якесь к1
        #         if chance == 1:
        #             user_health -= moster_damage
        #             update.message.reply_text(f'Монстр наніс тобі {moster_damage}!')
        #             update.message.reply_photo(
        #                 photo=open(
        #                     r"C:\Users\User\Pictures\Saved Pictures\зображення_viber_2022-11-27_02-51-33-096.jpg",
        #                     "rb"))
        #             hp_safe =  random.randint(10, 20)
        #             user_health = user_health + hp_safe

        #             update.message.reply_text(f'ти відновив{hp_safe} хп')

    if mountain_monster['health'] <= 0:
        user_move = True
        mountain_monster = random.choice(mountains)
        user_health = 40
        energy = 100
        Goat = {"strength": 33, "agility": 3, "endurance": 2, 'health': 10}
        Trol = {"strength": 2, "agility": 1, "endurance": 2, 'health': 25}
        Lizzard = {"strength": 3, "agility": 2, "endurance": 3, 'health': 20}
        user_health = 40
        energy = 100
        update.message.reply_text('Ти виграв битву!', reply_markup = ReplyKeyboardRemove())
        

    elif user_health <= 0:
        user_move = True
        user_health = 40
        Goat = {"strength": 33, "agility": 3, "endurance": 2, 'health': 10}
        Trol = {"strength": 2, "agility": 1, "endurance": 2, 'health': 25}
        Lizzard = {"strength": 3, "agility": 2, "endurance": 3, 'health': 20}
        mountain_monster = random.choice(mountains)
        energy = 100
        update.message.reply_text('Ти програв битву! Чекай поки тебе знайдуть шахтарі', reply_markup = ReplyKeyboardRemove())
        
        # ._.
    else:
        update.message.reply_text('У вас недостатньо енергії')

 

def add_points(update, context):
        with open('db.json', 'r') as db:
            info = json.load(db)

        name = update.message.from_user.username
        local_stats = {}

        # for i in info['users']:
        #     print(i)
        #     if i['name'] == name:
        #         [local_stats] = info['users'][i]
        #         print(local_stats)

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
 
    if answer == '1':
        with open('music/skyrim.mp3', 'rb') as music:
            sound = music.read()
        query.message.reply_voice(sound)
    elif answer == '2':
        with open('music/inn.mp3', 'rb') as inn:
            bw = inn.read()
        query.message.reply_voice(bw)

    # update.message.reply_text('hello11deadaf')
 

#     def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):

#         menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
#         if header_buttons:
#             menu.insert(0, header_buttons)
#         if footer_buttons:
#             menu.append(footer_buttons)
#         return menu

#     if energy > 10:
#         button_list = []
#         lis_horu = ["ліс", "гори"]

#         for i in lis_horu:
#             button_list.append(InlineKeyboardButton(i, callback_data=i))
#             reply_markup = InlineKeyboardMarkup(
#                 build_menu(button_list, n_cols=1))  # n_cols = 1 is for single column and mutliple rows
#         update.message.reply_text('Куди ви хочете піти подорожувати сьогодні? ', reply_markup=reply_markup)

#     def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):

#         menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
#         if header_buttons:
#             menu.insert(0, header_buttons)
#         if footer_buttons:
#             menu.append(footer_buttons)
#         return menu

#     if energy > 10:
#         button_list = []
#         lis_horu = ["ліс", "гори"]

#         for i in lis_horu:
#             button_list.append(InlineKeyboardButton(i, callback_data=i))
#             reply_markup = InlineKeyboardMarkup(
#                 build_menu(button_list, n_cols=1))  # n_cols = 1 is for single column and mutliple rows
#         update.message.reply_text('Куди ви хочете піти подорожувати сьогодні? ', reply_markup=reply_markup)

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

    # dp.add_handler(CallbackQueryHandler(callback))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    print('Bot is started')
