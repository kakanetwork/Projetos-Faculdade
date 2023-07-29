# Comentario: O codigo solicita ao usuario que informe quantos numeros ele deseja inserir em uma lista, em seguida, o 
# usuario deve inserir os numeros. A lista e classificada e, caso o numero de elementos da lista seja maior que o numero 
# solicitado pelo usuario, o ultimo elemento da lista e removido.


n = int(input('Informe quantos numerais você quer: '))
lista = list()
num = int(input('Informe um número: '))
lista.append(num)
print(lista)
if n > 0:
    while True:
        num = int(input('Informe outro número: '))
        if num == 0: break
        lista.append(num)
        lista.sort()
        if len(lista) > n:
            lista.remove(lista[n])
        print(lista)
else:
    print('Informe um Número Positivo!')

