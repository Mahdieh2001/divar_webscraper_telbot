import telebot

bot = telebot.TeleBot("5623955667:AAE8-3yEPBReHCjBUOqYaGSo6vx9JgGrkfY")

first_button = telebot.types.InlineKeyboardButton("رهن و اجاره", callback_data="rent")
second_button = telebot.types.InlineKeyboardButton("خرید", callback_data="buy")
markup_hello = telebot.types.InlineKeyboardMarkup(row_width=2)
markup_hello.add(first_button, second_button)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "سلام")
    bot.send_message(message.chat.id, "میخوای خونه بخری یا اجاره کنی؟", reply_markup = markup_hello)

building_type_first_button = telebot.types.InlineKeyboardButton("آپارتمان", callback_data="apartment")
building_type_second_button = telebot.types.InlineKeyboardButton("ویلا", callback_data="villa")
markup_building_type = telebot.types.InlineKeyboardMarkup(row_width=2)
markup_building_type.add(building_type_first_button, building_type_second_button)

@bot.callback_query_handler(func=lambda call: True)
def handle_query_1(call):
    global rent_or_buy
    if call.data == 'rent':
        bot.send_message(call.message.chat.id,  'چجور خونه ای میخوای اجاره کنی؟', reply_markup = markup_building_type)
        rent_or_buy = 'rent'
    elif call.data == 'buy':
        bot.send_message(call.message.chat.id, 'چجور خونه ای میخوای بخری؟', reply_markup = markup_building_type)
        rent_or_buy = 'buy'


@bot.callback_query_handler(func=lambda call: True)
def handle_query_2(call):
    global building_type
    bot.send_message(call.message.chat.id, 'تو کدوم شهر؟')
    if call.data == 'apartment':
        building_type = 'apartment'
    elif call.data == 'villa':
        rent_or_buy = 'villa'


bot.infinity_polling()