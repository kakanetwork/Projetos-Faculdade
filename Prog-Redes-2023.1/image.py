import socket, sys, ssl, os, platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('='*100)
#url = input('informa a url: ')
url = str('http://portal.mec.gov.br/images/comunicado/govbr.png')

# fragmenta toda a URL
url_fragmentada = url.split('/')

# pega apenas o host do fragmento acima
url_host = url_fragmentada[2]

# pega o local da imagem
# adiciona o '/'+'/' para iniciar com uma /
url_image = '/'+'/'.join(url_fragmentada[3:])

# pega o nome da imagem + extensão
arq_image = url_fragmentada[-1]

# pega apenas a extensão e converte para txt
extensão = arq_image.split('.')[-1]
arq_txt = arq_image.replace(extensão, 'txt')

# pega o protocolo (HTTP ou HTTPS)
protocolo = url.split(':')[0]
print('='*100)
print(f"\nhostname: {url_host}\nlocal_da_imagem: {url_image}\nnome_da_imagem: {arq_image}\nextensão: {extensão}\nprotocolo: {protocolo}\n")
print('='*100)

# define o tamanho do buffer 
buffer_size = 1024 

# verifica a porta se a url for HTTP ou HTTPS
if protocolo == 'https':
    # define a requisição 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

    # criação da conexão segura (SSL)
    context         = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # criação do socket/ conexão com o server 
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conexão = context.wrap_socket(socket, server_hostname=url_host)
    socket_conexão.connect((url_host, 443))

    # enviando requisição pedida acima
    socket_conexão.send(url_request.encode('utf-8'))

    print('\nBaixando a imagem...\n')

    # recebendo a resposta

    data_ret = b''
    try:
        while True:
            data = socket_conexão.recv(buffer_size)
            if not data: 
                break
            data_ret += data
    except:
        print(f'Erro...{sys.exc_info(0)}')    
    # fechando conexão
    socket_conexão.close()


elif protocolo =='http':

    # define a requisição 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

    # criando conexão IPV4(AF.INET) e TCP(SOCK_STREAM)
    socket_conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conexão.connect((url_host, 80))

    # enviando requisição pedida acima
    socket_conexão.sendall(url_request.encode('utf-8'))

    print('\nBaixando a imagem...')

    #RRecebendo os dados
    data_ret = b''
    try:
        while True:
            data = socket_conexão.recv(buffer_size)
            if not data: 
                break
            data_ret += data
    except ConnectionResetError:
        print('Erro... a conexão foi forçadamente encerrada pelo host remoto.')
    except:
        print(f'Erro...{sys.exc_info(0)}')
    # fechando conexão
    socket_conexão.close()

# Separando o Cabeçalho dos Dados
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

print('='*100,'\n')
# printando o head
print(str(headers, 'utf-8'),'\n')
print('='*100)

# salvando o head em um arquivo
with open(arq_txt, 'w', encoding='utf-8') as header:
    header.write(headers.decode('utf-8'))

# Salvando a imagem
file_output = open('image.png', 'wb')
file_output.write(image)
file_output.close()