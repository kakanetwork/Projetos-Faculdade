import socket, threading, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Variables')
from variables import *
from functions_client import *
from functions_others import PRINT_DIV


try:
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.connect((SERVER_CLIENT, PORT))

    PRINT_DIV(f"Você se conectou com sucesso ao Server de IP: {SERVER} | Na Porta: {PORT}")
    tServer = threading.Thread(target=servInteraction, args=sock_tcp)
    tUser = threading.Thread(target=userInteraction, args=sock_tcp)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
except Exception as e:
    print ("Falha ", e)
