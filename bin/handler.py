#coding=utf-8

from .mensajes import Mensajes
from .voto import Voto


class Handler:

    def start(self, bot, update):
        Mensajes().start(bot, update)


    def InlinekeyboardCallback(self, bot, update):
        data = update.callback_query.data
        idUsuario = update.callback_query.from_user.id

        if data == "iniciar_voto":
            bot.answer_callback_query(update.callback_query.id, "OK")
            Voto().iniciarVoto(idUsuario)
            Voto().mensajeVotar(bot, update)
        elif data.count("-") == 1:
            Voto().actualizarVoto(data, idUsuario)
            Voto().mensajeVotar(bot, update)
        elif data == "enviar_voto":
            Mensajes().votoEnviado(bot, update)