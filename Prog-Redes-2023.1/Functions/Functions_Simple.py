import os, sys

def clear_terminal(): # FUNÇÃO PARA DAR CLEAR NO TERMINAL
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def split_url (url): # FUNÇÃO PARA QUEBRAR A URL E PEGAR INFORMAÇÕES IMPORTANTES
    try:
        url_fragmentada = url.split('/')
        hostname = url_fragmentada[2]
        localarquive = '/'+'/'.join(url_fragmentada[3:])
        arquivename = url_fragmentada[-1]

        if len(arquivename) >= 150:
            arquivename = arquivename[0:150]

        caracteres_bloqueados = ['/', ':', '*', '?', '|', '<', '>', '"', '\\']
        for x in caracteres_bloqueados: # retirando caracteres que são proibidos de ter no nome de um arquivo, para salvar...
            arquivename = arquivename.replace(x, '') 

        nameheader = arquivename + '.txt'
        protocol = url.split(':')[0]
        if protocol == 'blob':
            protocol = url.split(':')[1]
        return hostname, localarquive, arquivename, nameheader, protocol
    except IndexError:
        print('\nInforme a URL corretamente... (tente novamente)!\n')
        exit()
    except:
        print(f'\nErro na Fragmentação da URL...{sys.exc_info()[0]}\n')
        exit()

def content_length (headers): # FUNÇÃO PARA RETIRAR O CONTENT-LENGTH DO HEADER DE UM ARQUIVO
    linhas = headers.strip().split('\n')  # pego o header já decodificado e quebro ele em linhas
    for x in linhas:
        if x.startswith('Content-Length:'): # vasculho nessas linhas o content-length por meio do startswich que retorna True quando a palavra existir
            linha_length = int(x[16:]) # transforma em int e pega somente da posição 16 em diante
            break
    return linha_length 

def content_type (headers): # FUNÇÃO PARA RETIRAR O CONTENT-TYPE DO HEADER DE UM ARQUIVO
    try:
        linhas = headers.strip().split('\n') # pego o header já decodificado e quebro ele em linhas
        for x in linhas:
            if x.startswith('Content-Type:'): # vasculho nessas linhas o content-type por meio do startswich que retorna True quando a palavra existir
                extensão = x.strip().split('/')[1] # pego a linha do Content-type, retiro os espaços com strip() e quebro com split() onde tiver uma barra
                break # com isso para o for, pois já tenho a extensão
        html_verification = extensão.find(';') # EXCEÇÃO: quando a url é de um arquivo HTML, temos que fazer um filtro diferente para conseguir pegar a extensão
        if html_verification != -1:
            extensão = extensão.split(';')[0] # usamos split() para quebrar a extensão onde tiver ';' e pego o primeiro resultado 
                                              # formato content type HTML -> html; charset = utf-8
        return extensão
    except:
        print(f'\nErro na captura do Content-Type...{sys.exc_info()[0]}\n')