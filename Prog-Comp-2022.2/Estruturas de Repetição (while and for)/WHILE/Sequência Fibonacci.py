# Comentario: O codigo abaixo solicita que o usuario insira um valor, e, em seguida, calcula a sequencia de 
# Fibonacci ate o numero inserido. Se o numero digitado for zero, a mensagem "Digite um valor diferente de Zero!" e exibida.


num = int(input('Insira um valor: '))
aux = 1
fibo = 0
aux1 = 0
aux2 = aux
if num != 0:
    while aux <= num:
        fibo = aux2 + aux1
        print(fibo, end=', ')
        aux +=1
        aux2 = aux1
        aux1 = fibo
    print('FIM DA SEQUÊNCIA FIBONACCI!')
else:
    print('Digite um valor diferente de Zero!')

