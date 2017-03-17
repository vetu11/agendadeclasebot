#coding=utf-8

import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

class Voto:

    votos = []

    def leerVotos(self):
        with open("votos.json") as f:
            lista = json.load(f)

            for e in lista:
                self.votos.append(e)
            print self.votos


    def guardarVotos(self):
        print "GUARDANDO..."
        with open("votos.json","w") as f:
            json.dump(self.votos, f, indent=4)
        print "GUARDADO"


    def iniciarVoto(self,idUsuario):

        self.votos.append({"id":idUsuario,
                           "voto":{
                               "1-1":0,"1-2":0,"1-3":0,"1-4":0,
                               "2-1":0,"2-2":0,"2-3":0,"2-4":0,
                               "3-1":0,"3-2":0,"3-3":0,"3-4":0
                           },
                           "votado":[]
                           })


    def finder(self, idUsuario):
        """Esta fución busca el voto del usuario especificado en la lista de votos
         devuelve el indice de posición del mismo en la lista. Devuelve None si no hay ningún voto para el usuario."""

        indice = 0
        for e in self.votos:
            if e["id"] == idUsuario:
                return indice
            indice = indice + 1


    def generarTeclado(self, idUsuario):

        dicc = {0:"⭕️", 1:"1️⃣", 2:"2️⃣", 3:"3️⃣", 4:"4️⃣", 5:"5️⃣", 6:"6️⃣", 7:"7️⃣", 8:"8️⃣", 9:"9️⃣"}

        keyboard =[[InlineKeyboardButton("⏰ \ 📆", callback_data=" "),
                     InlineKeyboardButton("Jueves", callback_data=" "),
                     InlineKeyboardButton("Viernes", callback_data=" "),
                     InlineKeyboardButton("Lunes", callback_data=" "),
                     InlineKeyboardButton("Martes", callback_data=" ")],

                   [InlineKeyboardButton("08:00", callback_data=" ")],

                   [InlineKeyboardButton("10:00", callback_data=" ")],

                   [InlineKeyboardButton("12:00", callback_data=" ")],

                   [InlineKeyboardButton("ENVIAR 📤", callback_data="enviar_voto"),
                    InlineKeyboardButton("AYUDA 🆘", url="google.com")]
                   ]


        posiciones = self.votos[self.finder(idUsuario)]["voto"]

        keyboard[1].append(InlineKeyboardButton(dicc[posiciones["1-1"]], callback_data="1-1"))
        keyboard[1].append(InlineKeyboardButton(dicc[posiciones["1-2"]], callback_data="1-2"))
        keyboard[1].append(InlineKeyboardButton(dicc[posiciones["1-3"]], callback_data="1-3"))
        keyboard[1].append(InlineKeyboardButton(dicc[posiciones["1-4"]], callback_data="1-4"))

        keyboard[2].append(InlineKeyboardButton(dicc[posiciones["2-1"]], callback_data="2-1"))
        keyboard[2].append(InlineKeyboardButton(dicc[posiciones["2-2"]], callback_data="2-2"))
        keyboard[2].append(InlineKeyboardButton(dicc[posiciones["2-3"]], callback_data="2-3"))
        keyboard[2].append(InlineKeyboardButton(dicc[posiciones["2-4"]], callback_data="2-4"))

        keyboard[3].append(InlineKeyboardButton(dicc[posiciones["3-1"]], callback_data="3-1"))
        keyboard[3].append(InlineKeyboardButton(dicc[posiciones["3-2"]], callback_data="3-2"))
        keyboard[3].append(InlineKeyboardButton(dicc[posiciones["3-3"]], callback_data="3-3"))
        keyboard[3].append(InlineKeyboardButton(dicc[posiciones["3-4"]], callback_data="3-4"))

        return keyboard


    def mensajeVotar(self, bot, update):

        msg = "Pulsa los botones para votar."

        keyboard = self.generarTeclado(update.callback_query.from_user.id)


        bot.edit_message_text(chat_id = update.callback_query.message.chat_id,
                              message_id = update.callback_query.message.message_id,
                              text = msg,
                              parse_mode = ParseMode.MARKDOWN,
                              reply_markup = InlineKeyboardMarkup(keyboard))


    def actualizarVoto(self, posicion, idUsuario):
        """Este metodo actualiza el valor de la posición indicada para el voto de la perosna indicada"""

        indVoto = self.finder(idUsuario)

        valorAnterior = self.votos[indVoto]["voto"][posicion]
        valorNuevo = valorAnterior

        while True:
            if valorNuevo == 9:
                valorNuevo = 0  # hacemos overflow
            else:
                valorNuevo = valorNuevo + 1

            if valorNuevo not in self.votos[indVoto]["votado"]:
                self.votos[indVoto]["voto"][posicion] = valorNuevo
                if valorNuevo != 0:
                    self.votos[indVoto]["votado"].append(valorNuevo)
                if valorAnterior in self.votos[indVoto]["votado"]:
                    self.votos[indVoto]["votado"].remove(valorAnterior)
                return True