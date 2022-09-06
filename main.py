import telebot
from ticket import ticket

bot = telebot.TeleBot(ticket)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,'Здравствуйте, я бот который будет повторять ваши сообщения.')

@bot.message_handler(content_types=['text'])
def indulgence(message):
    bot.send_message(message.chat.id,message)

bot.polling(none_stop=True)