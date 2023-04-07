# passo 1: a do ano ao usuário
ano = input('Digite o ano com 4 dígitos para abrir o arquivo do Cartola FC correspondente: ')

#dasdad
# passo 2: abertura do arquivo e armazenamento do conteúdo em um dicionário
with open(f'cartola_fc_{ano}.txt', 'r') as arquivo:
    cartola = eval(arquivo.read().replace('null', 'None'))

# passo 3: solicitação do esquema tático ao usuário
esquema = input('Digite o esquema tático desejado (3-4-3, 3-5-2, 4-3-3, 4-4-2, 4-5-1, 5-3-2 ou 5-4-1): ')

# passo 4: filtragem dos jogadores de acordo com o esquema tático escolhido
jogadores = {}
for posicao, qtd in zip(['goleiro', 'zagueiro', 'lateral', 'meia', 'atacante', 'tecnico'], [1, 3, 2, int(esquema.split('-')[1]), int(esquema.split('-')[2]), 1]):
    jogadores_posicao = {}
    for jogador, stats in cartola.items():
        if stats['posicao'] == posicao and stats['jogos_num'] > 0:
            media_pontos = stats['pontos_num'] / stats['jogos_num']
            jogadores_posicao[jogador] = media_pontos
    jogadores[posicao] = dict(sorted(jogadores_posicao.items(), key=lambda item: item[1], reverse=True)[:qtd])

# passo 6: exibição dos jogadores na tela, seguindo a ordem de prioridade de escolha de acordo com o esquema tático escolhido
print('Time escolhido:')
for posicao in ['goleiro', 'zagueiro', 'lateral', 'meia', 'atacante', 'tecnico']:
    for jogador, stats in jogadores[posicao].items():
        print(f'{posicao}: {jogador} ({cartola[jogador]["clube_id"]}), média de {stats:.2f} pontos por partida')
