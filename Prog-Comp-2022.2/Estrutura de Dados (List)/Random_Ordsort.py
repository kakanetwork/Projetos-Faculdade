# Comentario: O codigo importa a biblioteca "random" e pede para o usuario informar quantos numeros ele quer. Em seguida, 
# a variavel "inicio" e definida como 0 e a variavel "fim" e definida como 99. A variavel "lista" e definida como uma lista vazia.
# Se o valor da variavel "n" for maior que 0, a lista sera preenchida com numeros aleatorios entre "inicio" e "fim". Se o valor da variavel 
# "n" for menor ou igual a 0, o programa exibira a mensagem "Informe um numero Positivo!".


import random
n = int(input('\nInforme quantos números você quer: '))
inicio = 0
fim = 99
lista = list()
if n > 0:
    for num in range(n):
        lista.append(random.randint(inicio,fim))
    print(f'A lista original é:\n{lista}')
    print('-'*150)
    lista.sort(reverse=True)
    print(f'A lista alterada é:\n{lista}')
else:
    print('Informe um número Positivo!')

