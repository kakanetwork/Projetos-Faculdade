import sys, os
diretorio_atual = os.path.dirname(os.path.abspath(__file__)); sys.path.append(diretorio_atual + '\\Functions')
import Functions_Download_File, Functions_Socket_Connection
from Functions_Simple import clear_terminal, split_url
from Functions_Decorative import ascii_art

"IMPORTANTE: ANTES DA EXECUÇÃO DO CÓDIGO FAÇA O DOWNLOAD DA PASTA (FUNCTIONS) ONDE CONTÉM AS FUNÇÕES PARA O FUNCIONAMENTO DESTE CÓDIGO!"
"BIBLIOTECAS NECESSÁRIAS: SYS, OS, SSL, SOCKET, TIME, PYFIGLET(OPCIONAL)"

# ------------------------------------------------------------------------------------------------------------

clear_terminal() # utilizando função para dar clear no terminal
print('='*100); frase = 'Downloader Files'; ascii_art(frase); print('\t\t\tCreated by Kakanetwork')
print('Extensões Suportadas: Todas Extensões de Aúdio,Vídeo e Imagem, além de PDF, JS, HTML,')

# ------------------------------------------------------------------------------------------------------------

try:
    print('='*100); url = str(input('\ninforme a url: '))
except KeyboardInterrupt:
    print('\nVocê encerrou o programa com sucesso!\n')
    exit()
except:
    print(f'Erro na inserção da URL...{sys.exc_info()[0]}')
    exit()    

# ------------------------------------------------------------------------------------------------------------

hostname, localarquive, arquivename, nameheader, protocol = split_url(url) # utilizando função fragmentar a url e pegar apenas o pedido

print('\n'+'='*100)
print(f"\nhostname: {hostname}\nlocal_do_arquivo: {localarquive}\nnome_do_arquivo: {arquivename}\nprotocolo: {protocol}\n"); print('='*100)

# ------------------------------------------------------------------------------------------------------------ 

buffer_size = 4096

if protocol == 'https':
    socket_conexão = Functions_Socket_Connection.socket_https(localarquive, hostname) 
elif protocol =='http':
    socket_conexão = Functions_Socket_Connection.socket_http(localarquive, hostname)
else:
    print('\nprotocolo não suportado, em desenvolvimento.... (Utilize URLs HTTP ou HTTPS)\n'); print('='*100)
    exit()

headers, arquivo_dados, Content_type = Functions_Download_File.download_file(socket_conexão, buffer_size)

# ------------------------------------------------------------------------------------------------------------

print('='*100,'\n', '\nHEADER DO ARQUIVO:\n')
print(headers) # printando o head
print('\n','='*100)

diretorio_header = diretorio_atual + f'\\{nameheader}'
try:
    with open(diretorio_header, 'w', encoding='utf-8') as header:  # salvando o head em um arquivo
        header.write(headers)
except:
    print(f'Erro no save do header...{sys.exc_info()}')
    exit()

# -----------------------------------------------------------------------------------------------------------

if Content_type == 'Javascript':
    Content_type = 'js'

nome_arquivo = f'{arquivename}.' + Content_type
diretorio_arquivo = diretorio_atual + f'\\{nome_arquivo}'
try:
    with open(diretorio_arquivo, 'wb') as arquivo: # salvando o arquivo 
        arquivo.write(arquivo_dados)
except:
    print(f'Erro no save do arquivo...{sys.exc_info()[0]}')
    exit()

# ------------------------------------------------------------------------------------------------------------