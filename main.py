import requests
import telebot
import pyowm

BOT_TOKEN = '2015552107:AAH5k9rSHLq-p7utOJoMfFLTLvSSyffKfH0'
bot = telebot.TeleBot(BOT_TOKEN)

PRIVATBANK_API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
response = requests.get(PRIVATBANK_API).json()[0]
owm = pyowm.OWM('0fdcac5a6f22992894a40f9f64c50f80')


@bot.message_handler(commands=['hello'])
def hello_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hello')
    bot.send_message(chat_id, 'Would you like to know the weather or the USD exchange rate?')

@bot.message_handler(content_types=['text'])
def handler_text(message):
    text = message.text
    chat_id = message.chat.id
    print('TEXT_FROM_USER - ', text)
    if text == 'usd':
        bot.send_message(chat_id, 'Dollar exchange rate today: {} / {}.'.format(
        response['buy'], response['sale']))

    elif text == 'weather':
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Which city?')
        city = input()
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        bot.send_message(chat_id, "In " + city + "now " + str(temp) + "C") 

bot.polling()
