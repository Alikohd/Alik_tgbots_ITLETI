from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Defaults
from telegram import ParseMode
import logging

TOKEN = ""  # Токен бота
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello world!")
    print(context.args)


def media(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Here is your photo/video!')


def audio(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Here is your audio!')


def forward(update, context):
    text = f"<b>{'Here is forwarded photo/video'}</b>"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.HTML)


def links(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Here is your url!')


def number(update, context):
    key = str(context.args[0])
    value = int(context.args[1])
    context.user_data[key] = value


def sums(update, context):
    key1 = str(context.args[0])
    key2 = str(context.args[1])
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(context.user_data[key1] + context.user_data[key2]))


defaults = Defaults(parse_mode=ParseMode.HTML)
forward_handler = MessageHandler(Filters.forwarded & (Filters.video | Filters.photo), forward)
start_handler = CommandHandler('start', start)
audio_handler = MessageHandler(Filters.audio, audio)
media_handler = MessageHandler(Filters.photo or Filters.video, media)
links_handler = MessageHandler(Filters.entity('url'), links)
number_handler = CommandHandler('number', number)
sum_handler = CommandHandler('sum', sums)

dispatcher.add_handler(forward_handler)
dispatcher.add_handler(audio_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(media_handler)
dispatcher.add_handler(links_handler)
dispatcher.add_handler(number_handler)
dispatcher.add_handler(sum_handler)

updater.start_polling()
