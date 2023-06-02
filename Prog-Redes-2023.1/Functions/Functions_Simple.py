import os, sys

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def split_url (url):
    try:
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
        return url_host, url_image, arq_image, extensão, arq_txt, protocolo
    except:
        print(f'\nErro na Fragmentação da URL...{sys.exc_info()[0]}\n')

def content_length (headers):
    linhas = headers.strip().split('\n')
    for x in linhas:
        if x.startswith('Content-Length:'):
            linha_length = x
            break
    return int(linha_length[16:])

def content_type (headers):
    try:
        linhas = headers.strip().split('\n')
        for x in linhas:
            if x.startswith('Content-Type:'):
                extensão = x.strip().split('/')[1]
                break
        html_verification = extensão.find(';')
        if html_verification != -1:
            extensão = extensão.split(';')[0]
        return extensão
    except:
        print(f'\nErro na captura do Content-Type...{sys.exc_info()[0]}\n')