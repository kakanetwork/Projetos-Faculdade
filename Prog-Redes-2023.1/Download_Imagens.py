import sys
diretorio_atual = os.path.dirname(os.path.abspath(__file__)) 
sys.path.append(diretorio_atual + '\\Functions')
import platform, Functions_Socket, Functions_Simple

# ------------------------------------------------------------------------------------------------------------

Functions_Simple.clear_terminal()

# ------------------------------------------------------------------------------------------------------------

print('='*100)
url = str(input('\ninforme a url: '))

# ------------------------------------------------------------------------------------------------------------

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
    Functions_Socket.socket_https(url_image, url_host, buffer_size)

elif protocolo =='http':
    Functions_Socket.socket_http(url_image, url_host, buffer_size)

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
