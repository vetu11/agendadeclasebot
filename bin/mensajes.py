#coding=utf-8

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode


class Mensajes:

    def start(self, bot, update):

        msg = "Bienvenido. Para iniciar tu voto pulsa el botón de abajo."

        keyboard = [[InlineKeyboardButton("VOTAR ✉️", callback_data="iniciar_voto")]]

        update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(keyboard))

    def votoEnviado(self, bot, update):
        query = update.callback_query

        msg = "Gracias por enviar tu voto.\n*RECUERDA:* si tu voto no contiene los 9 examenes será nulo."

        keyboard = [[InlineKeyboardButton("MODIFICAR 🔧️", callback_data="iniciar_voto")]]

        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text=msg,
                              reply_markup=InlineKeyboardMarkup(keyboard),
                              parse_mode=ParseMode.MARKDOWN)