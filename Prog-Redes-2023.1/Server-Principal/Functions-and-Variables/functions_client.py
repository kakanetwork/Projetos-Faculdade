import socket, time
from variables import *
from functions_others import *



# ============================================================================================================

def closeSocket(sock_tcp):
    try:
        sock_tcp.close()
    except:
        None
    
# ============================================================================================================

def servInteraction(sock_tcp):
    try:
        while True:
            retorno = sock_tcp.recv(512)
            if not retorno:  # Verificar se o retorno é vazio, indicando que o socket foi fechado pelo cliente
                break
            msg = retorno.decode(UNICODE)
            if msg == '/q':
                print("\nConexão encerrada.\n")
                break
            print(msg)
    except:
        print(f'\nErro na interação com o servidor... {sys.exc_info()}')
    finally:
        closeSocket(sock_tcp)

# ============================================================================================================

def userInteraction(sock_tcp):
    try:
        while True:
            msg = input(PROMPT)
            sock_tcp.send(msg.encode())
            if msg == '/q':
                print("\nConexão encerrada.\n")
                break
            time.sleep(0.1)
    except:
        print(f'\nErro na interação com o Usuário... {sys.exc_info()}')
    finally:
        closeSocket(sock_tcp)

# ============================================================================================================
