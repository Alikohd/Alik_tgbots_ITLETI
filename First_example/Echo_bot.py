from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

TOKEN = ""  # Токен бота
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello world!")
    print(context.args)


def text(update, context):
    txt = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt)


start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.all, text)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()
