
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
    message_id = None
    while True:
        try:
            url_req = f'https://api.telegram.org/bot{API_key}/getUpdates'
            if message_id != None:
                url_req += f'?offset={message_id + 1}'
            print(url_req)
            chat = requests.get(url_req).json().get('result', [])
            print(chat)
            for message in chat:
                print(message)
                f = message.get('message', []).get('text', [])
                message_id = message['update_id']
                print(f)
                print(message_id)
            print('================')
        except:
            print('o')
            exit()
        finally:
            if message_id:
                message_id += 1 
COMMAND_BOT()
#req = requisicao
#print(req.get('result', []))

def LIST_CLIENTS_BOT():
    ...