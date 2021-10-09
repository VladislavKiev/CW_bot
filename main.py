import requests
import telebot
import pyowm  #1
# import os  #1
import time #1

PRIVATBANK_API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
response = requests.get(PRIVATBANK_API).json()[0]

owm = pyowm.OWM('0fdcac5a6f22992894a40f9f64c50f80')

BOT_TOKEN = '2015552107:AAH5k9rSHLq-p7utOJoMfFLTLvSSyffKfH0'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['hello'])
def hello_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hello')
    bot.send_message(chat_id, 'Would you like to know the weather or the USD exchange rate?')

@bot.message_handler(content_types=['text'])
def hendler_text(message):
    text = message.text
    chat_id = message.chat.id
    print('TEXT_FROM_USER - ', text)
    if text == 'usd':
        bot.send_message(chat_id, 'Dollar exchange rate today: {} / {}.'.format(
        response['buy'], response['sale']
    ))

#     elif text == 'weather':
#         bot.send_message(message.from_user.id, "Enter the name of the city")
#         observation = owm.weather_at_place(message.text)
#         weather = observation.get_weather()
#         temp = weather.get_temperature("celsius")["temp"]
#         temp = round(temp)
#         print(time.ctime(), "User id:", message.from_user.id)
#         print(time.ctime(), "Message:", message.text.title(), temp, "C", weather.get_detailed_status())
#         answer = "In " + message.text.title() + " now " + weather.get_detailed_status() + "." + "\n"
#         answer += "current temperatre: " + str(temp) + " С" + "\n\n"
#         # place = input('В каком городе/стране?')
#         # observation = owm.weather_manager().weather_at_place(place)
#         # w = observation.weather
#         # print(w)
#
# bot.polling()
