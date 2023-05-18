import requests
import re
import time

def procurar_produto_aliexpress():
    url = 'https://www.aliexpress.com/wholesale?'
    params = {
        'SearchText': '',
        'minPrice': '0',
        'maxPrice': '10',
        'isFreeShip': 'true',
        'SortType': 'default',
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            pattern = r'"productDetailUrl":"(.*?)"'
            matches = re.findall(pattern, response.text)
            for match in matches:
                link_produto = match.replace("\\", "")
                print(link_produto)
        except ValueError:
            print('Erro ao interpretar a resposta JSON')
    else:
        print('Erro ao realizar a busca')

while True:
    procurar_produto_aliexpress()
    time.sleep(5)
