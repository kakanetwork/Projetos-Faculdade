import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def split_url (url):
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