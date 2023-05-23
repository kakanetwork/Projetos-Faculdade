import socket


#url = input('informa a url: ')
url = str('https://www.nasa.gov/sites/default/files/thumbnails/image/nasa-logo-web-rgb.png')



url_fragmentada = url.split('/')
url_host = url_fragmentada[2]
url_image = '/'.join(url_fragmentada[3:-1])
arq_image = url_fragmentada[-1]

extensão = arq_image.split('.')[-1]
arq_txt = arq_image.replace(extensão, 'txt')

protocolo = url.split(':')[0]

if protocolo == 'https':
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
    host_port   = 443
    buffer_size = 1024
elif protocolo =='http':
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
    host_port   = 80
    buffer_size = 1024
else:
    print('Erro...')

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, host_port))
sock_img.sendall(url_request.encode())

print('\nBaixando a imagem...')


# Montado a variável que armazenará os dados de retorno
data_ret = b''
while True:
    data = sock_img.recv(buffer_size)
    if not data: break
    data_ret += data

sock_img.close()

# Obtendo o tamanho da imagem
img_size = -1
tmp = data_ret.split('\r\n'.encode())
for line in tmp:
   if 'Content-Length:'.encode() in line:
      img_size = int(line.split()[1])
      break
print(f'\nTamanho da Imagem: {img_size} bytes')

# Separando o Cabeçalho dos Dados
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

# Salvando a imagem
file_output = open('image.png', 'wb')
file_output.write(image)
file_output.close()