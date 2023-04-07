

import sys, platform, os, statistics, time
from myfunctions_ANP import *
# Pegando seu diretório atual e vendo contagem de sedgundos
start = time.time()
diretorio_atual = os.path.dirname(os.path.abspath(__file__)) 

# Verificando sistema para dar clear
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

# definindo diretorio da pasta 'dados_estatisticos' para criação
dir_dados = diretorio_atual + '\\dados_estatisticos'

# criando o diretorio pedido no item A
try:
    os.mkdir(dir_dados)
except FileExistsError:
    print(f'A Pasta (dados_estatisticos) já foi criada!\n')
except:
    print(f'Erro na criação da pasta......: {sys.exc_info()[0]}\n')
    sys.exit()

# Pegando diretorio da pasta onde contem os arquivos da ANP
dir_anp = diretorio_atual + '\\serie_historica_anp'

# Varrendo o diretório dos arquivos da ANP para pegar o nome de cada um
try: 
    lista_arq = tuple(os.listdir(dir_anp))
except:
    print(f'Erro na localização do diretório (serie_historica_anp)......: {sys.exc_info()[0]}\n')
    sys.exit()

# Utilizando minha função (para facilitar correção de erros) para leitura dos arquivos e realizando o pedido do ITEM B
dados_lidos = leitura_arq(lista_arq, dir_anp)

# Realizando o pedido do ITEM C, da criação do arquivo
try:
    arq_save1 = open(dir_dados+'\\serie_historica_anp.txt', 'w', encoding='utf-8')
except: 
    print(f'Erro na escrita......: {sys.exc_info()[0]}')
else:
    for dados in dados_lidos:
        # Adicionando os dados nas suas devidas posições
        arq_save1.write(f'{dados[0]};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{dados[5]}\n')
    arq_save1.close()


# Defini uma função para realizar a média de acordo com os parametros informados
def media_ano_produto_bandeira(parametros):
    # informe os 3 parametros pedidos
    bandeira, produto, ano = parametros
    # indexo as posições de todas os parametros da minha lista original, e os insiro em uma nova tupla
    all_dados = tuple([dados[4] for dados in dados_lidos if dados[5] == bandeira and dados[2] == produto and dados[3][6:10] == ano])
    # contagem de bandeiras/postos
    cont_bandeiras = len(all_dados)
    # realizando a média (LEMBRAR: FUNÇÃO ROUND PARA ARREDONDAMENTO)
    # (LEMBRAR: Esse metodo de utilização do if/else na mesma linha, Pesquisa: Operadores Ternários)
    média = round(statistics.mean(all_dados), 3) if cont_bandeiras > 0 else 0
    return (bandeira, produto, ano, média, cont_bandeiras)

# Faço o set para que os valores não se repitam quando for inserir no novo arquivo
save_dados_1 = set((dados[5], dados[2], dados[3][6:10]) for dados in dados_lidos)
save_dados_2 = map(media_ano_produto_bandeira, save_dados_1)

# Criando o Primeiro arquivo do ITEM D (Média Produto, Ano, Bandeira)
try:
    arquivo2_save = open(dir_dados+'\\media_bandeira.txt', 'w', encoding='utf-8')
except:
    print(f'Erro na escrita......: {sys.exc_info()[0]}\n')
else:
    for dados in save_dados_2:
        # Escrevendo o conteudo no novo arquivo
        arquivo2_save.write('{}\n'.format(';'.join(map(str, dados))))
    arquivo2_save.close()

def media_ano_produto_bandeira_regiao(parametros):
    regiao, produto, ano = parametros
    all_dados2 = tuple([dados[4] for dados in dados_lidos if dados[0] == regiao and dados[2] == produto and dados[3][6:10] == ano])
    cont_bandeiras2 = len(all_dados2)
    média2 = round(statistics.mean(all_dados2), 3) if cont_bandeiras2 > 0 else 0
    return (regiao, produto, ano, média2, cont_bandeiras2)
save_dados_3 = set((dados[0], dados[2], dados[3][6:10]) for dados in dados_lidos)
try:
    arquivo3_save = open(dir_dados+'\\media_regiao_bandeira.txt', 'w', encoding='utf-8')
except:
    print(f'Erro na escrita......: {sys.exc_info()[0]}\n')
else:
    for dados in map(media_ano_produto_bandeira_regiao, save_dados_3):
        arquivo3_save.write('{}\n'.format(';'.join(map(str, dados))))
    arquivo3_save.close()
end = time.time()
print(f'O tempo total de execução em Minutos foi de -> {((end-start)/60):.2f}')