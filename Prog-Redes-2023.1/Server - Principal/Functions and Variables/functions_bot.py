
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
url_req = f'https://api.telegram.org/bot{API_key}'
requisicao = requests.get(url_req+'/getUpdates')
print(requisicao.json())

print('================')

def LIST_CLIENTS_BOT():
    ...