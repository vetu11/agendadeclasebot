#coding=utf-8

from bin import Handler
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

TOKEN = "257284566:AAEqmUh-D5isX1hAa_z9K7B8NLPTmotbXWU"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher




"""DECLARANDO HANDLERS"""
handler = CommandHandler("start", Handler().start)
dispatcher.add_handler(handler)

handler = CallbackQueryHandler(Handler().InlinekeyboardCallback)
dispatcher.add_handler(handler)

del handler



"""INICIAR BOT"""
updater.start_polling()