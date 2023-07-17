import socket, sys
from functions_others import *
from variables import *
from functions_download import *

''' ATENÇÃO, TENHA A BIBLIOTECA SOCKETS INSTALADA! '''

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR O CHAT ENTRE CLIENTES ESPECIFICOS  '''

def CHAT(comand=None, clients_dict=None, info_client=None, sock=None, **kwargs): 
    try:
        ip_destination = comand[1] # guardando o ip de destino da mensagem
        port = comand[2] # guardando a porta de destino
        for chave, valor in clients_dict.items(): # dando um for na lista de clientes
            port_envio = str(chave) # Armazenamento Temporário 
            ip_envio = valor[0] # Armazenamento Temporário 
            sock_envio = valor[1] # pegando o socket do cliente destino 
            if ip_destination == ip_envio and port == port_envio: # verificando se o ip/porta (ou seja cliente) está conectado ao servidor
                msg_chat = f"\nO Cliente: {info_client[0]}:{info_client[1]} lhe enviou uma mensagem!\nMensagem >> {comand[3]}\n" # formatação de mensagem
                sock_envio.send(msg_chat.encode(UNICODE)) # realizando o envio para o socket do cliente destino
            else: # para caso do Cliente não ser achado 
                msg_erro = f"\nO Cliente informado para encaminhar a mensagem não está conectado ao Servidor!\n"
                sock.send(msg_erro.encode(UNICODE))
    except:
        print(f'\nErro no Chat...{sys.exc_info()[0]}')  
        exit() 
            
# ============================================================================================================

''' FUNÇÃO PARA REALIZAR O PRINT DA LISTAGEM DE CLIENTES CONECTADOS AO SERVIDOR '''

def LIST_CLIENTS(clients_dict=None, sock=None, **kwargs):
    try: 
        msg_list = "\nOs Clientes conectados ao Servidor são:\n\n" # formatando mensagem 
        num = 0
        for chave, valor in clients_dict.items():  # faço um for para pegar cada cliente conectado e enviar 
            ip = valor[0] # Armazenamento Temporário 
            num+=1 # formatação numeração cliente
            msg_list += f"\nCLIENTE {num}\nIP: {ip}\nPORT: {chave}\n\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip)
        sock.send(msg_list.encode(UNICODE)) # enviando mensagens 
    except:
        print(f'\nErro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit() 

# ============================================================================================================

''' FUNÇÃO PARA ENVIAR MENSAGEM EM MODO BROADCAST (P/ TODOS CLIENTES, EXCETO QUEM PEDIU) '''

def BROADCAST (clients_dict=None, info_client=None, comand=None, **kwargs):
    msg_broadcast = f"\nO Cliente: {info_client[0]} : {info_client[1]} Enviou uma mensagem para Todos!\nMensagem >> {comand[1]}\n" # formatação de mensagem
    try:
        for chave, valor in clients_dict.items(): # realizando o for para mandar p/ todos os clientes
            port_envio = chave # Armazenamento Temporário 
            ip_envio = valor[0] # Armazenamento Temporário 
            if port_envio != info_client[1]: # pegando sock de todos, exceto do cliente que pediu
                sock_broadcast = valor[1] # Armazenamento Temporário 
                sock_broadcast.send(msg_broadcast.encode(UNICODE)) # enviando mensagem
    except:
        print(f'\nErro no momento de enviar o Broadcast...{sys.exc_info()[0]}')  
        exit()                 

# ============================================================================================================

''' FUNÇÃO PARA ENVIAR AO CLIENTE O SEU HISTÓRICO DE COMANDOS '''

def HISTORY(history=None, sock=None, **kwargs):
    try:
        msg_history = f"\nEsse é o seu histórico de comandos:\n\n" # formatação mensagem
        num = 0
        for comands in history: # pegando cada comando do histórico
            num += 1 
            msg_history += f"    {num} {comands}\n" # formatando linha:comando
        sock.send(msg_history.encode(UNICODE)) # enviando comando por comando
    except:
        print(f'\nErro no momento de enviar o Histórico de Comandos...{sys.exc_info()[0]}')  
        exit()  


# ============================================================================================================

''' FUNÇÃO QUE LISTA AS OPÇÕES DISPONIVEIS PARA O CLIENTE '''

def HELP(sock=None, **kwargs):
    try:
        # Criando descrição de cada comando
        descriptive_options = {
        '/l': 'Listar clientes conectados',
        '/m:ip:porta:mensagem': 'Enviar mensagem para cliente especifíco (informe IP:PORTA do cliente)',
        '/b:mensagem': 'Enviar mensagem em Broadcast (Para todos clientes conectados)',
        '/h': 'Lista o seu histórico de comandos',
        '/?': 'Lista as opções disponiveis',
        '/q': 'Desconectar do Servidor'
        }
        msg_help = f"\nSegue abaixo as Opções disponiveis neste servidor:\n\n" # formatação mensagem
        for comando, descrição in descriptive_options.items(): # listando por meio do FOR comando por comando 
            msg_help += f"  {comando} -> {descrição}\n" # formatação mensagem
        sock.send(msg_help.encode(UNICODE)) # enviando comando por comando
    except:
        print(f'\nErro no momento de listar as Opções...{sys.exc_info()[0]}')  
        exit()  

# ============================================================================================================


def LIST_FILES():
    ...













# ============================================================================================================

''' FUNÇÃO QUE REALIZA A INTERAÇÃO DO CLIENTE (DEFINE A FUNÇÃO A SER CHAMADA DE ACORDO COM O PEDIDO DO CLIENTE) '''

def CLIENT_INTERACTION(sock_client, info_client, clients_connected):
    try:
        history_client = list()
        options = { # dicionário com todas as opções para o cliente (sendo o valor a função ser chamada)
            '/l': LIST_CLIENTS,
            '/m': CHAT,
            '/b': BROADCAST,
            '/h': HISTORY,
            '/?': HELP,
            '/f': LIST_FILES}
        options_choice = set(options.keys()) # usado para verificar se o comando pertence ao dicionário 
        msg = b'' 
        while msg != b'/q': # continuar ouvindo o cliente a menos que ele digite /q
            try:
                msg = sock_client.recv(BUFFER_SIZE01).decode(UNICODE) # recebendo mensagem do cliente
                history_client.append(msg) # histórico de comandos do cliente
                comand = COMAND_SPLIT(msg) # realizando split do comando do cliente 
                comand_prompt = comand[0].lower() # usando apenas para pegar o comando bruto "/x"
                if comand_prompt in options_choice:  # verificando se o comando está dentro das opções disponivéis 
                    # ativando a função chamada (passando argumento depois)
                    options[comand_prompt](clients_dict=clients_connected, sock=sock_client, comand=comand, info_client=info_client, history=history_client, options=options)
            except:
                msg = b'/q'
        del clients_connected[info_client[1]] # quando o cliente digitar /q ele exclui socket do cliente da lista de clientes ativos
        sock_client.close()
    except:
        print(f'\nErro na Interação do Cliente [pelo servidor]...{sys.exc_info()[0]}')  
        exit() 


# ============================================================================================================