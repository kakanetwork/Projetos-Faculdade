import socket, ssl, sys
import xml.etree.ElementTree as ET

# Constantes da Aplicação 
# https://www.gazetadopovo.com.br/feed/rss/mundo.xml
# https://rss.tecmundo.com.br/feed
# https://olhardigital.com.br/feed/
# https://feeds.folha.uol.com.br/emcimadahora/rss091.xml
# https://globoesporte.globo.com/ESP/Noticia/Rss/0,,AS0-4271,00.xml
# https://g1.globo.com/rss/g1/brasil/
# https://news.un.org/feed/subscribe/pt/news/region/americas/feed/rss.xml


urls = {'www.gazetadopovo.com.br':'/feed/rss/mundo.xml',
        'rss.tecmundo.com.br':'/feed',
        'olhardigital.com.br':'/feed/',
        'feeds.folha.uol.com.br':'/emcimadahora/rss091.xml',
        'globoesporte.globo.com':'/ESP/Noticia/Rss/0,,AS0-4271,00.xml',
        'g1.globo.com':'/rss/g1/brasil/',
        'news.un.org':'/feed/subscribe/pt/news/region/americas/feed/rss.xml'
}


RSS_SERVER   = 'g1.globo.com'
RSS_PATH     = '/rss/g1/brasil/'
RSS_PORT     = 443
CODE_PAGE    = 'utf-8'
MAX_NOTICIAS = 10
BUFFER_SIZE  = 4096

rss_content = ''

for chave, valor in urls.items():
    # Construir requisição HTTP para obter o feed RSS
    request  = f'GET {valor} HTTP/1.1\r\n'
    request += f'Host: {chave}\r\n'
    request += 'User-Agent: Python\r\n'
    request += 'Connection: close\r\n\r\n'

    # Iniciar conexão segura com o servidor
    context         = ssl.create_default_context()
    socket_rss      = socket.create_connection((chave, RSS_PORT))
    socket_rss_wrap = context.wrap_socket(socket_rss, server_hostname=chave)

    # Enviar a requisição
    socket_rss_wrap.send(request.encode(CODE_PAGE))

    # Receber a resposta
    retorno_noticias = ''
    while True:
        resposta = socket_rss_wrap.recv(BUFFER_SIZE).decode('iso-8859-1')
        if not resposta: break
        retorno_noticias += resposta

    # Encontrar o início do conteúdo do feed RSS
    posicao_inicial = retorno_noticias.find('<?xml')
    posicao_final   = retorno_noticias.find('</rss>')

    # Verificando se há conteúdo ma resposta do request
    if (posicao_inicial == -1):
        print('Conteúdo do feed RSS inválido ou vazio.')
        sys.exit()

    # Parsear o conteúdo do feed RSS
    rss_content = retorno_noticias[posicao_inicial:posicao_final+6]

    
    print(f'Conteúdo do feed RSS de {chave}:')
    print('\n')

    try:
        # Montando uma árvore com os elementos do XML de retorno
        root_rss = ET.fromstring(rss_content)
    except ET.ParseError:
        print(f'Erro ao fazer o parse do XML: {sys.exc_info()}')
    except:
        print(f'Erro.....: {sys.exc_info()[0]}')
    else:
        # Extrair as 10 notícias mais recentes
        noticias = root_rss.findall('.//item')[:MAX_NOTICIAS]
        # Imprimir as notícias
        palavra = "extrema"
        for posicao, noticia in enumerate(noticias):
            titulo = noticia.find('title').text
            url    = noticia.find('link').text
            if palavra in titulo.lower():
                print(f'\nNOTÍCIA {posicao+1}')
                print(f'Título.: {titulo}')
                print(f'URL....: {url}\n')