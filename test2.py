from telegram.ext import *
import json
import random


"Dymu_moi": {"strenght": 257765, "agility": 3, "endurance": 6}




mountains= "Козел","Троль","Ящір"

Goat = {"strength":33,"agility":3,"endurance":2}
Trol = {"strength":2,"agility":1,"endurance":2}
Lizzard = {"strength":3,"agility":2,"endurance":3}
mountain_monster=(random.choice(mountains))

forest = "Орк","Вовк","Кабани"

Ork = {"strength":2,"agility":4,"endurance":12}
Wolf = {"strength":1,"agility":1,"endurance":2}
Kaban = {"strength":3,"agility":4,"endurance":1}
forest_monster=(random.choice(forest))

stats = {'strenght': random.randint(1, 5), 'agility': random.randint(2, 7), 'endurance': random.randint(1, 9)}

def map(update, context):
    name = update.message.from_user.username
    mes = update.message.text

    if mes == "гори":
        update.message.reply_text(f"{name}ти натрапив на{mountain_monster}, хочеш втекти ?")

        num = stats["agility"] // mountain_monster["agility"]
        stats['strenght'] * num
        mountain_monster["endurancce"] -= stats["strenght"]

        num = mountain_monster["agility"] // stats["agility"]
        stats["strenght"] * num
        stats["endurance"] -= mountain_monster["strenght"]
        def final(update, context):
            if stats['endurance'] == 0:
                update.message.reply_text("Ви програли.")
            elif mountain_monster['endurance'] == 0:
                update.message.reply_text("Ви виграли!")


    elif mes == "ліс":
        update.message.reply_text(f"{name}ти натрапив на{forest_monster}!")
        num = stats["agility"] // forest_monster["agility"]
        stats['strenght'] * num
        forest_monster["endurancce"] -= stats["strenght"]

        num = forest_monster["agility"] // stats["agility"]
        stats["strenght"] * num
        stats["endurance"] -= forest_monster["strenght"]
        def final2(update, context):
            if stats['endurance'] == 0:
                update.message.reply_text("Ви програли.")
            elif forest_monster['endurance'] == 0:
                update.message.reply_text("Ви виграли!")

    else:
       update.message.reply_text('Помилка')


def location(update, context,):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Куди ви хочете піти подорожувати сьогодні? Ліс/Гори')


