import telebot
import requests
import json

BOT_TOKEN = '1830001814:AAGTh81pmrKyYlelAblAeu5MfcLjkm-s0ZE'

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['btc'])
def handle_massage(message):
   response = requests.get('https://blockchain.info/ru/ticker')
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    bot.reply_to(message, str("BTC/USD: " + str(parsed_string["USD"]["last"])))
   else:
    bot.reply_to(message, 'Can not access to blockchain.info')

@bot.message_handler(commands=['near'])
def handle_massage(message):
   response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=NEAR&tsyms=USD', {
  'auth': {
    'user': 'kirillchernov01',
    'pass': '6ae9562c140c794e0fa249394391df6c2738c83b5987902a1353499933d06d8f'
  }
})
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    bot.reply_to(message, str("NEAR/USD: " + str(parsed_string["USD"])))
   else:
    bot.reply_to(message, 'Can not access to min-api.cryptocompare.com')

@bot.message_handler(commands=['eth'])
def handle_massage(message):
   response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD', {
  'auth': {
    'user': 'kirillchernov01',
    'pass': '6ae9562c140c794e0fa249394391df6c2738c83b5987902a1353499933d06d8f'
  }
})
   if response.status_code == 200:
    parsed_string = json.loads(response.text)
    bot.reply_to(message, str("ETH/USD: " + str(parsed_string["USD"])))
   else:
    bot.reply_to(message, 'Can not access to min-api.cryptocompare.com')

@bot.message_handler(commands=['start'])
def handle_massage(message):
    bot.reply_to(message, 'Привет, юзер!')
   
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