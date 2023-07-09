import socket
from functions_others import *
from variables import *

# ============================================================================================================

def CHAT(comand=None, clients_dict=None, **kwargs):
    ip_destination = comand[1]
    port = comand[2]
    msg_chat = comand[3]
    for chave, valor in clients_dict.items():
        sock_envio = valor[1]
        ip_envio = valor[0]
        print(ip_destination, ip_envio)
        print('---')
        print(port, chave)
        if port == chave:
            rint('SIM É IGUAL 02')
        if ip_destination == ip_envio and port == chave:
            print('chegou')
            sock_envio.send(msg_chat.encode(UNICODE))
            
# ============================================================================================================

def LIST_CLIENTS(clients_dict=None, sock=None, **kwargs):
    msg_title = "\nOs Clientes conectados ao Servidor são:"
    sock.send(msg_title.encode(UNICODE))
    num = 0
    for chave, valor in clients_dict.items():  
        ip = valor[0]
        num+=1
        msg_list = f"\nCLIENTE {num}\nIP: {ip}\nPORT: {chave}\n"
        sock.send(msg_list.encode(UNICODE))
    
# ============================================================================================================

def CLIENT_INTERACTION(sock_client, info_client, clients_connected):
    opções = {
        '/l': LIST_CLIENTS,
        '/m': CHAT
    }
    msg = b'' 
    while msg != b'/q': 
        try:
            msg = sock_client.recv(512).decode(UNICODE)
            comand = COMAND_SPLIT(msg)
            for opcao in opções.keys():
                if comand[0] == opcao:
                    opções[opcao](clients_dict=clients_connected,sock=sock_client, comand=comand)
        except:
            msg = b'/q'
    del clients_connected[info_client[1]]
    sock_client.close()

# ============================================================================================================











def broadCast(msg, addrSource):
    #msg = f"{addrSource} -> {msg.decode(UNICODE)}"
    #PRINT_DIV(msg)
    for sockConn, addr in clients_connected:
        if addr != addrSource:
            sockConn.send(msg.encode(UNICODE))