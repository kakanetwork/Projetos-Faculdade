
import requests
from credentials import *

# ============================================================================================================

def NOTIFICATION_BOT(msg):
    try:
        url_req = f'https://api.telegram.org/bot{API_key}'
        resposta = {'chat_id':id_chat,'text':f'{msg}'}
        var = requests.post(url_req+'/sendMessage',data=resposta)
    except:
        print(f'\nErro no envio da mensagem para o Bot...{sys.exc_info()[0]}')  

# ============================================================================================================
def COMMAND_BOT():
    offset = None
    while True:
        url_req = f'https://api.telegram.org/bot{API_key}'
        chat = requests.get(url_req + '/getUpdates', params={'offset': offset}).json().get('result', [])

        for message in chat:
            command = message.get('message', []).get('text', [])
            if command == '/u':
                resposta = {'chat_id':id_chat,'text':'lista clientes'}
                var = requests.post(url_req+'/sendMessage',data=resposta)
            id_message= message['update_id'] + 1
            print(id_message)
            

COMMAND_BOT()


def LIST_CLIENTS_BOT():
    ...