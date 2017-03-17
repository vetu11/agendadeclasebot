#coding=utf-8

import logging, json
from bin import Handler, Voto
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

TOKEN = "257284566:AAEqmUh-D5isX1hAa_z9K7B8NLPTmotbXWU"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


"""LEER LOS VOTOS DESDE EL ARCHIVO"""
Voto().leerVotos() # LEEMOS LOS VOTOS GUARDADOS ANTERIORMENTE


"""DECLARANDO HANDLERS"""
handler = CommandHandler("start", Handler().start)
dispatcher.add_handler(handler)

handler = CallbackQueryHandler(Handler().InlinekeyboardCallback)
dispatcher.add_handler(handler)

del handler



"""INICIAR BOT"""
updater.start_polling()


"""CONSOLA"""
while True:

    input = raw_input(">")

    if input == "stop":
        Voto().guardarVotos()

        print "APAGANDO BOT..."
        updater.stop()
        print "BOT APAGADO"

        break

    elif input == "guardar":
        Voto().guardarVotos()