import requests, os, sys


# Input de algumas informações para requisição

try:
    ano_eleição = int(input('Informe o ano de eleição desejado: '))
except ValueError:
    print('Informe um valor compativel ao ano (ex: 2022)\n')
    sys.exit()
except:
    print(f'Erro......: {sys.exc_info()[0]}\n')
    sys.exit()

# Exibindo opções de cargo para o usuario
print('\nNúmeros dos respectivos cargos:')

print("1 - Presidente\n3 - Governador\n5 - Senador\n6 - Deputado Federal\n7 - Desputado Estadual\n8 - Deputado Distrital\n11 - Prefeito\n13 - Vereador")

try:
    cargo = int(input('Informe o Número do Cargo desejado: '))
except ValueError:
    print('Informe um valor compativel ao cargo (ex: 3)\n')
    sys.exit()
except:
    print(f'Erro......: {sys.exc_info()[0]}\n')
    sys.exit()

try:
    estado = str(input('\nInforme a sigla do estado desejado: ')).lower()
except:
    print(f'Erro......: {sys.exc_info()[0]}\n')
    sys.exit()

# Exibindo opções de ID's para usuario
print("\nNúmeros dos ID's das eleições:")
print("544 - Eleição Federal\n546 - Eleição Estadual\n548 - Eleição de Conselheiro Distrital (Pernambuco)\n426 - Eleições Municipais\n438 - Eleição Suplementar Senador/MT")

try:
    id = int(input('Informe o ID da eleição desejado: '))
except ValueError:
    print('Informe um valor compativel ao ID (ex: 544)\n')
    sys.exit()
except:
    print(f'Erro......: {sys.exc_info()[0]}\n')
    sys.exit()

# Criando URL com base nas informações 
# obs: realizo o zfill(4) no cargo, pois o usuario se informar valor 0003, o int desconsidera os zeros a esquerda, e transforma em 3
# para evitar poderia ter colocado os 000 em string na URL, ou utilizar o ZFILL para completar em até 4 números, com o valor ZERO (foi oque escolhi)
url = f'https://resultados.tse.jus.br/oficial/ele{ano_eleição}/{id}/dados-simplificados/{estado}/{estado}-c{str(cargo).zfill(4)}-e000{id}-r.json'

# realizando a requisção da URL
try:
    dados_gerais = requests.get(url).json()
except requests.exceptions.JSONDecodeError:
    print(f'\nA Requisição não foi concluida por erro em alguma informação [Ano, ID, Cargo] que a URL não processou corretamente..... {sys.exc_info()[0]}\n')
    sys.exit()
except:
    print(f'Erro......: {sys.exc_info()}\n')
    sys.exit()

# Realizando um filtro (map+lambda) para retirar da requisição URL, apenas os dados que quero, dentro de dados_gerais['cand'] que é a chave necessária 
filtro = tuple(map(lambda c: (c['n'], c['nm'], c['cc'], c['vap'], c['pvap']), dados_gerais['cand']))

# organizando meu filtro por ordem decrescente de acordo com a quantidade de votos de cada candidato (usando o lambda para verificar a quantidade de voto na a[3])
# Reverse = True para ativar o modo decrescente 
filtro_organizado = sorted(filtro, key=lambda a: int(a[3]), reverse=True)

# definindo um dict
numero_cand = dict()

# pegando pasta atual + nome do arquivo a ser criado e concatenando eles
dir = os.path.dirname(os.path.abspath(__file__)) 
file_dir = os.path.join(dir, 'resultados.txt')

# realizando abertura/criação do arquivo no modo Write
try:
    with open(file_dir, 'w', encoding='utf-8') as arq:

        # Adicionando o cabeçário do arquivo conforme pedido
        arq.write('numero, nome, partido, quantidade_votos, percentual_votos\n')

        # neste for, realizo várias coisas ao mesmo tempo... mas ele faz o X dentro
        for x in filtro_organizado:

            # aqui criei o dict com os dados de cada candidato por vez, pegando cada item pedido 
            dados_cand = {'nome': x[1], 'partido': x[2], 'votos': x[3], 'percentual': x[4]}
            # com o dict anterior criado, atribui cada dict de cada candidato, ao seu respectivo número como uma KEY, criando uma nova dict com a key = num candidato, e value = o dict anterior
            numero_cand[x[0]] = dados_cand 
            # finalmente termino com a criação do arquivo como pedido com algumas observações
            # utilizo INT no X[0],[3] e float x[4] para deixar mais organizado, e no x[4] também substituo a Virgula pelo Ponto
            # Dúvida: não precisei dos dicts anteriores, para fazer esse arquivo, porque precisaria deles?
            arq.write(f'{int(x[0])}, {x[1]}, {x[2]}, {int(x[3])}, {float(x[4].replace("," , "."))}\n')

except FileNotFoundError as erro:
    print(f"Erro ao escrever no arquivo: {erro}. Verifique se o caminho do arquivo está correto.")
    sys.exit()
except PermissionError as erro:
    print(f"Erro ao escrever no arquivo: {erro}. Verifique se você tem permissão para escrever no arquivo.")
    sys.exit()
except:
    print(f'Erro......: {sys.exc_info()}\n')
    sys.exit()