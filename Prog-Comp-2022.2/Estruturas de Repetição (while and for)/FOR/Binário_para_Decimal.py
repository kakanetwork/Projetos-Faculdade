# Comentario: O codigo abaixo pede para o usuario informar um numero binario, e ao receber o numero binario, o codigo faz a conversao do numero para decimal.


bin = input('informe um número binário: ')
var1 = bin[::-1]
dec = 0
for cont in range(len(var1)):
    if var1[cont] == '1':
        dec += 2 ** cont
print(f'O valor decimal de {bin} é = {dec}')

