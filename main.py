from distutils import command
import imp
from urllib import response
import requests
import telebot
from config import API_bot as apibot
from datetime import datetime


# функция получения стоимости биткоина:
def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    #print(response)                                    #вывод ответа в формате JSON
    sell_price = response["btc_usd"]["sell"]                                    #забираем из JSON-файла цену продажи
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


# функция для бота:
def telegram_bot(apibot):
    bot = telebot.TeleBot(apibot)

    # приветствие пользователя:
    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello, friend! Write the 'price' to find out the cost of BTC!")

    # функция реагирующая на отправленные сообщения:
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                #print(response)                                    #вывод ответа в формате JSON
                sell_price = response["btc_usd"]["sell"]                                    #забираем из JSON-файла цену продажи 
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                )      
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Something was wrong..."
                )
        else:
            bot.send_message(message.chat.id, "Whaaat??? Check the command dude!")

    bot.polling()


if __name__ == '__main__':
    #get_data()
    telegram_bot(apibot)