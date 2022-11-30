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
#         update.message.reply_text(f'Стати юзера: \n💪 Сила: {v["strength"]}, \n🏇 Спритність: {v["agility"]}, \n🛡️ Витривалітсть: {v["endurance"]}')
# if stat_points > 0:
#     update.message.reply_text("У тебе є вільні стат поінти, хочеш їх використати?")
#     user_message = str(text).lower()
#     if user_message in ('так', 'ага'):
#         update.message.reply_text("Що ви хочете підвищити? Введіть номер: 1.Сила, 2.Спритність, 3.Витривалість")
#     if user_message == 1:
#             stats["strength"] += 1
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
#         stats["strength"] += 1
#         stat_points -= 1
#     elif user_message == 2:
#         stats["agility"] += 1
#         stat_points -= 1
#     elif user_message == 3:
#         stats["endurance"] += 1
#         stat_points -= 1
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
#     #         stats['strength'] * num
#     #         mountain_monster["endurancce"] -= stats["strength"]

#     #         num = mountain_monster["agility"] // stats["agility"]
#     #         stats["strength"] * num
#     #         stats["endurance"] -= mountain_monster["strength"]

#     #         if stats['endurance'] == 0:
#     #             update.message.reply_text("Ви програли.")
#     #         elif mountain_monster['endurance'] == 0:
#     #             update.message.reply_text("Ви виграли!")
#     #     # ._.

#     #     elif mes2 == "ліс":
#     #         update.message.reply_text(f"{name} ти натрапив на {forest_monster}!")
#     #         num = stats["agility"] // forest_monster["agility"]
#     #         stats['strength'] * num
#     #         forest_monster["endurancce"] -= stats["strength"]

#     #         num = forest_monster["agility"] // stats["agility"]
#     #         stats["strength"] * num
#     #         stats["endurance"] -= forest_monster["strength"]

#     #         if stats['endurance'] == 0:
#     #             update.message.reply_text("Ви програли.")
#     #         elif forest_monster['endurance'] == 0:
#     #             update.message.reply_text("Ви виграли!")
#     #     # ._.
#     # else:
#     #     update.message.reply_text('У вас недостатньо енергії')
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