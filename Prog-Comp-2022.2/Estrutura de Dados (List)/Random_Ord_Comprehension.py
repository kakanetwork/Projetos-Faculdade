# Comentario: O codigo importa a funcao 'random' e pede ao usuario para informar quantos numeros aleatorios ele quer. A variavel 'n' armazena a quantidade informada pelo usuario.
# Em seguida, as variaveis 'inicio' e 'fim' sao criadas para armazenar os valores minimo e maximo, respectivamente, que os numeros aleatorios podem assumir. 
# A variavel 'lista' e criada para armazenar os numeros aleatorios.
# Caso a quantidade informada pelo usuario seja maior que zero, a variavel 'var1' e criada para armazenar os numeros aleatorios de acordo com as especificacoes. 
# A lista e entao exibida na tela. Em seguida, a lista e ordenada e exibida na tela.
# Caso a quantidade informada pelo usuario seja igual ou menor que zero, uma mensagem de erro e exibida na tela.


import random
n = int(input('\nInforme quantos numerais você quer: '))
inicio = 0
fim = 99
lista = list()
if n > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(n)]
    print(f'A lista original é:\n{lista}')
    print('='*100)

    lista_ord = list()
    tam = len(lista)
    for x in range(tam):
        menor = lista[0]
        for a in range(len(lista)):
            if lista[a] < menor:
                menor = lista[a]
                pos_menor = a
        lista_ord.append(menor)
        lista.remove(menor)
    print(lista_ord)
else:
    print('Informe um Número Positivo!')

