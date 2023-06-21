import socket, sys, os

# Caso o arquivo sockets_constants.py esteja um diretório acima do atual
#diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#diretorio_atual = diretorio_atual.rsplit('\\',1)[0]
#sys.path.insert(0, diretorio_atual)

from socket_constants import *

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicitar o arquivo
    nome_arquivo = input('Digite o nome do arquivo (EXIT p/ sair): ')
    
    # Enviando o nome do arquivo para o servidor
    print(f'\nSolicitando o arquivo {nome_arquivo}')
    udp_socket.sendto(nome_arquivo.encode(CODE_PAGE), (HOST_SERVER, SOCKET_PORT))
    
    if nome_arquivo.upper() == 'EXIT': break

    dado_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE)
    dado_retorno = dado_retorno.decode(CODE_PAGE)
    if 'Size:' in dado_retorno:
        tamanho_total = int(dado_retorno.split(':')[1])

    # Gravar o dado recebido em arquivo
    print(f'Gravando o arquivo {nome_arquivo} ({tamanho_total} bytes)')
    nome_arquivo_ = ATUAL_DIR + '\\img_client\\' + nome_arquivo
    arquivo = open(nome_arquivo_, 'wb')
    bytes_recebidos = 0
    pct = 1
    while True:
        # Recebendo o conteúdo do servidor
        dado_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE)
        if not dado_retorno: break
        print(f'Pacote ({pct}) - Dados Recebidos: {len(dado_retorno)} bytes')
        arquivo.write(dado_retorno)
        bytes_recebidos += len(dado_retorno)
        if bytes_recebidos >= tamanho_total: break
        pct += 1

    arquivo.close()

# Fechando o socket
udp_socket.close()