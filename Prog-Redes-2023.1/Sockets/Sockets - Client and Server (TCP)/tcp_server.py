import socket, sys, os
diretorio_atual = os.path.dirname(os.path.abspath(__file__)); sys.path.append(diretorio_atual + '\\Functions')
from socket_constants import * ; from Socket_Connection import SERVER_TCP

# ------------------------------------------------------------------------------------------------------------

socket_tcp = SERVER_TCP(HOST_SERVER, SOCKET_PORT, 1)

# informações do servidor ativo (ip e porta)
print(f'\nSERVIDOR ATIVO: {socket_tcp.getsockname()}\n')

# aceitando conexões
socket_conexão, ip_client = socket_tcp.accept()
print(f'O cliente de ip: {ip_client[0]}\nNa porta: {ip_client[1]}\nFoi conectado com sucesso ao servidor!\n')   
print('Esperando Recebimento de mensagens...\n')

# ------------------------------------------------------------------------------------------------------------

try:
    arq_existe = 0
    while True:
        msg_client = socket_conexão.recv(BUFFER_SIZE)
        msg_client = msg_client.decode(CODE_PAGE)
        if msg_client.upper() == 'EXIT':
            print(f'\nO cliente {ip_client} se desconectou do servidor...!\n')
            break
        
# ------------------------------------------------------------------------------------------------------------

        else:
            nome_arquivo = ATUAL_DIR + '\\img_server\\' + msg_client
            for arquivo in ATUAL_DIR+'\\img_server':
                if nome_arquivo != arquivo:
                    arq_existe = 1
            if arq_existe != 0:
                print(f'O Arquivo que você pediu {msg_client} não existe no servidor!')
                break
            print(f'Enviando o arquivo: {msg_client}\n')
            size_arq = os.path.getsize(nome_arquivo)
            msg_server = f'Size: {size_arq}'.encode(CODE_PAGE)
            socket_conexão.send(msg_server)
            
# ------------------------------------------------------------------------------------------------------------

            with open(nome_arquivo, 'rb') as arquivo:
                while True:
                    dados_img = arquivo.read(BUFFER_SIZE)
                    if not dados_img:
                        break
                    socket_conexão.send(dados_img)
            print(f'O Arquivo: {msg_client} foi enviado!\n')
            
# ------------------------------------------------------------------------------------------------------------

except KeyboardInterrupt:
    print('Foi pressionado CTRL+C!')
    # Fechando o socket
    socket_conexão.close()    
except:
    print(f'ERRO: {sys.exc_info()[0]}')
    socket_conexão.close()    
finally:    
    # Fechando o socket
    socket_conexão.close()


# ------------------------------------------------------------------------------------------------------------
