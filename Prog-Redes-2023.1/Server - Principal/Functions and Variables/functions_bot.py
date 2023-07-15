
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
        url_req = f'https://api.telegram.org/bot{API_key}'
        requisicao = requests.get(url_req+'/getUpdates').json().get('result', [])
        print(requisicao)
        print('================')
        
req = requisicao
#print(req.get('result', []))

def LIST_CLIENTS_BOT():
    ...