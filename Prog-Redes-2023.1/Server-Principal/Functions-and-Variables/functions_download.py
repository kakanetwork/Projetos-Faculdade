
import socket, sys, ssl, logging
from variables import *
from functions_others import *

loggerServer  = logging.getLogger('Server')

# ============================================================================================================

def SOCKET_HTTPS(localarquive, hostname):
    requisição = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\nConnection: close\r\n\r\n'    # define a requisição 
    context = ssl.create_default_context()      # criação do contexto SSL para conexão HTTPS
    context.check_hostname = False      # desativa a verificação do nome do host durante a autenticação SSL.
    context.verify_mode = ssl.CERT_NONE     # o certificado do servidor não será verificado
    socket_TCP_IPV4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # criação do socket/ conexão com o server (IPV4/TCP)
    socket_conexão = context.wrap_socket(socket_TCP_IPV4, server_hostname=hostname)     # Envolve o socket criado anteriormente em uma conexão segura (wrap_socket)
    socket_conexão.connect((hostname, 443))     # estabelece a conexão
    socket_conexão.send(requisição.encode(UNICODE))     # enviando requisição pedida acima
    return socket_conexão # retornando conexão 


# ============================================================================================================


def SOCKET_HTTP(localarquive, hostname):
    requisição = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\nConnection: close\r\n\r\n'
    socket_conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conexão.connect((hostname, 80))
    socket_conexão.sendall(requisição.encode(UNICODE))
    return socket_conexão

# ============================================================================================================

def DOWNLOAD_WEB(socket_conexão, sock_client):
    data_ret = b'' 
    dados_recebidos = 0
    try:
        content_lenght = -1
        msg_download = f'\nDownload do Arquivo foi Iniciado!\n'
        MESSAGE_CLIENT(sock_client, msg_download)
        while True:     # recebendo a resposta 
            data = socket_conexão.recv(BUFFER)    # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            if not data: 
                break
            data_ret += data
            dados_recebidos += len(data)    # joga na variavel o quanto de bytes já foram recebidos
            position  = data_ret.find('\r\n\r\n'.encode())
            headers   = data_ret[:position].decode('utf-8').lower()   # pegando o cabeçalho 
            try:
                content_lenght = CONTENT_LENGHT(headers)    # função para capturar o content length no header
                msg_download = f'\rBytes baixados: {dados_recebidos} / {content_lenght} bytes'
                MESSAGE_CLIENT(sock_client, msg_download)
            except: pass  # passando pois o content_lenght não é vital para o código
        if content_lenght == -1:
            msg_size = 'Não foi possivel capturar o Content_Lenght...'
            MESSAGE_CLIENT(sock_client, msg_size) # criando um aviso para quando o content lenght não for pego 
        arquivo_dados = data_ret[position+4:]   # pegando os dados do arquivo
        content_type = CONTENT_TYPE(headers) # usando a função para pegar a extensão do arquivo pelo header
        msg_download = f'\nO Download do arquivo foi concluído!\n'
        MESSAGE_CLIENT(sock_client, msg_download)
    except:
        loggerServer.error(f'\nErro no recebimento dos dados do Download Web...{sys.exc_info()}')  
        exit()  
    socket_conexão.close() # fechando a conexão
    return headers, arquivo_dados, content_type
    
# ============================================================================================================


