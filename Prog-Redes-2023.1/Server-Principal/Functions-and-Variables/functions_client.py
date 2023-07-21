import socket, time
from variables import *
from functions_others import *


# ============================================================================================================

def DOWNLOAD_RECV(sock_tcp, size, name, dir_atual):
    try:
        print(f'\nGravando o arquivo: {name}\nTamanho: {size} bytes')
        local_arquive = dir_atual + f'\\{name}'
        with open(local_arquive, 'wb') as arquivo:
            bytes_recebidos = 0
            pct = 1
            while True:
                # Recebendo o conteúdo do servidor
                data_arquive = sock_tcp.recv(BUFFER)
                if not data_arquive: break
                arquivo.write(data_arquive)
                bytes_recebidos += len(data_arquive)
                print(f'Pacote ({pct}) - Dados: {bytes_recebidos}/{size} bytes')
                if bytes_recebidos >= size: break
                pct += 1
        print('\nDownload Finalizado!\n')
    except:
        print(f'download...{sys.exc_info()}')



# ============================================================================================================

def CLOSE_SOCKET(sock_tcp):
    try:
        sock_tcp.close()
    except:
        None
    
# ============================================================================================================

def SERVER_INTERACTION(sock_tcp, dir_atual):
    try:
        while True:
            retorno = sock_tcp.recv(512)
            if not retorno:  # Verificar se o retorno é vazio, indicando que o socket foi fechado pelo cliente
                break
            msg = retorno.decode(UNICODE)
            if msg == '/q':
                print("\nConexão encerrada.\n")
                break
            if msg[:2] == '/d':
                info_arquive = COMAND_SPLIT(msg)
                size = int(info_arquive[1])
                name = info_arquive[2]
                DOWNLOAD_RECV(sock_tcp, size, name, dir_atual)
                continue
            print(msg)
    except:
        print(f'\nErro na interação com o servidor... {sys.exc_info()}')
    finally:
        CLOSE_SOCKET(sock_tcp)

# ============================================================================================================

def USER_INTERACTION(sock_tcp, dir_atual):
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
        CLOSE_SOCKET(sock_tcp)

# ============================================================================================================
