
import requests, sys
from credentials import *

# variavel de request 
url_req = f'https://api.telegram.org/bot{API_key}'

# ============================================================================================================

''' FUNÇÃO PARA NOTIFICAR O BOT A CADA CLIENTE CONECTADO '''

def NOTIFICATION_BOT(msg_connected):
    try:
        resposta = {'chat_id':id_chat,'text':f'{msg_connected}'} # realizo a montagem da formatação para o chat com id especificado
        var = requests.post(url_req+'/sendMessage',data=resposta) # envio a mensagem via requests.post
    except:
        print(f'\nErro no envio da mensagem para o Bot...{sys.exc_info()}')  
        exit()

# ============================================================================================================

''' FUNÇÃO PARA LISTAR OS CLIENTES CONECTADOS AO BOT '''

def LIST_CLIENTS_BOT(clients_connected):
    try:
        num = 0 
        msg_list = "Os clientes conectados são:\n" # formatação mensagem
        for chave, valor in clients_connected.items(): # pego cada cliente conectado (ip/porta) do dicionário já criado
            ip = valor[0] # Armazenamento Temporário 
            num+=1 # formatação numeração cliente
            msg_list += f"\nCLIENTE {num}\nIP: {ip}\nPORTA: {chave}\n\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip
        resposta = {'chat_id':id_chat,'text':f'{msg_list}'} # realizo a montagem da formatação para o chat com id especificado
        var = requests.post(url_req+'/sendMessage',data=resposta) # envio a mensagem via requests.post
    except:
        print(f'\nErro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit() 

# ============================================================================================================

''' FUNÇÃO PARA RECEBER MENSAGENS/COMANDOS DA CONVERSA COM O BOT '''

def START_BOT(clients_connected):
    print('oi')
    id_message = None # defino o id da mensagem como NONE, usado mais a frente
    while True: # while True para ficar "ouvindo" o chat
        # faço o get com o parametro offset = id_message, que inicialmente é NONE, transformo em .json e pego apenas oque tem dentro da variavel "RESULT"
        # isso me retorna todas as últimas mensagens do chat e seus parametros (ex: id da mensagem, pelo ID eu consigo identificar a última mensagem)
        chat = requests.get(url_req + '/getUpdates', params={'offset': id_message}).json().get('result', [])
        print(chat)
        for message in chat: # pego cada mensagem das últimas mensagens
            command = message.get('message', []).get('text', []) # realizo o get dentro de cada mensagem, para me retornar apenas oque foi digitado ('text')
            if command == '/u' : # verifico se o que foi digitado = /u
                LIST_CLIENTS_BOT(clients_connected) # se sim, ativo a função de listagem dos clientes conectados
            elif command == '/log':
                ... # EM DESENVOLVIMENTO ....
            id_message= message['update_id'] + 1 # aqui eu defino o id message (pego ele dentro do .json), e jogo +1 pois funciona como um OFFSET
                # onde a cada mensagem, o seu id vai ser +1 em relação ao anterior

# ============================================================================================================


