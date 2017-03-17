#coding=utf-8

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

class Voto:

    votos = []

    def iniciarVoto(self,idUsuario):

        self.votos.append({"id":idUsuario,
                           "voto":{
                               "1-1":0,"1-2":0,"1-3":0,"1-4":0,
                               "2-1":0,"2-2":0,"2-3":0,"2-4":0,
                               "3-1":0,"3-2":0,"3-3":0,"3-4":0
                           },
                           "votado":[]
                           })

    def mensajeVotar(self, bot, update):

        msg = "Pulsa los botones para votar."

        keyboard = [[InlineKeyboardButton("⏰ / 📆", callback_data=" "),
                     InlineKeyboardButton("Jueves", callback_data=" "),
                     InlineKeyboardButton("Viernes", callback_data=" "),
                     InlineKeyboardButton("Lunes", callback_data=" "),
                     InlineKeyboardButton("Martes", callback_data=" ")],

                    [InlineKeyboardButton("8:00", callback_data=" "),
                     InlineKeyboardButton("0", callback_data="1-1"),
                     InlineKeyboardButton("0", callback_data="1-2"),
                     InlineKeyboardButton("0", callback_data="1-3"),
                     InlineKeyboardButton("0", callback_data="1-4")],

                    [InlineKeyboardButton("10:00", callback_data=" "),
                     InlineKeyboardButton("0", callback_data="2-1"),
                     InlineKeyboardButton("0", callback_data="2-2"),
                     InlineKeyboardButton("0", callback_data="2-3"),
                     InlineKeyboardButton("0", callback_data="2-4")],

                    [InlineKeyboardButton("12:00", callback_data=" "),
                     InlineKeyboardButton("0", callback_data="3-1"),
                     InlineKeyboardButton("0", callback_data="3-2"),
                     InlineKeyboardButton("0", callback_data="3-3"),
                     InlineKeyboardButton("0", callback_data="3-4")],

                    [InlineKeyboardButton("ENVIAR 📤", callback_data="enviar_voto"),
                     InlineKeyboardButton("AYUDA 🆘", url="google.com")]]


        bot.edit_message_text(chat_id = update.callback_query.message.chat_id,
                              message_id = update.callback_query.message.message_id,
                              text = msg,
                              parse_mode = ParseMode.MARKDOWN,
                              reply_markup = InlineKeyboardMarkup(keyboard))
