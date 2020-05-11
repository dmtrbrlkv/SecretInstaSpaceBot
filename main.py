import telebot
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname).1s %(message)s', datefmt='%Y.%m.%d %H:%M:%S')
logging.info(f"Start")

bot = telebot.TeleBot(os.environ.get("TG_TOKEN"))

line = "\n\n"
secret_space = "\n⠀\n"


@bot.message_handler(commands=['start'])
def start(message):
    logging.info(f"Start by {message.chat.id}")
    bot.send_message(message.chat.id, "Пришлите сообщение, бот пришлет в ответ отредактированный текст")


@bot.message_handler(content_types=['text'])
def send_text(message):
    logging.info(f"Text by {message.chat.id}")
    text = message.text
    text = text.replace(line, secret_space)
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
logging.info(f"Stop")
