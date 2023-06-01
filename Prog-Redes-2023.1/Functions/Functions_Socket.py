import socket, ssl, sys

# verifica se a url é HTTP ou HTTPS
def socket_https(url_image, url_host, buffer_size):
    # define a requisição 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
    # criação do contexto SSL para conexão HTTPS
    context = ssl.create_default_context()
    # desativa a verificação do nome do host durante a autenticação SSL.
    context.check_hostname = False
    # o certificado do servidor não será verificado
    context.verify_mode = ssl.CERT_NONE
    # criação do socket/ conexão com o server (IPV4/TCP)
    socket_TCP_IPV4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Envolve o socket criado anteriormente em uma conexão segura (wrap_socket)
    socket_conexão = context.wrap_socket(socket_TCP_IPV4, server_hostname=url_host)
    try:
        # estabelece a conexão
        socket_conexão.connect((url_host, 443))
        # enviando requisição pedida acima
        socket_conexão.send(url_request.encode('utf-8'))
    except:
        print(f'Erro...{sys.exc_info()[0]}')
        exit()
    print('\nBaixando a imagem...\n')
    # recebendo a resposta 
    data_ret = b''
    dados_recebidos = 0
    content_length = 0
    try:
        while True:
            # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            data = socket_conexão.recv(buffer_size)
            if not data: 
                break
            data_ret += data
            dados_recebidos += len(data)
            position  = data_ret.find('\r\n\r\n'.encode())
            headers   = data_ret[:position] 
            inicio_length = headers.find(b'Content-Length:')
            final_length = headers.find(b'\r\n', inicio_length)
            content_length = headers[inicio_length+15:final_length]
    except:
        print(f'Erro...{sys.exc_info(0)}')  
        exit()  
    # fechando conexão
    socket_conexão.close()
    return data_ret, headers, content_length

def socket_http (url_image, url_host, buffer_size):
    # define a requisição 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
    # criando conexão IPV4(AF.INET) e TCP(SOCK_STREAM)
    socket_conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Realizando a conexão
        socket_conexão.connect((url_host, 80))
        # enviando requisição pedida acima
        socket_conexão.sendall(url_request.encode('utf-8'))
    except:
        print(f'Erro...{sys.exc_info()[0]}')    
        exit()
    print('\nBaixando a imagem...')
    #Recebendo os dados
    data_ret = b''
    try:
        while True:
            # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            data = socket_conexão.recv(buffer_size)
            if not data: 
                break
            data_ret += data
    except ConnectionResetError:
        print('Erro... a conexão foi forçadamente encerrada pelo host remoto.\n')
        print('='*100)
        exit()
    except:
        print(f'Erro...{sys.exc_info()[0]}')
        exit()
    # fechando conexão
    socket_conexão.close()
    return data_ret