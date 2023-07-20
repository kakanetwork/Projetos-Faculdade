import socket, threading, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions-and-Variables')
dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual

from variables import *
from functions_client import *
from functions_others import PRINT_DIV


try:
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.connect((SERVER_CLIENT, PORT))

    PRINT_DIV(f"Você se conectou com sucesso ao Server de IP: {SERVER} | Na Porta: {PORT}")
    tServer = threading.Thread(target=servInteraction, args=(sock_tcp,))
    tUser = threading.Thread(target=userInteraction, args=(sock_tcp,))

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
except KeyboardInterrupt:
    print(f'\n\nVocê encerrou a conexão.\nVolte Sempre!\n')  
    exit()     

except:
    print(f'\nErro na Inicialização do Cliente...{sys.exc_info()[0]}')  
    exit() 