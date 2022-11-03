import telebot
from dotenv import dotenv_values


#* Take environment variables from .env
config = dotenv_values(".env")

bot = telebot.TeleBot(config.get('TELEGRAM_BOT_TOKEN'));

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  with open('./request.json', 'a+', encoding='utf-8') as reqf:
    reqf.write('''
               request: {message}
               '''.format(message=message))