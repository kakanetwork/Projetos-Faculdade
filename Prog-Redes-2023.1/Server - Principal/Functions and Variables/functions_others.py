
def PRINT_DIV(dados):
    print('\n'+'-'*100)
    print(dados)
    print('-'*100)

def OPTIONS():
    opções_descritivas = {
        '/q': 'Realizar Push no GitHub',
        '/l': 'Realizar Pull do GitHub'
        }

    print('\nFerramentas Disponiveis:\n')

    for key, value in opções_descritivas.items():
        print(f'{key}: {value}')

    ferramenta = ''

    while ferramenta not in opções:
        ferramenta = input('\nQual Ferramenta deseja utilizar? ')
        if ferramenta not in opções:
            print('Tente Novamente... informe corretamente!')

    print(f'Você escolhou a ferramenta: {opções_descritivas[ferramenta]}\n')
    opções[ferramenta]()

