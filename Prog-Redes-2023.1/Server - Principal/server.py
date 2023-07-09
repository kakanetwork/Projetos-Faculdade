import socket, threading, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Variables')
from variables import *

try: 
    clientes = list() # lista de clientes conectados
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # conexão IPV4/TCP
    sock.bind((SERVER, PORT))



try:
    clientes = [] # lista de clientes
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # conexão IPV4/TCP
    sock.bind((SERVER, PORT)) # atribuindo Porta e Local
    print ("Servidor:", (SERVER, PORT))
    sock.listen() # deixando indefinido quantidade máxima de conexões
    while True:
        sockConn, addr = sock.accept()
        print ("Connection from: ", addr)
        clientes.append((sockConn, addr))
        tClient = threading.Thread(target=cliInteraction, args=(sockConn, addr))
        tClient.start()
except Exception as e:
    print ("Fail: ", e)