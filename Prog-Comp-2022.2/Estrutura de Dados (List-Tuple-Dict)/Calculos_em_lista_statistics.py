# Comentario: O codigo importa a biblioteca statistics e a biblioteca random. Depois solicita ao usuario que informe 
# quantos numeros aleatorios ele deseja. Em seguida, define os intervalos inicial e final para a geracao dos numeros aleatorios. 
# Cria uma lista vazia e, se o numero informado for maior que zero, insere numeros aleatorios na lista e os ordena. Por fim, calcula e 
# exibe a media, mediana, variancia e desvio padrao dos numeros da lista.


import statistics
import random
n = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 99
lista = list()
if n > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(n)]
    lista.sort()
    print(f'\nOs números foram: {lista}\n')
    print(f'A média é -> {statistics.mean(lista):.2f}')
    print(f'A médiana é -> {statistics.median(lista):.2f}')
    print(f'A variação é -> {statistics.variance(lista):.2f}')
    print(f'O Desvio é -> {statistics.stdev(lista):.2f}')
else:
    print('Informe um Número Positivo!')

