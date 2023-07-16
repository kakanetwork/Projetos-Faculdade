import socket, threading, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Variables')
from variables import *
from functions_server import CLIENT_INTERACTION
from functions_others import PRINT_DIV
from functions_bot import *


# ============================================================================================================

try: 
    clients_connected = dict() # lista de clientes conectados (IP:PORTA)
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # conexão IPV4/TCP
    sock_tcp.bind((SERVER, PORT)) # atribuindo Porta e Local
    PRINT_DIV(f'Servidor: {SERVER} / {PORT}')
    thread_bot = threading.Thread(target=START_BOT, args=(clients_connected,)) # adicionando a thread do bot (pois sem ela, eu não consegueria rodar o server e o bot ao mesmo tempo)
    thread_bot.start() # iniciando a thread do bot
    sock_tcp.listen() # deixando indefinido quantidade máxima de conexões

# ============================================================================================================

    while True: 
        try:
            sock_client, info_client = sock_tcp.accept() # aceitando clientes 
            msg_connected = f"O Cliente de IP: {info_client[0]} | Na Porta: {info_client[1]}\nFoi conectado com sucesso!"
            PRINT_DIV(msg_connected) # printando o cliente conectado
            NOTIFICATION_BOT(msg_connected) # enviando mensagem para o bot do cliente que se conectou
            clients_connected[info_client[1]] = [info_client[0], sock_client] # adicionando o cliente ao dicionario de clientes conectados (PORTA:IP,SOCKET)
            thread_client = threading.Thread(target=CLIENT_INTERACTION, args=(sock_client, info_client, clients_connected)) # adicionando uma thread para cada cliente
            thread_client.start() # iniciando a thread

# ============================================================================================================

        except:
            print(f'\nErro na Inicialização da Thread...{sys.exc_info()}')  
            exit() 
except:
    print(f'\nErro na Inicialização do Server...{sys.exc_info()}')  
    exit() 
