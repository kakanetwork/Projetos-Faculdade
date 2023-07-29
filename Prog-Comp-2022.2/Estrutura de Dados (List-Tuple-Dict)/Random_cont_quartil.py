# Comentario: O codigo importa a funcao "random" e solicita ao usuario que informe quantos numeros aleatorios ele deseja que sejam gerados, 
# os quais serao armazenados em uma lista. Apos isso, e verificado se o numero informado e maior que zero e, caso seja, os numeros sao gerados e armazenados. 
# Por fim, e calculado quantas vezes cada numero se repetiu na lista.


import random
n = int(input('\nInforme quantos numerais você quer que repita: '))
inicio = 0
fim = 99
lista = list()
if n > 0:
    for i in range(n):
        lista.append(random.randint(inicio,fim))
    print(f'\nOs números foram: {lista}\n')
    print('='*150)
    soma1 = 0
    soma2 = 0
    soma3 = 0
    soma4 = 0
    for i in range(inicio, fim+1):
        cont = lista.count(i)
        if i < 25:
            soma1 += cont
        elif i >= 25 and i <= 49:
            soma2 += cont
        elif i >= 50 and i <= 74:
            soma3 += cont
        elif i >= 75 and i <= 99:
            soma4 += cont
    print(f'\nOs números do 1° QUARTIL Repetiram -> {soma1}x')
    print(f'\nOs números do 2° QUARTIL Repetiram -> {soma2}x')
    print(f'\nOs números do 3° QUARTIL Repetiram -> {soma3}x')
    print(f'\nOs números do 4° QUARTIL Repetiram -> {soma4}x')
    print('\nFIM!\n')
else:
    print('Informe um Número Positivo!')

