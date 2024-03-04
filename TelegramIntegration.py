import telebot
import requests

token = "6941720254:AAHJpqWTdB35cjfwj2JGLtVNXvCeutDx2dg"

bot = telebot.TeleBot(token=token)


def get_answer_rasa(message) -> str:
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://localhost:5005/webhooks/rest/webhook',
                             json=
                             {"sender": "Rasa", "message": message.text},
                             headers=headers)
    json_resp = response.json()
    print(json_resp)
    print(f"Resposta do RASA: {json_resp[0]['text']}")
    return json_resp    #json


@bot.message_handler(content_types=['text'])
def receive_message(message):
    print(f'Pergunta: {message.text}')
    answer = get_answer_rasa(message)
    if len(answer) > 1:
        bot.send_message(chat_id=message.chat.id, text=answer[0]['text'])
        bot.send_photo(chat_id=message.chat.id, photo=answer[1]['image'])
        bot.send_message(chat_id=message.chat.id, text=answer[2]['text'])
    else:
        bot.send_message(chat_id=message.chat.id, text=answer[0]['text'])


bot.polling(True)  # faz com que o código fique em loop