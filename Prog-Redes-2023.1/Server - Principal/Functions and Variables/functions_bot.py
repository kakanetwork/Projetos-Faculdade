
import requests, sys, time

# ============================================================================================================

''' VERIFICANDO A EXISTÊNCIA DA API_key PARA O TELEGRAM BOT'''

try:
    from credentials import API_key # verificando se a pasta com as credenciais existem (*Apenas no meu computador)
except ModuleNotFoundError: 
    print('\nNão foi encontrado a sua API_key!\n')
    API_key = input('Insira sua API_KEY do Telegram BOT: ') # pedindo a sua API_key
except:
    print(f'\nErro na Aquisição da API_KEY...{sys.exc_info()[0]}')  
    exit()      

url_req = f'https://api.telegram.org/bot{API_key}' # montagem variavel para requisição

# ============================================================================================================

''' FAZENDO A VALIDAÇÃO DA API_KEY E PEGANDO O ID DO CHAT BOT '''

def VERIFICATION_KEY_ID(): 
    try:
        verification_key = requests.get(url_req + '/getUpdates').json() # fazendo uma requisição
        if verification_key.get('ok'): # verificando se a requisição foi completa
            print('\nA API_Key informada foi validada!\n') 
            verification_id = verification_key.get('result') # verificando o chat com o bot 
            if verification_id: # verificando se você possui mensagens no chat do bot para capturar id
                id_chat = verification_id[0]['message']['chat']['id'] # havendo mensagens, ele ira capturar o seu id para prosseguir
                return id_chat # retornando o id 
            else:
                print('Você não possui mensagens armazenadas no Bot, por favor envie qualquer mensagem!')
                return
        else:
            print(f'\nA chave: {API_key}\nInformada é inválida!\n')
            return
    except:
        print(f'\nErro na Verificação da API_KEY...{sys.exc_info()[0]}')  
        exit()
   
id_chat = VERIFICATION_KEY_ID()

# ============================================================================================================

''' FUNÇÃO PARA NOTIFICAR O BOT A CADA CLIENTE CONECTADO '''

def NOTIFICATION_BOT(msg_connected):
    try:
        resposta = {'chat_id':id_chat,'text':f'{msg_connected}'} # realizo a montagem da formatação para o chat com id especificado
        var = requests.post(url_req+'/sendMessage',data=resposta) # envio a mensagem via requests.post
    except:
        print(f'\nErro no envio da mensagem para o Bot...{sys.exc_info()[0]}')  
        exit()

# ============================================================================================================

''' FUNÇÃO PARA LISTAR OS CLIENTES CONECTADOS AO BOT '''

def LIST_CLIENTS_BOT(clients_connected):
    try:
        num = 0
        if len(clients_connected) > 0: # verifica se existe algum cliente conectado
            msg_list = "Os clientes conectados são:\n" # formatação mensagem
            for chave, valor in clients_connected.items(): # pego cada cliente conectado (ip/porta) do dicionário já criado
                ip = valor[0] # Armazenamento Temporário 
                num+=1 # formatação numeração cliente
                msg_list += f"\nCLIENTE {num}\nIP: {ip}\nPORTA: {chave}\n\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip
        else: # se não existir ele informa para o chat que não possui nenhum conectado
            msg_list = "O Servidor não possui nenhum cliente conectado!"
        resposta = {'chat_id':id_chat,'text':f'{msg_list}'} # realizo a montagem da formatação para o chat com id especificado
        var = requests.post(url_req+'/sendMessage',data=resposta) # envio a mensagem via requests.post
    except:
        print(f'\nErro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit() 

# ============================================================================================================

def LOG_BOT():
    try:
        msg_log = "Essa função está em desenvolvimento...."
        resposta = {'chat_id':id_chat,'text':f'{msg_list}'} 
        var = requests.post(url_req+'/sendMessage',data=resposta) 
    except:
        print(f'\nErro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit() 



# ============================================================================================================

''' FUNÇÃO PARA RECEBER MENSAGENS/COMANDOS DA CONVERSA COM O BOT '''

def START_BOT(clients_connected):
    try:
        id_message = None # defino o id da mensagem como NONE, usado mais a frente
        while True: # while True para ficar "ouvindo" o chat
            # faço o get com o parametro offset = id_message, que inicialmente é NONE, transformo em .json e pego apenas oque tem dentro da variavel "RESULT"
            # isso me retorna todas as últimas mensagens do chat e seus parametros (ex: id da mensagem, pelo ID eu consigo identificar a última mensagem)
            chat = requests.get(url_req + '/getUpdates', params={'offset': id_message}).json().get('result', [])
            if len(chat) == 0: # verificando se o chat tá vazio, se estiver ele dá sleep de 1s, e volta pro while para não gastar processamento extra
                time.sleep(1)
                continue
            for message in chat: # pego cada mensagem das últimas mensagens
                command = message.get('message', []).get('text', []) # realizo o get dentro de cada mensagem, para me retornar apenas oque foi digitado ('text')
                if command == '/u' : # verifico se o que foi digitado = /u
                    LIST_CLIENTS_BOT(clients_connected) # se sim, ativo a função de listagem dos clientes conectados
                elif command == '/log':
                    ... # EM DESENVOLVIMENTO ....
                elif command == '/date':
                    ... # EM DESENVOLVIEMNTO ....
                id_message= message['update_id'] + 1 # aqui eu defino o id message (pego ele dentro do .json), e jogo +1 pois funciona como um OFFSET
                    # onde a cada mensagem, o seu id vai ser +1 em relação ao anterior
    except:
        print(f'\nErro no momento de Ler as mensagens do Telegram...{sys.exc_info()[0]}')  
        exit() 

# ============================================================================================================


