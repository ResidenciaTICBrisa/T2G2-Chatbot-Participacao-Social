import telebot
import dotenv
import os
from state_machine import StateMachine

# sm = StateMachine("id")   # exemplo de como utilizar
dotenv.load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(token)
sm_dict = {}


def compare(user_id, valor):
    global sm_dict
    if sm_dict[user_id].getstate() == valor:
        return True
    return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global sm_dict
    id_chat = message.chat.id
    bot.send_message(id_chat,
                     "Bem-vindo(a) ao atendimento virtual do Brasil Participativo. Para começar, "
                     "diga-nos o seu nome")
    sm_dict.update({id_chat: StateMachine(id_chat)})
    sm_dict[id_chat].setstate(-1)


@bot.message_handler(func=lambda message: not message.text.isdigit() and compare(message.chat.id, -1) and message.text)
def send_greeting(message):
    global sm_dict
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
    sm_dict[id_chat].setstate(0)


# primeiro bloco de perguntas
@bot.message_handler(
    func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 7) and compare(message.chat.id, 0))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    mensagem_usuario = message.text
    match mensagem_usuario:
        case "1":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,
                             "Brasil Participativo é a nova plataforma de participação social do governo federal,"
                             "um espaço para que a população possa contribuir com a criação e melhoria das políticas públicas."
                             "A plataforma é gerenciada pela Secretaria Nacional de Participação Social (SNPS),"
                             "vinculada à Secretaria Geral da Presidência da República (SGPR).Quer saber mais informações?"
                             "Acesse o site https://brasilparticipativo.presidencia.gov.br/")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "2":
            sm_dict[id_chat].setstate(3)
            bot.reply_to(message,"Digite 1 - Plano Clima/PPA Participativo\n"
                                "Digite 2 - Conferências\n"
                                "Digite 3 - Consultas Públicas\n"
                                "Digite 4 - Enquetes\n"
                                "Digite 5 - Audiências Públicas\n "
                                "Digite 6 - Colegiados")
        case "3":
            sm_dict[id_chat].setstate(1)
            bot.reply_to(message,"Por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br")
            bot.reply_to(message, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "4":
            sm_dict[id_chat].setstate(1)
            bot.reply_to(message,"Para aderir à plataforma ou tirar dúvidas sobre os processos participativos, por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\n\nAcesse os nossos cursos de capacitação na plataforma EVG (quando estiverem disponibilizados)\n")
            bot.reply_to(message, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "5":
            sm_dict[id_chat].setstate(1)
            bot.reply_to(message,"Por favor, entre em contato pelo e-mail:\nparticipacaodigital@presidencia.gov.br")
            bot.reply_to(message, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "6":
            sm_dict[id_chat].setstate(1)
            bot.reply_to(message,"Confira as principais perguntas sobre os serviços relacionados ao Brasil Participativo (inserir link, da plataforma, de perguntas frequentes)\n")
            bot.reply_to(message, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "7":
            sm_dict[id_chat].setstate(1)
            bot.reply_to(message,"Para assuntos relacionados à plataforma Brasil Participativo, por favor, entre em contato pelo e-mail:\nparticipacaodigital@presidencia.gov.br\nPara outros assuntos, registre a sua manifestação na Plataforma Integrada de Ouvidoria e Acesso à Informação (Fala.BR) https://falabr.cgu.gov.br\n")
            bot.reply_to(message, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")


# penultimo bloco de perguntas
@bot.message_handler(
    func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 7) and compare(message.chat.id, 1))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            bot.send_message(id_chat,
                             "Agradecemos o seu contato e continuamos à disposição! Para acompanhar todas "
                             "as atividades realizadas pelo Brasil Participativo, acesse "
                             "https://brasilparticipativo.presidencia.gov.br/")
        case "2":
            sm_dict[id_chat].setstate(2)
            bot.send_message(id_chat,
                             "Digite 9 - Retornar ao menu anterior ?\nCaso queira encerrar o atendimento, digite “sair”")


# ultimo bloco de perguntas
@bot.message_handler(func=lambda message: message.text == "9" and compare(message.chat.id, 2))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "9":
            bot.send_message(id_chat, "Digite 1 - O que é o Brasil Participativo?\n" +
                             "Digite 2 - Processos Participativos\n" +
                             "Digite 3 - Dificuldade de acesso\n" +
                             "Digite 4 - Represento um órgão da Administração Pública Federal\n" +
                             "Digite 5 - Sou da imprensa\n" +
                             "Digite 6 - Perguntas Frequentes\n" +
                             "Digite 7 - Outros Assuntos\n")
            sm_dict[id_chat].setstate(0)
#Daqui pra baixo apenas lógica do segundo fluxo

@bot.message_handler(func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 6) and compare(message.chat.id, 3))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            sm_dict[id_chat].setstate(4)
            bot.reply_to(message,"Digite 1 - O que é o Plano Clima/PPA Participativo?\n "
                            "Digite 2 - Como participar?\n "
                            "Digite 3 - Plano Clima/PPA abertos\n "
                            "Digite 4 - Plano Clima/PPA fechados")
        case "2":
            sm_dict[id_chat].setstate(5)
            bot.reply_to(message,"Digite 1 - O que é uma conferência?\n "
                            "Digite 2 - Como participar?\n "
                            "Digite 3 - Conferências abertas/ativas\n "
                            "Digite 4 - Conferências fechadas/encerradas")
        case "3":
            sm_dict[id_chat].setstate(6)
            bot.reply_to(message,"Digite 1 - O que é uma consulta pública?\n "
                            "Digite 2 - Como participar?\n "
                            "Digite 3 - Consultas públicas abertas\n "
                            "Digite 4 - Consultas públicas fechadas")
        case "4":
            sm_dict[id_chat].setstate(7)
            bot.reply_to(message,"Digite 1 - O que é uma enquete?\n "
                            "Digite 2 - Como participar?\n "
                            "Digite 3 - Enquetes abertas\n "
                            "Digite 4 - Enquetes públicas fechadas")
        case "5":
            sm_dict[id_chat].setstate(8)
            bot.reply_to(message,"Digite 1 - O que é uma audiência?\n "
                            "Digite 2 - Como participar?\n "
                            "Digite 3 - Audiências públicas abertas\n "
                            "Digite 4 - Audiências públicas fechadas")
        case "6":
            sm_dict[id_chat].setstate(9)
            bot.reply_to(message,"Digite 1 - O que é um colegiado?\n "
                            "Digite 2 - Como participar?\n "
                            "Digite 3 - Colegiados abertos\n "
                            "Digite 4 - Colegiados fechados")

#Plano clima          
@bot.message_handler(func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 4) and compare(message.chat.id, 4))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"O Plano Clima é uma estratégia governamental adotada pelo Brasil para lidar com as "
                                  "mudanças climáticas. Seu principal objetivo é liderar a redução das emissões de "
                                  "gases de efeito estufa, visando conter o aquecimento global abaixo de 1,5°C.\n"
                                  "O Plano Plurianual (PPA) é um documento que está previsto na Constituição de 1988. "
                                  "Ele é elaborado de quatro em quatro anos, sempre no primeiro ano de mandato do "
                                  "presidente. O PPA define metas, diretrizes e programas do Governo. Em 2023, ele será"
                                  " elaborado com apoio aberto da população por meio da plataforma Brasil"
                                  " Participativo. O PPA deve ser entregue às(aos) senadoras(es) e deputadas(os) no "
                                  "Congresso Nacional até 31 de agosto de 2023, junto à Lei Orçamentária Anual (LOA).")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "2":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Basta criar uma conta no Gov.Br ou baixar o app. Se você já tem conta, "
                                  "é só entrar com seu login e senha, em seguida fazer suas escolhas e propostas "
                                  "entre 11 de maio e 14 de julho de 2023.")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "3":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para mais informações sobre o Plano Clima atual, acesse:\n"
                                "https://lab-decide.dataprev.gov.br/processes/planoclima?locale=pt-BR")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "4":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"O Plano Clima foi instituído em 2009 para consolidar a execução da Política Nacional"
                                  " de Mudança do Clima.\n"
                                  "Plano Clima de 2015: https://www.mds.gov.br/webarquivos/arquivo/seguranca_alimentar"
                                  "/caisan/Publicacao/Caisan_Nacional/PlanoNacionaldeAdaptacaoaMudancadoClima"
                                  "_Junho2015.pdf\n"
                                  "Plano Clima atual: "
                                  "https://lab-decide.dataprev.gov.br/processes/planoclima?locale=pt-BR\n"
                                  "Para consultar os PPAs anteriores, acesse:"
                                  "https://www.gov.br/planejamento/pt-br/assuntos/plano-plurianual/paginas/"
                                  "acesse-os-planos-plurianuais-anteriores")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")

#Conferências
@bot.message_handler(func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 4) and compare(message.chat.id, 5))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Uma conferência é um importante instrumento de participação social que "
                                  "reúne diversos segmentos representativos da sociedade para debater e avaliar "
                                  "políticas públicas e propor diretrizes para o seu aperfeiçoamento nos três "
                                  "níveis de governo: municipal, estadual e nacional. Elas são espaços de diálogo "
                                  "social e construção coletiva, nos quais atores diversos apontam suas demandas e "
                                  "contribuições em relação à política pública e a como ela se materializa em serviços "
                                  "nos territórios e comunidades.\n")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "2":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para participar, basta seguir o passo a passo abaixo: "
                                  "1º  Acesse o endereço: https://brasilparticipativo.presidencia.gov.br/"
                                  "2º Clique em “entrar” no canto superior direito da tela;"
                                  "3º Clique em “entrar com Gov.br” e preencha com os  seus dados;"
                                  "4º Selecione o módulo ‘Conferências’;"
                                  "5º Escolha a conferência desejada para fazer sua contribuição.")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "3":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Confira as conferências abertas pelo link:\n"
                                  "https://brasilparticipativo.presidencia.gov.br/assemblies")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "4":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Confira as conferências fechadas pelo link:\n"
                                  "https://brasilparticipativo.presidencia.gov.br/assemblies")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")

#Consultas Públicas
@bot.message_handler(func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 4) and compare(message.chat.id, 6))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"É um mecanismo de participação social, de caráter consultivo, realizado com prazo "
                                  "definido e aberto a qualquer interessado, com o objetivo de receber contribuições"
                                  " sobre determinado assunto. Incentiva a participação da sociedade na tomada de "
                                  "decisões relativas à formulação e definição de políticas públicas.")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "2":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para participar, siga o passo a passo abaixo: "
                                  "1º  Acesse o Sistema de Consulta Pública "
                                  "(https://www3.bcb.gov.br/audpub/HomePage?1)"
                                  "e clique no link de Consultas Ativas para "
                                  "sugerir alterações em minuta de norma a ser publicada pelo Banco Central;\n"
                                  "2º Inserir sugestões ao texto da minuta ao clicar no link “Enviar sugestão”. Deverá "
                                  "ser descrita a sugestão e a qual parte do texto se refere. "
                                  "Também é possível incluir anexos;\n"
                                  "3º Acesse o Sistema de Consulta Pública e clique no link de Consultas Encerradas. "
                                  "As sugestões e os anexos encaminhados em todas as consultas "
                                  "são disponibilizadas no sistema.")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "3":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para ver as consultas públicas abertas, acesse:"
                                  "https://www.gov.br/saude/pt-br/acesso-a-informacao/"
                                  "participacao-social/consultas-publicas")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "4":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Confira as consultas púbicas fechadas pelo link: "
                                  "https://www.gov.br/saude/pt-br/acesso-a-informacao/"
                                  "participacao-social/consultas-publicas")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")

#Enquetes
@bot.message_handler(func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 4) and compare(message.chat.id, 7))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"As Enquetes visam a dar maior publicidade e transparência ao trabalho de elaboração"
                                  " de Protocolos Clínicos e Diretrizes Terapêuticas (PCDT) desenvolvido pela Conitec."
                                  " Foram criadas como mais um meio de comunicação com a sociedade, a fim de "
                                  "melhorarmos esse processo. Elas são disponibilizadas como consulta prévia, ainda na"
                                  " primeira etapa de construção do PCDT, para que possamos discutir uma proposta "
                                  "inicial e, assim, melhorá-la, identificando aspectos que podem não ter sido "
                                  "considerados anteriormente. Dessa forma, a participação popular será considerada "
                                  "desde o início do processo de elaboração do PCDT, e não apenas na Consulta Pública"
                                  " para deliberação final.\n")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "2":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para votar, o cidadão deve acessar a página de enquetes disponível no Portal da "
                                  "Câmara pelo menu superior Participe/Enquetes ou pelo endereço enquetes.camara.leg.br"
                                  " e registrar seu voto. Comentários à matéria, no entanto, não são computados "
                                  "como votos.\n")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "3":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para consultar as enquetes abertas, acesse:\n"
                             "https://www.gov.br/conitec/pt-br/assuntos/participacao-social/enquetes")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "4":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para consultar as enquetes fechadas, acesse:\ns"
                             "https://www.gov.br/conitec/pt-br/assuntos/participacao-social/enquetes\n")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")

#Audiências Públicas
@bot.message_handler(func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 4) and compare(message.chat.id, 8))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"As Audiências Públicas são ambientes de ampla consulta à sociedade com o "
                                  "objetivo de colher"
                                  " subsídios e informações, além de oferecer aos interessados a oportunidade de "
                                  "encaminhar "
                                  "suas solicitações, pleitos, opiniões e sugestões, em especial da população "
                                  "diretamente "
                                  "afetada pelo objeto do debate.")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "2":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para participar, acesse:\n"
                                  "https://www.gov.br/pt-br/servicos/participar-de-audiencias-e-consultas-publicas")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "3":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para consultar as audiências abertas, acesse:\n"
                             "https://www.gov.br/saude/pt-br/acesso-a-informacao/participacao-social/audiencias-publicas")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "4":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para consultar as audiências fechadas, acesse:\n"
                             "https://www.gov.br/saude/pt-br/acesso-a-informacao/participacao-social/audiencias-publicas")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")

#Colegiados
@bot.message_handler(func=lambda message: message.text.isdigit() and (1 <= int(message.text) <= 4) and compare(message.chat.id, 9))
def handle_messages(message):
    global sm_dict
    id_chat = message.chat.id
    match message.text:
        case "1":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Órgãos Colegiados referem-se a um corpo consultivo e/ou deliberativo que tem como"
                                  " objetivo reunir pessoas com a competência de emitir pareceres e deliberações sobre"
                                  " políticas públicas e atuam como canais de diálogo e de fiscalização.")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "2":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Para participar de colegiados, bem como obter mais informações, acesse:\n"
                             "https://www.gov.br/participamaisbrasil/colegiados")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "3":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"Consulte os colegiados abertos e as datas de reuniões em:\n"
                             "https://www.gov.br/mdh/pt-br/acesso-a-informacao/governanca/comissao-de-etica-publica-setorial/calendario")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")
        case "4":
            sm_dict[id_chat].setstate(1)
            bot.send_message(id_chat,"ara consultar os colegiados encerrados, acesse:\n"
                             "https://www.gov.br/mdh/pt-br/acesso-a-informacao/governanca/scomissao-de-etica-publica-setorial/calendario")
            bot.send_message(id_chat, "Sua demanda foi atendida? \n1 - Sim \n2 - Não")




@bot.message_handler(func=lambda message: message.text == "sair")
def handle_messages(message):
    id_chat = message.chat.id
    bot.send_message(id_chat, "Saindo")
    # precisamos ver como encerrar o atendimento


bot.infinity_polling()
