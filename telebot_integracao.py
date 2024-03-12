import telebot
from telebot import types

bot = telebot.TeleBot("token")

conversation_state = {}


@bot.message_handler(regexp='^sair$')
def sair(message):
    bot.send_message(chat_id=message.chat.id, text="Acabando o fluxo")


@bot.message_handler(regexp='^9$')
def voltar_menu(message):
    bot.send_message(chat_id=message.chat.id, text="voltando para o menu")


@bot.message_handler(func=lambda message: True)
def demanda_atendida(message):
    bot.send_message(chat_id=message.chat.id, text="Sua demanda foi atendida?\nDigite 1 - Sim\nDigite 2 - Não")

    match message.text:
        case "1":
            bot.send_message(chat_id=message.chat.id,
                             text="Agradecemos o seu contato e continuamos à disposição!Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/")
        case "2":
            voltar_menu(message)


bot.infinity_polling()