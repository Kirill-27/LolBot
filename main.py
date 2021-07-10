import telebot
import requests
import json

BOT_TOKEN = '1830001814:AAGTh81pmrKyYlelAblAeu5MfcLjkm-s0ZE'
CRYPTOCOMPARE_USER = 'kirillchernov01'
CRYPTOCOMPARE_PASS = '6ae9562c140c794e0fa249394391df6c2738c83b5987902a1353499933d06d8f'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['cryp'])
def handle_massage(message):
   response = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,NEAR&tsyms=USD')
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    bot.reply_to(message, str("BTC/USD: " + str(parsed_string["BTC"]["USD"]) + "\nNEAR/USD: " + str(parsed_string["ETH"]["USD"]) +"\nETH/USD: " + str(parsed_string["NEAR"]["USD"])))
   else:
    bot.reply_to(message, 'Can not access to min-api.cryptocompare.com')

@bot.message_handler(commands=['news'])
def handle_massage(message):
   response = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN', {
  'auth': {
    'user': CRYPTOCOMPARE_USER,
    'pass': CRYPTOCOMPARE_PASS
  }
})
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    bot.reply_to(message, str(parsed_string["Data"][0]["url"]))
   else:
    bot.reply_to(message, 'Can not access to min-api.cryptocompare.com')

@bot.message_handler(commands=['start'])
def handle_massage(message):
    bot.reply_to(message, 'Привет, юзер! Тут ты можешь узнать актуальный курс крипты к USD и иностранных валют к UAN')
   
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