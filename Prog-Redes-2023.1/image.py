import socket, sys, ssl, os, platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

#url = input('informa a url: ')
url = str('https://www.nasa.gov/sites/default/files/thumbnails/image/nasa-logo-web-rgb.png')

# fragmenta toda a URL
url_fragmentada = url.split('/')

# pega apenas o host do fragmento acima
url_host = url_fragmentada[2]

# pega o local da imagem
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

# Define a porta se a url for HTTP ou HTTPS
if protocolo == 'https':
    buffer_size = 1024 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
    context         = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    socket = socket.socket((socket.AF_INET))
    socket_rss      = socket.create_connection((url_host, 443))
    sock_img = context.wrap_socket(socket_rss, server_hostname=url_host)

    sock_img.send(url_request.encode('utf-8'))
    print('\nBaixando a imagem...')

elif protocolo =='http':
    buffer_size = 1024
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
    sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_img.connect((url_host, 80))
    sock_img.sendall(url_request.encode())
    print('\nBaixando a imagem...')

else:
    print('\nProtocolo não suportado...\n')
    exit()


# Montado a variável que armazenará os dados de retorno
data_ret = b''
while True:
    data = sock_img.recv(buffer_size)
    if not data: 
        break
    data_ret += data

sock_img.close()

# Obtendo o tamanho da imagem
img_size = -1
tmp = data_ret.split('\r\n'.encode())
for line in tmp:
   if 'Content-Length:'.encod6e() in line:
      img_size = int(line.split()[1])
      break
print(f'Tamanho da Imagem: {img_size} bytes\n')

# Separando o Cabeçalho dos Dados
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

print('='*100,'\n')
# salvando head
print(str(headers, 'utf-8'),'\n')
print('='*100)

with open('saida.txt', 'w', encoding='utf-8') as header:
    header.write(headers.decode('utf-8'))

# Salvando a imagem
file_output = open('image.png', 'wb')
file_output.write(image)
file_output.close()