# Comentario: O codigo abaixo importa a funcao "random" e pede para o usuario informar quantos numeros ele quer. Em seguida, a funcao 
# "lista" e criada e os numeros sao inseridos nela. A lista original e impressa e, em seguida, a lista e ordenada de forma decrescente.


import random
n = int(input('\nInforme quantos números você quer: '))
inicio = 0
fim = 99
lista = list()
if n > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(n) ]
    print(f'A lista original é:\n{lista}')
    print('-'*150)
    lista.sort(reverse=True)
    print(f'A lista alterada é:\n{lista}')
else:
    print('Informe um Número Positivo!')

