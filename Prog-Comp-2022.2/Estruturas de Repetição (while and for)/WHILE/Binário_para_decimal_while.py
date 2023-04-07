# Comentario: O codigo abaixo converte um numero binario 
#informado pelo usuario em um numero decimal. A variavel bin recebe o valor informado pelo usuario, a variavel 
#var1 inicia com o valor de bin em ordem inversa e a variavel dec inicia com o valor 0. Enquanto o contador for menor que o 
#tamanho da variavel var1, o programa verifica se o valor na posicao do contador e igual a 1. Se for, o valor da variavel dec e somado com a 
#potencia de 2 elevado ao valor do contador. Por fim, e exibido o valor decimal de bin.


bin = input('informe um número binário: ')
var1 = bin[::-1]
dec = 0
cont = 0 
while cont < len(var1):
    if var1[cont] == '1':
        dec += 2 ** cont
    cont+=1
print(f'O valor decimal de {bin} é = {dec}')

