import sys, requests
from mylibrary.functions import *

auto_clear(True)

try:
    ano = int(input('\nInforme o Ano para consulta do Dólar: '))
except TypeError:
    print(f'\nInforme um Ano Válido!\n')
except:
    print(f'Erro......: {sys.exc_info()[0]}')
else:
    if ano <= 0:
        print('Informe um ano Positivo ou Maior que Zero!')
        sys.exit()

url = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2712-31-{ano}%27&$format=json'

dados = requests.get(url).json()
cota_ano = dados['value']
for mes in range(1,13):
    filtro = list()

    # A função lambda está verificando a o mês na data da cotação é igual ao mês que está sendo filtrando (no for) obs:
    # A definição da função lambda dentro da variável "filtro" é apenas uma preparação para o que será feito dentro do "filter".
    # Quando o "filter" é chamado, ele passa cada item da lista "cota_ano" para a função lambda que está dentro da variável "filtro". 
    # A função lambda, por sua vez, verifica se o mês na dataHoraCotacao é igual ao mês que está sendo filtrado (no caso, o mês do loop). 
    # Se a condição da lambda for verdadeira, o item é adicionado a uma lista de cotações referentes ao mês atual. 
    # A LAMBDA NÃO É EXECUTADA AQUI, SÓ É DEFINIDA OQ VAI FAZER, QUEM EXECUTA É O FILTER
    # A função zfill serve para acrescentar os zeros a esquerda do número, para que 1 fique como 01 
    filtro = lambda m: m['dataHoraCotacao'][5:7] == str(mes).zfill(2)
    cotacoes_mes = list(filter(filtro, cota_ano))

    print(cotacoes_mes)

#print(dados['value'])

# Questão 01: Solicitar o ano 
# e a média das cotações de compra e
#             e venda do ano informado e as maiores cotações de 
#             compra e venda de cada mês