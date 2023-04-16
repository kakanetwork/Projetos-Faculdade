'''
    O TSE divulga na sua página oficial um webservice que fornece os dados 
    das apurações das eleições realizadas no Brasil.

    O fragmento de código a seguir monta um dicionário (dados_retorno) com o 
    resultado das eleições do ano de 2022 no 1º turno para Presidente.

    Com base na documentação da API contida na URL 
    https://www.tse.jus.br/eleicoes/eleicoes-2022/interessados-na-divulgacao-de-resultados-2022

    0001 Presidente Majoritário
    0003 Governador Majoritário
    0005 Senador Majoritário
    0011 Prefeito Majoritário
    0006 Deputado Federal Proporcional
    0007 Deputado Estadual Proporcional
    0008 Deputado Distrital Proporcional
    0013 Vereador Proporcional
    # Solicitar o ano,  solicitar a sigla do estado (ou br), cargo eletivo, id da eleição (ex: 544, 546)


    Pede-se que seja desenvolvido um programa que solicite ao usuário o 
    ano da eleição, tipo de eleição (estadual, nacional) e o cargo eletivo 
    e o programa  deverá montar um dicionário {k:v} no seguinte formato:
    {
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        ...'''

import requests, os



'''ano_eleição = int(input('Informe o ano de eleição desejado: '))

print('\nNúmeros dos respectivos cargos:')
print("1 - Presidente\n3 - Governador\n5 - Senador\n6 - Deputado Federal\n7 - Desputado Estadual\n8 - Deputado Distrital\n11 - Prefeito\n13 - Vereador")
cargo = int(input('Informe o Número do Cargo desejado: '))

estado = str(input('\nInforme o estado desejado: ')).lower()

print("\nNúmeros dos ID's das eleições:")
print("544 - Eleição Federal\n546 - Eleição Estadual\n548 - Eleição de Conselheiro Distrital (Pernambuco)\n426 - Eleições Municipais\n438 - Eleição Suplementar Senador/MT")
id = int(input('Informe o ID da eleição desejado: '))
'''
id = 544
ano_eleição = 2022
estado = 'br'
cargo = 1

url = f'https://resultados.tse.jus.br/oficial/ele{ano_eleição}/{id}/dados-simplificados/{estado}/{estado}-c{str(cargo).zfill(4)}-e000{id}-r.json'
dados_gerais = requests.get(url).json()


filtro = tuple(map(lambda c: (c['n'], c['nm'], c['cc'], c['vap'], c['pvap']), dados_gerais['cand']))
filtro_organizado = sorted(filtro, key=lambda a: int(a[3]), reverse=True)
numero_cand = dict()
dir = os.path.dirname(os.path.abspath(__file__)) 
file_dir = os.path.join(dir, 'resultados.txt')
with open(file_dir, 'w', encoding='utf-8') as arq:
    arq.write('numero, nome, partido, quantidade_votos, percentual_votos\n')
    for x in filtro_organizado:
        dados_cand = {'nome': x[1], 'partido': x[2], 'votos': x[3], 'percentual': x[4]}
        numero_cand[x[0]] = dados_cand 
        arq.write(f'{int(x[0])}, {x[1]}, {x[2]}, {int(x[3])}, {float(x[4].replace("," , "."))}\n')

print(numero_cand)