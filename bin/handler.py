#coding=utf-8

from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from .voto import Voto


class Handler:

    def start(self, bot, update):

        msg = "Bienvenido. Para iniciar tu voto pulsa el botón de abajo."

        keyboard = [[InlineKeyboardButton("VOTAR ✉️", callback_data="iniciar_voto")]]

        update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(keyboard))



    def InlinekeyboardCallback(self, bot, update):
        data = update.callback_query.data

        if data == "iniciar_voto":
            bot.answer_callback_query(update.callback_query.id, "OK")
            Voto().iniciarVoto(update.callback_query.from_user.id)
            Voto().mensajeVotar(bot, update)
        else:
            bot.answer_callback_query(update.callback_query.id, data)