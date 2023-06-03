import sys, os
diretorio_atual = os.path.dirname(os.path.abspath(__file__)); sys.path.append(diretorio_atual + '\\Functions')
import Functions_Download_File, Functions_Simple, Functions_Decorative

"IMPORTANTE: ANTES DA EXECUÇÃO DO CÓDIGO FAÇA O DOWNLOAD DA PASTA (FUNCTIONS) ONDE CONTÉM AS FUNÇÕES PARA O FUNCIONAMENTO DESTE CÓDIGO!"

# ------------------------------------------------------------------------------------------------------------
Functions_Simple.clear_terminal() # utilizando função para dar clear no terminal
print('='*100); frase = 'Downloader Files'; Functions_Decorative.ascii_art(frase); print('\t\t\tCreated by Kakanetwork')
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
hostname, localarquive, arquivename, extensão, nameheader, protocol = Functions_Simple.split_url(url) # utilizando função fragmentar a url e pegar apenas o pedido

print('\n'+'='*100)
print(f"\nhostname: {hostname}\nlocal_do_arquivo: {localarquive}\nnome_do_arquivo: {arquivename}\nextensão (presente na URL): {extensão}\nprotocolo: {protocol}\n"); print('='*100)
# ------------------------------------------------------------------------------------------------------------ 
buffer_size = 4096

if protocol == 'https':
    # realizando toda conexão/envio/recebimento com função no protocolo HTTPS
    data_ret, headers, arquivo_dados, Content_type = Functions_Download_File.download_file_https(localarquive, hostname, buffer_size)
elif protocol =='http':
    # realizando toda conexão/envio/recebimento com função no protocolo HTTPS
    data_ret, headers, arquivo_dados, Content_type = Functions_Download_File.socket_http(localarquive, hostname, buffer_size)
else:
    print('\nprotocolo não suportado, em desenvolvimento.... (Utilize URLs HTTP ou HTTPS)\n'); print('='*100)
    exit()
# ------------------------------------------------------------------------------------------------------------
print('='*100,'\n', '\nHEADER DO ARQUIVO:\n')
print(headers) # printando o head
print('\n','='*100)

diretorio_header = diretorio_atual + f'\\{nameheader}' # salvando o head em um arquivo

try:
    with open(diretorio_header, 'w', encoding='utf-8') as header:
        header.write(headers)
except:
    print(f'Erro no save do header...{sys.exc_info()[0]}')
    exit()
# -----------------------------------------------------------------------------------------------------------
caracteres_bloqueados = ['/', ':', '*', '?', '|', '<', '>', '"', '\\']
for x in caracteres_bloqueados:
    arquivename = arquivename.replace(x, '')

nome_arquivo = f'{arquivename}.' + Content_type
diretorio_arquivo = diretorio_atual + f'\\{nome_arquivo}'
try:
    with open(diretorio_arquivo, 'wb') as arquivo:
        arquivo.write(arquivo_dados)
except:
    print(f'Erro no save do arquivo...{sys.exc_info()[0]}')
    exit()
# ------------------------------------------------------------------------------------------------------------