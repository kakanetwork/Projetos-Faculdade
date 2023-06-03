import socket, sys, ssl
    
    
def socket_https(localarquive, hostname):
    requisição = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\nConnection: close\r\n\r\n'    # define a requisição 
    context = ssl.create_default_context()      # criação do contexto SSL para conexão HTTPS
    context.check_hostname = False      # desativa a verificação do nome do host durante a autenticação SSL.
    context.verify_mode = ssl.CERT_NONE     # o certificado do servidor não será verificado
    socket_TCP_IPV4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # criação do socket/ conexão com o server (IPV4/TCP)
    socket_conexão = context.wrap_socket(socket_TCP_IPV4, server_hostname=hostname)     # Envolve o socket criado anteriormente em uma conexão segura (wrap_socket)
    
    # -----------------------------------------------------------------------------------------------------------

    try:
        socket_conexão.connect((hostname, 443))     # estabelece a conexão
        socket_conexão.send(requisição.encode('utf-8'))     # enviando requisição pedida acima
    except:
        print(f'Erro na conexão do socket...{sys.exc_info()[0]}')
        exit()
    return socket_conexão # retornando conexão 

































def socket_http(localarquive, hostname):
    requisição = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\nConnection: close\r\n\r\n'
    socket_conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_conexão.connect((hostname, 80))
        socket_conexão.sendall(requisição.encode('utf-8'))
    except:
        print(f'Erro na conexão do socket...{sys.exc_info()[0]}')    
        exit()
    return socket_conexão