import socket, sys, os, time
from socket_constants import *
# Criação do socket (IPV4 / TCP)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando ao host e porta 
socket_tcp.bind((HOST_SERVER,SOCKET_PORT))

# definindo quantas conexões ele ira atender
socket_tcp.listen(1)

# informações do servidor ativo (ip e porta)
print(f'\nSERVIDOR ATIVO: {socket_tcp.getsockname()}\n')

socket_conexão, ip_client = socket_tcp.accept()
print(f'O cliente de ip: {ip_client[0]}\nNa porta: {ip_client[1]}\nFoi conectado com sucesso ao servidor!\n')   
print('Esperando Recebimento de mensagens...\n')

while True:
    msg_client = socket_conexão.recv(BUFFER_SIZE)
    msg_client = msg_client.decode(CODE_PAGE)
    if msg_client.upper() == 'EXIT':
        print(f'\nO cliente {ip_client} se desconectou do servidor...!\n')
        break
    else:
        nome_arquivo = ATUAL_DIR + '\\img_server\\' + msg_client
        print(f'Enviando o arquivo: {msg_client}\n')
        size_arq = os.path.getsize(nome_arquivo)
        msg_server = f'Size: {size_arq}'.encode(CODE_PAGE)
        socket_conexão.send(msg_server)
        with (nome_arquivo, 'rb') as arquivo:
            while True:
                dados_img = arquivo.read(BUFFER_SIZE)
                if not data_retorno:
                    break
                
    break
'''
print('\nRecebendo Mensagens...\n\n')

try:
    while True:
        mensagem, ip_cliente = socket_TCP_IPV4.recv(BUFFER_SIZE)
        mensagem = mensagem.decode(CODE_PAGE)
        if mensagem.upper() == 'EXIT':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
        else:
            # Nome do arquivo a ser enviado
            nome_arquivo = ATUAL_DIR + '\\img_server\\' + mensagem
            print(f'Enviando arquivo {mensagem.upper()} ...')

            tamanho_arquivo = os.path.getsize(nome_arquivo)
            msg = f'Size:{tamanho_arquivo}'.encode(CODE_PAGE)
            socket_TCP_IPV4.send(msg, ip_cliente)

            arquivo = open(nome_arquivo, 'rb')
            while True:
                data_retorno = arquivo.read(BUFFER_SIZE)
                if not data_retorno: break                                
                socket_TCP_IPV4.send(data_retorno, ip_cliente)
                time.sleep(0.02)
            print(f'Arquivo {mensagem.upper()} Enviado...')
            arquivo.close()
except KeyboardInterrupt:
    print('Foi pressionado CTRL+C')
    # Fechando o socket
    socket_TCP_IPV4.close()    
except:
    print(f'\nERRO: {sys.exc_info()}')
finally:    
    # Fechando o socket
    socket_TCP_IPV4.close()'''