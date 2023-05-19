import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot("5623955667:AAE8-3yEPBReHCjBUOqYaGSo6vx9JgGrkfY")

# Define inline keyboard buttons
first_button = telebot.types.InlineKeyboardButton("رهن و اجاره", callback_data="rent")
second_button = telebot.types.InlineKeyboardButton("خرید", callback_data="buy")
markup_hello = telebot.types.InlineKeyboardMarkup(row_width=2)
markup_hello.add(first_button, second_button)

building_type_first_button = telebot.types.InlineKeyboardButton("آپارتمان", callback_data="apartment")
building_type_second_button = telebot.types.InlineKeyboardButton("ویلا", callback_data="villa")
markup_building_type = telebot.types.InlineKeyboardMarkup(row_width=2)
markup_building_type.add(building_type_first_button, building_type_second_button)

city_first_button = telebot.types.InlineKeyboardButton("تهران", callback_data="tehran-province")
city_second_button = telebot.types.InlineKeyboardButton("البرز", callback_data="alborz-province")
city_third_button = telebot.types.InlineKeyboardButton("اصفحان", callback_data="isfahan-province")
city_4th_button = telebot.types.InlineKeyboardButton("فارس", callback_data="fars-province")
city_5th_button = telebot.types.InlineKeyboardButton("خراسان رضوی", callback_data="khorasan-razavi-province")
city_6th_button = telebot.types.InlineKeyboardButton("آدربایجان شرقی", callback_data="azarbaijan-east-province")
city_7th_button = telebot.types.InlineKeyboardButton("آذربایجان غربی", callback_data="azerbaijan-west-province")
city_8th_button = telebot.types.InlineKeyboardButton("اردبیل", callback_data="ardabil-province")
city_9th_button = telebot.types.InlineKeyboardButton("ایلام", callback_data="ilam-province")
city_10th_button = telebot.types.InlineKeyboardButton("بوشهر", callback_data="bushehr-province")
city_11th_button = telebot.types.InlineKeyboardButton("چهارمحال بختیاری", callback_data="chahar-mahaal-and-bakhtiari-province")
city_12th_button = telebot.types.InlineKeyboardButton("خراسان جنوبی", callback_data="khorasan-south-province")
city_13th_button = telebot.types.InlineKeyboardButton("خراسان شمالی", callback_data="khorasan-north-province")
city_14th_button = telebot.types.InlineKeyboardButton("خوزستان", callback_data="khuzestan-province")
city_15th_button = telebot.types.InlineKeyboardButton("زنجان", callback_data="zanjan-province")
city_16th_button = telebot.types.InlineKeyboardButton("سمنان", callback_data="semnan-province")
city_17th_button = telebot.types.InlineKeyboardButton("یزد", callback_data="yazd-province")
city_18th_button = telebot.types.InlineKeyboardButton("قزوین", callback_data="qazvin-province")
city_19th_button = telebot.types.InlineKeyboardButton("قم", callback_data="qom")
city_20th_button = telebot.types.InlineKeyboardButton("کردستان", callback_data="kurdistan-province")
city_21th_button = telebot.types.InlineKeyboardButton("کرمان", callback_data="kerman-province")
city_22th_button = telebot.types.InlineKeyboardButton("کرمانشاه", callback_data="kermanshah-province")
city_23th_button = telebot.types.InlineKeyboardButton("کهگلویه و بویراحمد", callback_data="kohgiluyeh-and-boyer-ahmad-province")
city_24th_button = telebot.types.InlineKeyboardButton("گلستان", callback_data="golestan-province")
city_25th_button = telebot.types.InlineKeyboardButton("گیلان", callback_data="gilan-province")
city_26th_button = telebot.types.InlineKeyboardButton("لرستان", callback_data="lorestan-province")
city_27th_button = telebot.types.InlineKeyboardButton("مازندران", callback_data="mazandaran-province")
city_28th_button = telebot.types.InlineKeyboardButton("مرکزی", callback_data="markazi-province")
city_29th_button = telebot.types.InlineKeyboardButton("هرمزگان", callback_data="hormozgan-province")
city_30th_button = telebot.types.InlineKeyboardButton("همدان", callback_data="hamadan-province")
city_31th_button = telebot.types.InlineKeyboardButton("سیستان و بلوچستان", callback_data="sistan-and-baluchestan-province")

markup_province = telebot.types.InlineKeyboardMarkup(row_width=2)
markup_province.add(city_first_button, city_second_button, city_third_button, city_4th_button, city_5th_button, city_6th_button, city_7th_button, city_8th_button, city_9th_button, city_10th_button, city_11th_button, city_12th_button, city_13th_button, city_14th_button, city_15th_button, city_16th_button, city_17th_button, city_18th_button, city_19th_button, city_20th_button, city_21th_button,city_22th_button, city_23th_button, city_24th_button, city_25th_button, city_26th_button, city_27th_button, city_28th_button, city_29th_button, city_30th_button, city_31th_button)

# Define global variables
rent_or_buy = None
building_type = None
province = None

# Define callback query handler function
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    global rent_or_buy, building_type, province
    
    if call.data == 'rent':
        bot.send_message(call.message.chat.id, 'چجور خونه‌ای می‌خوای اجاره کنی؟', reply_markup=markup_building_type)
        rent_or_buy = 'rent'
    
    elif call.data == 'buy':
        bot.send_message(call.message.chat.id, 'چجور خونه‌ای می‌خوای بخری؟', reply_markup=markup_building_type)
        rent_or_buy = 'buy'
    
    elif call.data == 'apartment':
        building_type = 'apartment'
        bot.send_message(call.message.chat.id, 'تو کدوم استان؟', reply_markup=markup_province)
    
    elif call.data == 'villa':
        building_type = 'villa'
        bot.send_message(call.message.chat.id, 'تو کدوم استان؟', reply_markup=markup_province)

    elif call.data == 'tehran-province':
        province = 'tehran-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )

    elif call.data == 'alborz-province':
        province = 'alborz-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'isfahan-province':
        province = 'isfahan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'fars-province':
        province = 'fars-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'khorasan-razavi-province':
        province = 'khorasan-razavi-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'azarbaijan-east-province':
        province = 'azarbaijan-east-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'azerbaijan-west-province':
        province = 'azerbaijan-west-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'ardabil-province':
        province = 'ardabil-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'ilam-province':
        province = 'ilam-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'bushehr-province':
        province = 'bushehr-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'chahar-mahaal-and-bakhtiari-province':
        province = 'chahar-mahaal-and-bakhtiari-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'khorasan-south-province':
        province = 'khorasan-south-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'khorasan-north-province':
        province = 'khorasan-north-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'khuzestan-province':
        province = 'khuzestan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'zanjan-province':
        province = 'zanjan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'semnan-province':
        province = 'semnan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'yazd-province':
        province = 'yazd-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'qazvin-province':
        province = 'qazvin-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'qom':
        province = 'qom'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'kurdistan-province':
        province = 'kurdistan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'kerman-province':
        province = 'kerman-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'kermanshah-province':
        province = 'kermanshah-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'kohgiluyeh-and-boyer-ahmad-province':
        province = 'kohgiluyeh-and-boyer-ahmad-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'golestan-province':
        province = 'golestan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'gilan-province':
        province = 'gilan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'lorestan-province':
        province = 'lorestan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'mazandaran-province':
        province = 'mazandaran-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'markazi-province':
        province = 'markazi-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'hormozgan-province':
        province = 'hormozgan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst ) 
    elif call.data == 'hamadan-province':
        province = 'hamadan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )
    elif call.data == 'sistan-and-baluchestan-province':
        province = 'sistan-and-baluchestan-province'
        web_scraper_response = web_scraper(province, rent_or_buy, building_type)
        for item in web_scraper_response :
            if rent_or_buy == 'rent':
                print_lst = item[0] + '\n' + "ودیعه:" + item[1] + '\n' + "اجاره:" + item[2] + '\n' + item[3]
            if rent_or_buy == 'buy':
                print_lst = item[0] + '\n' + "قیمت:" + item[1] + '\n' + item[3]

            bot.send_message(call.message.chat.id, print_lst )


def web_scraper(province, rent_or_buy, building_type):
    province_0 = province
    rent_or_buy_0 = rent_or_buy
    building_type_0 = building_type
    html_text = requests.get(f'https://divar.ir/s/{province_0}/{rent_or_buy_0}-{building_type_0}').text
    soup = BeautifulSoup(html_text, 'lxml')
    ad_list = []

    def preprocess(soup):
        ads = soup.find_all('div', class_='post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46')
        for item in ads:
            title = item.find('h2', class_='kt-post-card__title').text
            parent = item.find('div', class_='kt-post-card__description')
            deposit = parent.text.split()[-2]
            if deposit == 'ودیعه:':
                deposit = ""
            rent = parent.next_sibling.text.split()[-2]
            if rent == 'اجاره:' or rent == 'رهن':
                rent = ""
            link = 'https://divar.ir' + item.a['href']

            ad = [title, deposit, rent, link]
            ad_list.append(ad)
        return ad_list
    response = preprocess(soup)
    return response 


# Define message handler function
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "سلام")
    bot.send_message(message.chat.id, "می‌خوای خونه بخری یا اجاره کنی؟", reply_markup=markup_hello)

# Start the bot
bot.infinity_polling()