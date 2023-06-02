import sys, os
diretorio_atual = os.path.dirname(os.path.abspath(__file__)) 
sys.path.append(diretorio_atual + '\\Functions')
import Functions_Socket, Functions_Simple

# ------------------------------------------------------------------------------------------------------------

# utilizando função para dar clear no terminal
Functions_Simple.clear_terminal()

# ------------------------------------------------------------------------------------------------------------

print('='*100)
url = str(input('\ninforme a url: '))

# ------------------------------------------------------------------------------------------------------------

# utilizando função fragmentar a url e pegar apenas o pedido
url_host, url_image, arq_image, extensão, arq_txt, protocolo = Functions_Simple.split_url(url)

print('\n'+'='*100)
print(f"\nhostname: {url_host}\nlocal_da_imagem: {url_image}\nnome_da_imagem: {arq_image}\nextensão: {extensão}\nprotocolo: {protocolo}\n"); print('='*100)

# ------------------------------------------------------------------------------------------------------------ 
 
# define o tamanho do buffer 
buffer_size = 1024 

if protocolo == 'https':
    # realizando toda conexão/envio/recebimento com função no protocolo HTTPS
    data_ret,headers,Content_type = Functions_Socket.socket_https(url_image, url_host, buffer_size)
elif protocolo =='http':
    # realizando toda conexão/envio/recebimento com função no protocolo HTTPS
    data_ret = Functions_Socket.socket_http(url_image, url_host, buffer_size)
else:
    print('\nProtocolo não suportado, em desenvolvimento.... (Utilize URLs HTTP ou HTTPS)\n'); print('='*100)
    exit()

# ------------------------------------------------------------------------------------------------------------

# Separando o Head da Imagem
position  = data_ret.find('\r\n\r\n'.encode())
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
    print(f'Erro no save do header...{sys.exc_info()[0]}')
    exit()

# ------------------------------------------------------------------------------------------------------------

nome_imagem = 'arquivo' + f'.{Content_type}'
dir2 = diretorio_atual + f'\\{nome_imagem}'
# Salvando a imagem com o formato (extensão) que conseguimos na parte anterior
try:
    with open(dir2, 'wb') as imagem:
        imagem.write(image)
except:
    print(f'Erro no save da imagem...{sys.exc_info()[0]}')
    exit()

# ------------------------------------------------------------------------------------------------------------