# Comentario: O codigo importa a funcao randint do modulo random. Em seguida, o usuario informa quantos numeros aleatorios ele deseja ver. 
#A variavel n armazena esse valor. Depois e criada uma lista vazia chamada lista. Se o valor de n for maior que zero, o laco for e executado n vezes, 
# adicionando a lista numeros aleatorios gerados pela funcao randint. Por fim, e exibido na tela a lista de numeros gerados e a quantidade de repeticoes de cada um deles.


import random
n = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 9
lista = list()
if n > 0:
    for i in range(n):
        lista.append(random.randint(inicio,fim))
    print(f'\nOs números foram: {lista}')
    print('\nA quantidade de repitação de cada número foi: ')
    for i in range(inicio, fim+1):
        print(f'{i} -> {lista.count(i)}')
    print('\nFIM!')
else:
    print('Informe um Número Positivo!')


