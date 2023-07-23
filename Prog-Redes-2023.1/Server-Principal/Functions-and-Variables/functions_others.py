import sys, os, logging
from variables import *

loggerServer  = logging.getLogger('Server')

# ============================================================================================================


''' FUNÇÃO PARA EVITAR A REPETIÇÃO DE CÓDIGO DE ENVIOS '''

def MESSAGE_CLIENT(sock, msg):
    try:
        sock.send(msg.encode(UNICODE))
    except:
        loggerServer.error(f'\nErro ao enviar mensagem para o cliente...{sys.exc_info()[0]}')

# ============================================================================================================

''' REALIZA A PROCURA DO CONTENT_LENGHT DO ARQUIVO '''

def CONTENT_LENGHT (headers): # FUNÇÃO PARA RETIRAR O CONTENT-LENGTH DO HEADER DE UM ARQUIVO
    try:
        lines = headers.strip().split('\n')  # pego o header já decodificado e quebro ele em linhas
        for line in lines:
            if line.lower().startswith('content-length:'): # vasculho nessas linhas o content-length por meio do startswich que retorna True quando a palavra existir
                linha_length = int(line[16:]) # transforma em int e pega somente da posição 16 em diante
                return linha_length 
    except:
        loggerServer.warning(f'\nErro na captura do Content-Lenght...{sys.exc_info()[0]}')

# ============================================================================================================

''' REALIZA A PROCURA DO CONTENT_TYPE DO ARQUIVO '''

def CONTENT_TYPE (headers): # FUNÇÃO PARA RETIRAR O CONTENT-TYPE DO HEADER DE UM ARQUIVO
    try:
        lines = headers.strip().split('\n') # pego o header já decodificado e quebro ele em linhas
        for line in lines:
            if line.lower().startswith('content-type:'): # vasculho nessas linhas o content-type por meio do startswich que retorna True quando a palavra existir
                extensao = line.strip().split('/')[1] # pego a linha do Content-type, retiro os espaços com strip() e quebro com split() onde tiver uma barra
                return extensao
    except:
        loggerServer.error(f'\nErro na captura do Content-Type...{sys.exc_info()[0]}')

# ============================================================================================================

''' REALIZA A QUEBRA DA URL SOMENTE NOS PARAMETROS QUE EU QUERO TER '''


def SPLIT_URL (url): # FUNÇÃO PARA QUEBRAR A URL E PEGAR INFORMAÇÕES IMPORTANTES
    url_fragmentada = url.split('/')
    hostname = url_fragmentada[2]
    localarquive = '/'+'/'.join(url_fragmentada[3:])
    if '.' in url_fragmentada[-1]:
        arquivename = url_fragmentada[-1].split('.')[0]
    else:
        arquivename = url_fragmentada[-1]
    if len(arquivename) >= 150:
        arquivename = arquivename[0:150]
    caracteres_bloqueados = ['/', ':', '*', '?', '|', '<', '>', '"', '\\']
    for x in caracteres_bloqueados: # retirando caracteres que são proibidos de ter no nome de um arquivo, para salvar...
        arquivename = arquivename.replace(x, '') 
    protocol = url.split(':')[0]
    return hostname, localarquive, arquivename, protocol

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR PRINT ORGANIZADO '''

def PRINT_DIV(dados):
    print('\n'+'-'*100)
    print(dados)
    print('-'*100)

# ============================================================================================================

''' FUNÇÃO PARA REALIZAR SPLIT DO COMANDO DO CLIENTE '''

def COMAND_SPLIT(msg):
    try:
        msg_split = msg.split(':')
    except:
        loggerServer.error(f'\nErro no Split do Comand...{sys.exc_info()[0]}')  
        exit() 
    return msg_split

# ============================================================================================================

def CREATE_PAST(name):
    try:
        os.makedirs(name, exist_ok=True)
    except:
        loggerServer.error(f'\nErro na Criação da Pasta...{sys.exc_info()}')  
        exit()      

# ============================================================================================================
