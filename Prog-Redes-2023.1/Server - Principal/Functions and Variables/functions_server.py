import socket
from functions_others import *
from variables import *

def connection():
    ...

def LIST_CLIENTS(clients_dict=None, sock=None, **kwargs):
    for chave, valor in clients_dict.items():  
        ip = valor[0]
        msg_list = f"IP: {ip}\nPORT: {chave}"
        sock.send(msg_list.encode(UNICODE))
    

def CLIENT_INTERACTION(sock_client, info_client, clients_connected):
    opções = {'/l': LIST_CLIENTS}
    msg = b'' # definindo uma mensagem binária
    while msg != b'/q': 
        try:
            msg = sock_client.recv(512).decode(UNICODE)
            print(msg)
            for opcao in opções.keys():
                if msg == opcao:
                    opções[opcao](clients_dict=clients_connected,sock=sock_client)
            #broadCast (msg, info_client)
        except:
            msg = b'/q'
    del clients_connected[info_client[1]]
    sock_client.close()

def broadCast(msg, addrSource):
    #msg = f"{addrSource} -> {msg.decode(UNICODE)}"
    #PRINT_DIV(msg)
    for sockConn, addr in clients_connected:
        if addr != addrSource:
            sockConn.send(msg.encode(UNICODE))