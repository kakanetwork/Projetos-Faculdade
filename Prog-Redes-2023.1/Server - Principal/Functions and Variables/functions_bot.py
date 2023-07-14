
import requests
from credentials import *

url_req = f'https://api.telegram.org/bot{API_key}'

def connected_client(msg):
    try:
        resposta = {'chat_id':id_chat,'text':f'{msg}'}
        var = requests.post(url_req+'/sendMessage',data=resposta)
    except:
        print(f'\nErro no envio da mensagem para o Bot...{sys.exc_info()[0]}')  