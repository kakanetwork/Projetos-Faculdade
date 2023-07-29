
"""  LEMBRETE:
     A função lambda está verificando a o mês na data da cotação é igual ao mês que está sendo filtrando (no for) obs:
     A definição da função lambda dentro da variável "filtro" é apenas uma preparação para o que será feito dentro do "filter".
     Quando o "filter" é chamado, ele passa cada item da lista "cota_ano" para a função lambda que está dentro da variável "filtro". 
     A função lambda, por sua vez, verifica se o mês na dataHoraCotacao é igual ao mês que está sendo filtrado (no caso, o mês do loop). 
     Se a condição da lambda for verdadeira, o item é adicionado a uma lista de cotações referentes ao mês atual. 
     A LAMBDA NÃO É EXECUTADA AQUI, SÓ É DEFINIDA OQ VAI FAZER, QUEM EXECUTA É O FILTER
     A função zfill serve para acrescentar os zeros a esquerda do número, para que 1 fique como 01 """


import requests, sys, statistics

meses = ['JAN','FEV','MAR','ABR','MAI','JUN',
         'JUL','AGO','SET','OUT','NOV','DEZ']

# ----------------------------------------
# 1) Solicitar o ano e obter cotacoes do
#    ano solicitado

while True:
    try:
        ano = int(input('Informe o ano: '))
    except ValueError:
        print('ERRO: Informado valor String...\n')
    except:
        print(f'ERRO...... {sys.exc_info()[0]}\n')
    else:
        if ano <= 0:
            print('ERRO: Informado Ano Inválido...\n')
        else:
            break

url  = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2712-31-{ano}%27&$format=json'

dados = requests.get(url).json()

cotacoes_ano = dados['value']


# ----------------------------------------
for mes in range(1, 13):
    # 2) Calcular a média das cotações de compra e venda do ano informado
    filtro = lambda m: m['dataHoraCotacao'][5:7] == str(mes).zfill(2)    
    cotacoes_mes = list(filter(filtro, cotacoes_ano))
    try:
        cotacoes_compra = list(map(lambda c: c['cotacaoCompra'], cotacoes_mes))
        media_compra    = statistics.mean(cotacoes_compra)
        maior_compra    = max(cotacoes_compra)
        cotacoes_venda  = list(map(lambda c: c['cotacaoVenda'], cotacoes_mes))
        media_venda     = statistics.mean(cotacoes_venda)
        maior_venda     = max(cotacoes_venda)
    except:
        media_compra = media_venda = maior_compra = maior_venda = 0
    finally:
        print(f'Mês {meses[mes-1]}: ... ', end = ' ')
        print(f'Média Compra: {media_compra:.3f} / Média Venda: {media_venda:.3f}', end = ' ')
        print(f'/ Maior Compra: {maior_compra:.3f} / Maior Venda: {maior_venda:.3f}')

    # 3) Informar maiores cotações de compra e venda de cada mês 
