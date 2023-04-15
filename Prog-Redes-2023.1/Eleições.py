'''
    O TSE divulga na sua página oficial um webservice que fornece os dados 
    das apurações das eleições realizadas no Brasil.

    O fragmento de código a seguir monta um dicionário (dados_retorno) com o 
    resultado das eleições do ano de 2022 no 1º turno para Presidente.

    Com base na documentação da API contida na URL 
    https://www.tse.jus.br/eleicoes/eleicoes-2022/interessados-na-divulgacao-de-resultados-2022


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
        ...
    }
    
    O dicionário deverá ser ordenado de forma decrescente pela quantidade de
    votos que o candidato obteve.

    Em seguida, deverá ser gerado um arquivo (resultados.txt) onde na 
    primeira linha deverá constar a seguinte string:
        numero;nome,partido;quantidade_votos;percentual_votos

    Da segunda linha em diante deverão constar os dados correspondentes de
    cada candidato
'''
# partido = cc / nome = nm / votos = vap


import requests, os

ano_eleição = 2022
cargo = '0003'
estado = 'rn'
id = 546

url = f'https://resultados.tse.jus.br/oficial/ele{ano_eleição}/{id}/dados-simplificados/{estado}/{estado}-c{cargo}-e000{int(id)}-r.json'

dados_gerais = requests.get(url).json()

filtro = list(map(lambda c: (c['sqcand'], c['nm'], c['cc'], c['vap'], c['pvap']), dados_gerais['cand']))
filtro_organizado = sorted(filtro, key=lambda a: int(a[3]), reverse=True)
numero_cand = dict()
dir = os.path.dirname(os.path.abspath(__file__)) 
file_dir = os.path.join(dir, 'resultados.txt')

with open(file_dir, 'w', encoding='utf-8') as arq:
    arq.write('numero; nome; partido; quantidade_votos; percentual_votos\n')
    for x in filtro_organizado:
        dados_cand = dict()
        dados_cand = {'nome': x[1], 'partido': x[2], 'votos': x[3], 'percentual': x[4]}
        numero_cand[x[0]] = dados_cand
        arq.write(str(f'{int(x[0]), x[1], x[2], int(x[3]), float(x[4].replace("," , "."))}\n'))


   
