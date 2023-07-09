import socket, threading, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Variables')
from variables import *

try: 
    clientes = dict() # lista de clientes conectados (IP:PORTA)
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # conexão IPV4/TCP
    sock_tcp.bind((SERVER, PORT)) # atribuindo Porta e Local
    print(f'Servidor: {SERVER} / {PORT}')
    sock_tcp.listen() # deixando indefinido quantidade máxima de conexões
    while True:
        try:
            port_client, ip_client = sock.accept()
            print ("Connection from: ", ip_client)
            clientes.append((port_client, ip_client))
            tClient = threading.Thread(target=cliInteraction, args=(port_client, ip_client))
            tClient.start()
        except:
            print('a')
            exit()
except:
    print ("Fail: ")