# Comentario: O codigo importa a biblioteca random, pede para o usuario informar quantos numeros ele quer e cria uma lista vazia. 
#Em seguida, cria uma lista com numeros aleatorios de acordo com o numero informado pelo usuario. Por fim, pede para o usuario informar
#um valor e verifica se esse valor se encontra na lista criada anteriormente.


import random
n = int(input('\nInforme quantos numerais você quer: '))
inicio = 0
fim = 1000
lista = list()
if n > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(n)]
    print(lista)
    valor = int(input('Insira o valor que deseja pesquisar na lista entre 0-1000:'))
    if valor not in lista: 
        print(f'\no {valor} não se encontra na lista!')
    else:
        print(f'\no {valor} se encontra na lista na posição {lista.index(valor)}')
else: 
    print('Informe um Número Positivo!')
    

