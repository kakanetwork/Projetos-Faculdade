import socket, sys, ssl, os, platform
from Functions_01 import *
# ------------------------------------------------------------------------------------------------------------

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

# ------------------------------------------------------------------------------------------------------------

print('='*100)
url = str(input('\ninforme a url: '))

# ------------------------------------------------------------------------------------------------------------

# pegando meu dir atual (será usado mais a frente)
diretorio_atual = os.path.dirname(os.path.abspath(__file__)) 

# fragmenta a URL usando a '/' como referencia
url_fragmentada = url.split('/')

# pega apenas o host 
url_host = url_fragmentada[2]

# pega o local da imagem
url_image = '/'+'/'.join(url_fragmentada[3:])

# pega o nome da imagem + extensão
arq_image = url_fragmentada[-1]

# pega a extensão e converte para txt (será utlizado posteriomente para save do HEAD)
extensão = arq_image.split('.')[-1]
arq_txt = arq_image.replace(extensão, 'txt')

# pega o protocolo (HTTP ou HTTPS)
protocolo = url.split(':')[0]

print('\n'+'='*100)
print(f"\nhostname: {url_host}\nlocal_da_imagem: {url_image}\nnome_da_imagem: {arq_image}\nextensão: {extensão}\nprotocolo: {protocolo}\n")
print('='*100)

# ------------------------------------------------------------------------------------------------------------
 
# define o tamanho do buffer 
buffer_size = 1024 

# verifica se a url é HTTP ou HTTPS
if protocolo == 'https':

    # define a requisição 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

    # criação do contexto SSL para conexão HTTPS
    context = ssl.create_default_context()

    # desativa a verificação do nome do host durante a autenticação SSL.
    context.check_hostname = False

    # o certificado do servidor não será verificado
    context.verify_mode = ssl.CERT_NONE

    # criação do socket/ conexão com o server (IPV4/TCP)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Envolve o socket criado anteriormente em uma conexão segura (wrap_socket)
    socket_conexão = context.wrap_socket(socket, server_hostname=url_host)

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
    try:
        while True:

            # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            data = socket_conexão.recv(buffer_size)
            if not data: 
                break
            data_ret += data
    except:
        print(f'Erro...{sys.exc_info(0)}')  
        exit()  

    # fechando conexão
    socket_conexão.close()

# ------------------------------------------------------------------------------------------------------------

elif protocolo =='http':

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

else:
    print('\nProtocolo não suportado, em desenvolvimento.... (Utilize URLs HTTP ou HTTPS)\n')
    print('='*100)
    exit()

# ------------------------------------------------------------------------------------------------------------
     
# Separando o Head da Imagem
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

# ------------------------------------------------------------------------------------------------------------

# printando o head
print('='*100,'\n')
print(str(headers, 'utf-8'),'\n')
print('='*100)

dir1 = diretorio_atual + f'\\{arq_txt}'

# salvando o head em um arquivo
try:
    with open(dir1, 'w', encoding='utf-8') as header:
        header.write(headers.decode('utf-8'))
except:
    print(f'Erro...{sys.exc_info()[0]}')
    exit()

# ------------------------------------------------------------------------------------------------------------

dir_head = diretorio_atual + f'\\{arq_txt}'
chave_extensão = 'Content-Type'
try:
    with open(dir_head, 'r', encoding='utf-8') as read_header:
        for x in read_header:
            if chave_extensão in x:
                extensão_head = x.split('/')[1].strip()
except:
    print(f'Erro...{sys.exc_info()[0]}')
    exit()

# ------------------------------------------------------------------------------------------------------------

nome_imagem = 'imagem' + f'.{extensão_head}'
dir2 = diretorio_atual + f'\\{nome_imagem}'
# Salvando a imagem
try:
    with open(dir2, 'wb') as imagem:
        imagem.write(image)
except:
    print(f'Erro...{sys.exc_info()[0]}')
    exit()

# ------------------------------------------------------------------------------------------------------------
