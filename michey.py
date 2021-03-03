from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


TOKEN = '1629080653:AAF3owQ5LrMnnXhVyCItug29-YBfIMn35Nk'


def main():
    updater = Updater(token=TOKEN)    # объект, который ловит сообщения из телеграм

    dispatcher = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)   # отфильтровываем сообщения: теперь устройство должно реагировать
    start_handler = CommandHandler('start', do_start)
    info_handler = CommandHandler('info', do_info)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text(text='??')

def do_start(update: Update, context):
    update.message.reply_text(text="Я тебя знаю?")

def do_info(update: Update, context):
    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    update.message.reply_text(text=f'{name}, сейчас узнаю кто ты.\nКстати твой id: {user_id} ')

main()






