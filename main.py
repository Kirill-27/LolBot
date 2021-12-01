import telebot
import requests
import json

BOT_TOKEN = '1830001814:AAGTh81pmrKyYlelAblAeu5MfcLjkm-s0ZE'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['cryp'])
def handle_massage(message):
   response = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BNB,BTC,ETH,NEAR&tsyms=USD')
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    bot.reply_to(message, str("BTC/USD: " + str(parsed_string["BTC"]["USD"]) 
    + "\nETH/USD: " + str(parsed_string["ETH"]["USD"])
    + "\nBNB/USD: " + str(parsed_string["BNB"]["USD"])
    + "\nNEAR/USD: " + str(parsed_string["NEAR"]["USD"])))
   else:
    bot.reply_to(message, 'Can not access to min-api.cryptocompare.com')

@bot.message_handler(commands=['news'])
def handle_massage(message):
   response = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    bot.reply_to(message, str(parsed_string["Data"][0]["url"]))
   else:
    bot.reply_to(message, 'Can not access to min-api.cryptocompare.com')

@bot.message_handler(commands=['start'])
def handle_massage(message):
    bot.reply_to(message, "Привет, юзер! Тут ты можешь узнать актуальный курс крипты к USD\
(для этого используй команды из меню) и иностранных валют к UAN\
(для этого пиши наименование валюты боту)")
   
@bot.message_handler(regexp='лох')
def handle_massage(message):
   bot.reply_to(message, 'сам ты лох!')

@bot.message_handler(content_types=['text'])
def handle_massage(message):
   response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode="+ message.text +"&json")
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    if len(parsed_string) < 1:
        bot.reply_to(message, 'Invalid request.')
    else :
        bot.reply_to(message, str(parsed_string[0]["txt"] + ": " + str(parsed_string[0]["rate"]) + " UAN"))
   else:
    bot.reply_to(message, 'Can not access to NBU.')

bot.polling(timeout=30)
