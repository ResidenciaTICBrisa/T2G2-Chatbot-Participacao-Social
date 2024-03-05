import telebot
import requests
from dotenv import load_dotenv
import os

load_dotenv()   # verifica se existe um arquivo .env

token = os.getenv('TELEGRAM_TOKEN')  # pega o valor do token do dotenv
bot = telebot.TeleBot(token=token)  # inicia o bot determinado pelo token


def get_answer_rasa(message) -> list[dict]:
    # essa função envia uma requisição POST para a url do rasa e recebe a resposta do RASA, retornando-a em um json
    headers = {'Content-Type': 'application/json'}  # define o tipo de arquivo a ser enviado na requisição
    response = requests.post('http://localhost:5005/webhooks/rest/webhook',
                             json={"sender": "Rasa", "message": message.text},
                             headers=headers)
    # envia a requisição
    json_resp = response.json()  # recebe a requisição, converte pra json e armazena em uma variável
    # print(json_resp)    # nota-se que é uma lista de json, porque o chatbot pode responder multiplas vezes para /
    # unica questão
    print(f"Resposta do RASA: {json_resp[0]['text']}")
    return json_resp  # retorna a lista de json


@bot.message_handler(content_types=['text'])
# decorator necessário para que a função receive_message possa receber as mensagens do telegram
def receive_message(message):
    # essa função fica rodando até que o script seja encerrado, fazendo pooling.
    # portanto, não precisa ser chamada
    print(f'Pergunta: {message.text}')
    answer = get_answer_rasa(message)   # envia a resposta para o rasa
    
    for item in answer:
        #print(f'TESTEEE: {item}')
        
        try:
            if item['text']:
                bot.send_message(chat_id=message.chat.id, text=item['text'])
            
        except KeyError:
            bot.send_photo(chat_id=message.chat.id, photo=item['image'])
            
    
bot.polling(True)  # faz com que o código fique em loop

