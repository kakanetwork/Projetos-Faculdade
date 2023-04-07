import sys, os, requests
from mylibrary.functions import *
auto_clear(True)


url  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-2021%27&@dataFinalCotacao=%2712-31-2021%27&$format=json'

dados = requests.get(url).json()

#print(dados['value'])

# Questão 01: Solicitar o ano 
# e a média das cotações de compra e
#             e venda do ano informado e as maiores cotações de 
#             compra e venda de cada mês 