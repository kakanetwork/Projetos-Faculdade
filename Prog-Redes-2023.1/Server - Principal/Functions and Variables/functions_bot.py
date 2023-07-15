
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
    id_message = None
    while True:
        url_req = f'https://api.telegram.org/bot{API_key}'
        chat = requests.get(url_req + '/getUpdates', params={'offset': id_message}).json().get('result', [])
        for message in chat:
            command = message.get('message', []).get('text', [])
            if command == '/u':
                resposta = {'chat_id':id_chat,'text':'lista clientes'}
                var = requests.post(url_req+'/sendMessage',data=resposta)
            id_message= message['update_id'] + 1
            print(id_message)

# ============================================================================================================

def LIST_CLIENTS_BOT(clients_dict):
    try: 
        msg_title = "\nOs Clientes conectados ao Servidor são:" # formatando mensagem 
        '''num = 0
        for chave, valor in clients_dict.items():  # faço um for para pegar cada cliente conectado e enviar 
            ip = valor[0] # Armazenamento Temporário 
            num+=1 # formatação numeração cliente
            msg_list = f"\nCLIENTE {num}\nIP: {ip}\nPORT: {chave}\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip) '''
    except:
        print(f'\nErro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit() 
