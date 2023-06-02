import socket, ssl, sys, time, Functions_Simple

# verifica se a url é HTTP ou HTTPS
def socket_https(url_image, url_host, buffer_size):
    # define a requisição 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\nConnection: close\r\n\r\n' 
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
        print(f'Erro na conexão do socket...{sys.exc_info()[0]}')
        exit()
    print('\nBaixando a imagem...')
    # recebendo a resposta 
    data_ret = b''
    dados_recebidos = 0
    type_arq = ''
    try:
        start_time = time.time()
        while True:
            # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            data = socket_conexão.recv(buffer_size)
            if not data: 
                break
            data_ret += data
            # joga na variavel o quanto de bytes já foram recebidos
            dados_recebidos += len(data)
            # pegando o cabeçalho 
            position  = data_ret.find('\r\n\r\n'.encode())
            headers   = data_ret[:position] 
            # função para capturar o content length no header
            content_length = Functions_Simple.content_length(headers)
            Content_type = Functions_Simple.content_type(headers)
            # printando na tela usando Dtdout.write (para escrever print sob print)
            sys.stdout.write(f'\rBytes baixados: {dados_recebidos} / {content_length} bytes')
            # flush para criar um buffer dos prints e ter sensação de carregamento
            sys.stdout.flush()
        print('\nDownload Concluído...\n')
        end_time = time.time()
        tempo_total = end_time - start_time
        # para ver o tempo total decorrido
        print(f'Tempo total: {tempo_total:.2f}s\n')
    except:
        print(f'Erro no recebimento dos dados...{sys.exc_info()[0]}')  
        exit()  
    # fechando conexão
    socket_conexão.close()
    return data_ret, headers, Content_type

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
        print(f'Erro na conexão do socket...{sys.exc_info()[0]}')    
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