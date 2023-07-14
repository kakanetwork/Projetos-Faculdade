import socket
from variables import *

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR PRINT ORGANIZADO '''

def PRINT_DIV(dados):
    print('\n'+'-'*100)
    print(dados)
    print('-'*100)

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR SPLIT DO COMANDO DO CLIENTE '''

def COMAND_SPLIT(msg):
    try:
        msg_split = msg.split(':')
    except:
        print(f'\nErro no Split do Comand...{sys.exc_info()[0]}')  
        exit() 
    return msg_split

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR DESCONEXÃO DO CLIENTE '''

def QUIT(clients_connected, sock_client, info_client):
    try:
        msg = f"\nVocê será desconectado, volte sempre!\n"
        sock_client.send(msg.encode(UNICODE))
    except:
        print(f'\nErro no envio da mensagem de Desconexão...{sys.exc_info()[0]}')  
        exit() 
    try:
        del clients_connected[info_client[1]] # quando o cliente digitar /q ele exclui socket do cliente da lista de clientes ativos
        sock_client.close()
    except:
        print(f'\nErro na Desconexão do cliente...{sys.exc_info()[0]}')  
        exit() 