import telebot

bot = telebot.TeleBot("5906211167:AAFG-i9_ljPz_HR6Pwb_5uCfruU4ROmQt8M")

first_button = telebot.types.InlineKeyboardButton("Button 1", url = "https://t.me/wasted_food_0")
second_button = telebot.types.InlineKeyboardButton("Button 2", callback_data="Hi!")

markup_hello = telebot.types.InlineKeyboardMarkup(row_width=1)

markup_hello.add(first_button, second_button)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    bot.answer_callback_query(call.id, "You clicked on hi!", show_alert=True)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi", reply_markup = markup_hello)

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key_markup.add("One", "Two", "Three")

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, "What can i do?", reply_markup = key_markup)

@bot.message_handler()
def keyboard(message):
    if message.text == "One":
        bot.send_message(message.chat.id, "You tapped on the first button.")
    elif message.text == "Two":
        bot.send_message(message.chat.id, "You tapped on the second button.")
    elif message.text == "Three":
        bot.send_message(message.chat.id, "You tapped on the third button.")








import telebot
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

bot = telebot.TeleBot("5906211167:AAFG-i9_ljPz_HR6Pwb_5uCfruU4ROmQt8M")

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key_markup.add("calculate BMI","weight chart")

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "What can i do?", reply_markup = key_markup)

@bot.message_handler(func=lambda m: True)
def info(message):
    global x_current_date
    if message.text == "calculate BMI":
        msg = bot.send_message(message.chat.id, "Enter your weight in kg")
        bot.register_next_step_handler(msg, weight)
    elif message.text == "weight chart":
        xpoints = np.array([1, 2, 6, 8])
        ypoints = np.array([3, 8, 1, 10])
        plt.plot(ypoints, marker='o')
        bot.send_photo(message.chat.id, plt.savefig('foo.png'))
def weight(message):
    global wit
    wit = float(message.text)
    msg = bot.reply_to(message, "Enter your height in centimeter")
    bot.register_next_step_handler(msg, height)

def height(message):
    global hit, current_date
    hit = float(message.text)
    bmi = wit*10000 / (hit*hit)
    if (bmi < 18.5):
        health_condition = "underweight"
    elif ( bmi >= 18.5 and bmi < 24.9):
        health_condition = "healthy"
    elif ( bmi >= 24.9 and bmi < 30):
        health_condition = "overweight"
    elif ( bmi >=30):
        health_condition = "suffering from Obesity"
    now = datetime.datetime.now()
    current_date = now.strftime("%Y/%m/%d")
    bot.send_message(message.chat.id, f"your BMI is: {round(bmi, 2)}\n \nYou are {health_condition}")

bot.infinity_polling()