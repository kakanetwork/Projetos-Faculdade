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
    try:
        inicio_length = headers.find(b'Content-Length:')
        final_length = headers.find(b'\r\n', inicio_length)
        # pego apenas a variavel do tamanho e transformo em inteiro (+16 corresponde ao nome 'content_length: ')
        content_length = int(headers[inicio_length+16:final_length])
        return content_length
    except: 
        print(f'\nErro na captura do Content-Length...{sys.exc_info()[0]}\n')

def content_type (headers):
    try:
        inicio_type = headers.find(b'Content-Type:')       
        final_type = headers.find(b'\r\n', inicio_type)
        type_complete = headers[inicio_type+14:final_type]
        type_resume = type_complete.decode('utf-8').split('/')[1]
        return type_resume
    except:
        print(f'\nErro na captura do Content-Type...{sys.exc_info()[0]}\n')