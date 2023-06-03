import socket, ssl, sys, time, Functions_Simple

def download_file_https(localarquive, hostname, buffer_size):
    requisição = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\nConnection: close\r\n\r\n'    # define a requisição 
    context = ssl.create_default_context()      # criação do contexto SSL para conexão HTTPS
    context.check_hostname = False      # desativa a verificação do nome do host durante a autenticação SSL.
    context.verify_mode = ssl.CERT_NONE     # o certificado do servidor não será verificado
    socket_TCP_IPV4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # criação do socket/ conexão com o server (IPV4/TCP)
    socket_conexão = context.wrap_socket(socket_TCP_IPV4, server_hostname=hostname)     # Envolve o socket criado anteriormente em uma conexão segura (wrap_socket)
    try:
        socket_conexão.connect((hostname, 443))     # estabelece a conexão
        socket_conexão.send(requisição.encode('utf-8'))     # enviando requisição pedida acima
    except:
        print(f'Erro na conexão do socket...{sys.exc_info()[0]}')
        exit()
    print('\nBaixando o arquivo...')
    data_ret = b'' 
    dados_recebidos = 0
    try:
        content_length = -1
        start_time = time.time()   # iniciando contagem de tempo
        while True:     # recebendo a resposta 
            data = socket_conexão.recv(buffer_size)    # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            if not data: 
                break
            data_ret += data
            dados_recebidos += len(data)    # joga na variavel o quanto de bytes já foram recebidos
            position  = data_ret.find('\r\n\r\n'.encode())
            headers   = data_ret[:position].decode('utf-8')   # pegando o cabeçalho 
            try:
                content_length = Functions_Simple.content_length(headers)    # função para capturar o content length no header
                print(f'\rBytes baixados: {dados_recebidos} / {content_length} bytes', end='')
            except:
                pass    # passando pois o content_length não é vital para o código
        if content_length == -1:
            print('Não foi possivel capturar o Content_Lenght...')  # criando um aviso para quando o content lenght não for pego 
        arquivo_dados = data_ret[position+4:]   # pegando os dados do arquivo
        Content_type = Functions_Simple.content_type(headers) # usando a função para pegar a extensão do arquivo pelo header
        print('\nDownload Concluído...\n')
        end_time = time.time() 
        tempo_total = end_time - start_time
        print(f'Tempo total: {tempo_total:.2f}s\n') # informando o tempo total de download
    except KeyboardInterrupt:
        print('\nVocê encerrou o programa com sucesso!\n')
    except:
        print(f'\nErro no recebimento dos dados...{sys.exc_info()[0]}')  
        exit()  
    socket_conexão.close() # fechando a conexão
    return data_ret, headers, arquivo_dados, Content_type

def socket_http (localarquive, hostname, buffer_size):
    # define a requisição 
    requisição = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\n\r\n' 
    # criando conexão IPV4(AF.INET) e TCP(SOCK_STREAM)
    socket_conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Realizando a conexão
        socket_conexão.connect((hostname, 80))
        # enviando requisição pedida acima
        socket_conexão.sendall(requisição.encode('utf-8'))
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