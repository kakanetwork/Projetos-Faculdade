import socket, threading, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Variables')
from variables import *
from functions_server import *

try: 
    clientes = dict() # lista de clientes conectados (IP:PORTA)
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # conexão IPV4/TCP
    sock_tcp.bind((SERVER, PORT)) # atribuindo Porta e Local
    print(f'Servidor: {SERVER} / {PORT}')
    sock_tcp.listen() # deixando indefinido quantidade máxima de conexões
    while True:
        try:
            port_client, ip_client = sock_tcp.accept() # aceitando clientes (guardando porta e ip respectivamente do cliente)
            print ("Connection from: ", ip_client) # informando a conexão
            clientes[port_client] = ip_client # adicionando o cliente ao dicionario de clientes conectados
            thread_client = threading.Thread(target=cliInteraction, args=(port_client, ip_client)) # adicionando uma thread para cada cliente
            thread_client.start()

        except:
            print(sys.exc_info())
            exit()
except:
    print ("Fail: ")