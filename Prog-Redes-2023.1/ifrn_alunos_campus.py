import requests, sys, os

# Finalizado: 07/04/2023 
# Atualizado V2: 11/04/2023

# Url do site que iremos realizar o REQUEST
url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

# Realizando o Request
try:
    dados = requests.get(url).json()
except:
    print(f'Não foi possivel acessar o URL, ERRO...... {sys.exc_info()[0]}')

# Pegando diretório atual
dir = os.path.dirname(os.path.abspath(__file__)) 

# Realizando a captura dos Campus do IFRN (sem as duplicatas)
campi = set(map(lambda c: c['campus'], dados))

print('\nEsses são os nossos Campus no IFRN e seus respectivos Alunos:')

for x in campi:
    # Realizando a função (definindo) para captura de todos os Campus (Com duplicatas)
    filtro = lambda m: m['campus'] == x
    # Aqui eu jogo quantos campus existem ao todo, e faço a contagem (qnt_campus_totais == qnt_alunos_totais) 
    # Como estamos dentro do FOR, ele vai fazer a contagem para cada Campus e apenas aqui a função lambda é ativada
    alunos = tuple(filter(filtro, dados))
    qt_alunos = len(alunos)
    print(f'Campus {x}: {qt_alunos} Alunos')

try:
    # Pedindo a sigla ao usuario e utilizando .upper para evitar erros de maiusculo/minusculo
    sigla = str(input('\nINFORME A SIGLA DO CAMPUS: ')).upper()
except: 
    # Tratamento Genérico
    print(f'Erro......: {sys.exc_info()[0]}')
    sys.exit()
else:
    # Tratamento para só aceitar siglas dentro das quais já filtramos em Campi
    if sigla in campi:

        # Parecido com o Filtro1 ele pega todos os cursos (com duplicatas) mas apenas da sigla/campus informado
        filtro2 = lambda m: m['campus'] == sigla
        campus_sigla = list(filter(filtro2, dados))

        # Aqui fazemos a captura dos cursos (sem duplicatas)
        curso = set(map(lambda c: c['curso'], campus_sigla))

        # Definindo nome do arquivo
        file_name = f'{sigla}.txt'
        # Junção do name_arquive + diretorio para 
        file_dir = os.path.join(dir, file_name)

        print(f'\nEsses são os cursos disponibilizados no {sigla}, e sua quantidade de alunos:')

        # abertura do modo Write para escrita do arquivo 
        with open(file_dir, 'w', encoding='utf-8') as file:
            # Parecido com o primeiro for (lá era para os campus) e aqui será para os cursos do campus especifico (segue a mesma lógica)
            for x in curso:
                # filtro somente os cursos de um em um, do campus escolhido
                filtro_cursos = lambda c: c['curso'] == x
                qnt_cursos = list(filter(filtro_cursos, campus_sigla))
                # faço o len para descobrir a quantidade de alunos/por curso 
                qt_alun_cursos = len(qnt_cursos)
                # escrevendo as linhas do código no arquivo
                file.write(str(f'{x}: {qt_alun_cursos} Alunos') + '\n')
                print(f'Curso {x}: {qt_alun_cursos} Alunos')
    else:
        print("\nSigla Inválida!\n")
        sys.exit()
