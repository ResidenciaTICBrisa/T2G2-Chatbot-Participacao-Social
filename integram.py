import telebot
import dotenv
import os

dotenv.load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(token)
index_function = 0


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global index_function
    id_chat = message.chat.id
    bot.send_message(id_chat,
                     "Bem-vindo(a) ao atendimento virtual do Brasil Participativo. Para começar, "
                     "diga-nos o seu nome")
    index_function = -1


@bot.message_handler(func=lambda message: not message.text.isdigit() and index_function == -1 and message.text)
def send_greeting(message):
    global index_function
    id_chat = message.chat.id
    bot.send_message(id_chat, f"Olá, {message.text}. Digite o número que corresponde à opção que deseja acessar. "
                              f"Caso queira encerrar o atendimento, digite 'sair' a qualquer momento")
    bot.send_message(message.chat.id, "Digite 1 - O que é o Brasil Participativo?\n" +
                     "Digite 2 - Processos Participativos\n" +
                     "Digite 3 - Dificuldade de acesso\n" +
                     "Digite 4 - Represento um órgão da Administração Pública Federal\n" +
                     "Digite 5 - Sou da imprensa\n" +
                     "Digite 6 - Perguntas Frequentes\n" +
                     "Digite 7 - Outros Assuntos\n")
    index_function = 0


# primeiro bloco de perguntas
@bot.message_handler(
    func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 7) and index_function == 0)
def handle_messages(message):
    global index_function
    id_chat = message.chat.id
    mensagem_usuario = message.text
    match mensagem_usuario:
        case "1":
            index_function = 1
            bot.send_message(id_chat,
                             "Brasil Participativo é a nova plataforma de participação social do governo federal,"
                             "um espaço para que a população possa contribuir com a criação e melhoria das políticas públicas."
                             "A plataforma é gerenciada pela Secretaria Nacional de Participação Social (SNPS),"
                             "vinculada à Secretaria Geral da Presidência da República (SGPR).Quer saber mais informações?"
                             "Acesse o site https://brasilparticipativo.presidencia.gov.br/")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")


# penultimo bloco de perguntas
@bot.message_handler(
    func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 7) and index_function == 1)
def handle_messages(message):
    global index_function
    id_chat = message.chat.id
    match message.text:
        case "1":
            bot.send_message(id_chat,
                             "Agradecemos o seu contato e continuamos à disposição! Para acompanhar todas "
                             "as atividades realizadas pelo Brasil Participativo, acesse "
                             "https://brasilparticipativo.presidencia.gov.br/")
        case "2":
            index_function = 2
            bot.send_message(id_chat,
                             "Digite 9 - Retornar ao menu anterior ?\nCaso queira encerrar o atendimento, digite “sair”")


# ultimo bloco de perguntas
@bot.message_handler(func=lambda message: message.text == "9" and index_function == 2)
def handle_messages(message):
    global index_function
    id_chat = message.chat.id
    match message.text:
        case "9":
            bot.send_message(message.chat.id, "Digite 1 - O que é o Brasil Participativo?\n" +
                             "Digite 2 - Processos Participativos\n" +
                             "Digite 3 - Dificuldade de acesso\n" +
                             "Digite 4 - Represento um órgão da Administração Pública Federal\n" +
                             "Digite 5 - Sou da imprensa\n" +
                             "Digite 6 - Perguntas Frequentes\n" +
                             "Digite 7 - Outros Assuntos\n")
            index_function = 0


@bot.message_handler(func=lambda message: message.text == "sair")
def handle_messages(message):
    id_chat = message.chat.id
    bot.send_message(id_chat, "Saindo")
    # precisamos ver como encerrar o atendimento


bot.infinity_polling()
