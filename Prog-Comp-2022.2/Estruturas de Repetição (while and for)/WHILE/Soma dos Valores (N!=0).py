# Comentario: O codigo abaixo solicita que o usuario informe um numero, e enquanto o numero informado nao for zero,
# a variavel 'soma' ira armazenar a soma dos numeros informados. Ao informar um numero zero, o looping e encerrado e o valor final da soma e exibido.


num = 1
soma = 0
while num != 0:
    num = int(input('Informe um número: '))
    soma = num + soma
print(f'A soma dos valores foi igual à: {soma}!')

