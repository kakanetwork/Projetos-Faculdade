import os, sys

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def split_url (url):
    try:
        url_fragmentada = url.split('/')
        hostname = url_fragmentada[2]
        localarquive = '/'+'/'.join(url_fragmentada[3:])
        arquivename = url_fragmentada[-1]
        extensão = arquivename.split('.')[-1]
        nameheader = arquivename.replace(extensão, 'txt')
        protocol = url.split(':')[0]
        return hostname, localarquive, arquivename, extensão, nameheader, protocol
    except IndexError:
        print('\nInforme a URL corretamente... (tente novamente)!\n')
        exit()
    except:
        print(f'\nErro na Fragmentação da URL...{sys.exc_info()[0]}\n')
        exit()

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