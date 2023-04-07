import requests

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

dados = requests.get(url).json()

# o lambda vai percorrer cada item dentro da lista (cada item é um aluno e seus dados) que estão dentro de um dict (lista de dict's), então eu acesso primeiro os dicts
# com o Lambda, pois ele vai de item em item dentro da lista!, após acessar os dicts eu deixo claro no lambda que quero dentro do dict a key 'campus'
# e quem pega para mim os valores dentro dessa key, é o Map que joga para uma lista, entaõ o lambda é a função e o map é quem confirma essa função e joga na lista!
# o set serve para remover as duplicatas
campi = set(map(lambda c: c['campus'], dados))

for campus in campi:
    # usamos o lambda para entrar dentro da lista de dict's, e pegar todas as x vezes que y campus se repete (sabemos que y é campi, na variavel que resolvemos anteriormente)
    # então ele vai pegar cada CAMPUS da lista e comparar a cada CAMPI do set que fizemos, se for igual, ele ativa o Filtro e joga dentro da lista
    # após ele varrer tudo, vai pro próximo campi e vai printando assim em diante........
    filtro = lambda m: m['campus'] == campus
    alunos = tuple(filter(filtro, dados))
    qt_alunos = len(alunos)
    print(f'Campus {campus}: {qt_alunos} Alunos')

while True:
    try:
        sigla = str(input('\nINFORME A SIGLA DO CAMPUS: ')).upper()
    except: 
        print(f'Erro......: {sys.exc_info()[0]}')
    else:
        if sigla in campi:
            break

filtro2 = lambda m: m['campus'] == sigla
campus_sigla = list(filter(filtro2, dados))
curso = set(map(lambda c: c['curso'], campus_sigla))


print(f'\nEsses são os cursos disponibilazdos no {sigla}, e sua quantidade de alunos:')


for x in curso:
    filtro_cursos = lambda c: c['curso'] == x
    qnt_cursos = list(filter(filtro_cursos, campus_sigla))
    qt_alun_cursos = len(qnt_cursos)
    print(f'Curso {x}: {qt_alun_cursos} Alunos')

