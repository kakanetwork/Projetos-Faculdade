import socket, time
from variables import *
from functions_others import *



def DOWNLOAD_RECV(sock_tcp, size, name, dir_atual):
    dados_arquive = sock_tcp.recv(4096)
    print(f'\nGravando o arquivo: {name}\nTamanho: {size} bytes')
    local_arquive = dir_atual + f'\\{name}'
    arquivo = open(local_arquive, 'wb')
    bytes_recebidos = 0
    pct = 1

    while True:
        # Recebendo o conteúdo do servidor
        dado_retorno = RECV(socket_client, BUFFER_SIZE)
        if not dado_retorno: break
        print(f'Pacote ({pct}) - Dados Recebidos: {len(dado_retorno)} bytes')
        arquivo.write(dado_retorno)
        bytes_recebidos += len(dado_retorno)
        if bytes_recebidos >= tamanho_total: break
        pct += 1
    arquivo.close()
    ...

# ============================================================================================================

def closeSocket(sock_tcp):
    try:
        sock_tcp.close()
    except:
        None
    
# ============================================================================================================

def servInteraction(sock_tcp, dir_atual):
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
                size = info_arquive[1]
                name = info_arquive[2]
                DOWNLOAD_RECV(sock_tcp, size, name, dir_atual)
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
