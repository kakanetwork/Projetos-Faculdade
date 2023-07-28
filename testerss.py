import requests
import xml.etree.ElementTree as ET

RSS_PORT = 443
CODE_PAGE = 'utf-8'
MAX_NOTICIAS = 10

def get_rss_content(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar a URL {url}: {e}')
        return None

def rss():
    palavra_chave = "rap"

    with open('rss.conf', 'r') as file:
        urls = file.readlines()

    for url in urls:
        #url = url.strip()

        rss_content = get_rss_content(url)
        if rss_content:
            try:
                root_rss = ET.fromstring(rss_content)
            except ET.ParseError:
                print(f'Erro ao fazer o parse do XML da URL {url}')
            else:
                noticias = root_rss.findall('.//item')[:MAX_NOTICIAS]
                for posicao, noticia in enumerate(noticias):
                    titulo = noticia.find('title').text
                    url = noticia.find('link').text
                    if palavra_chave.lower() in titulo.lower().split():
                        print(f'\nNOTÍCIA {posicao + 1}')
                        print(f'Título: {titulo}')
                        print(f'URL: {url}\n')

rss()
