# Comentario: O codigo abaixo solicita que o usuario informe um numero decimal para conversao. 
# Em seguida, o codigo calcula o resto da divisao do numero decimal informado pelo usuario por 2 e guarda o valor na variavel "resto". 
# O codigo divide o numero decimal informado pelo usuario por 2 e guarda o valor na variavel "dec". O codigo concatena o valor da variavel "resto" com a variavel "binario". 
# Por fim, o codigo exibe o valor da variavel "binario", que contem o numero binario correspondente ao numero decimal informado pelo usuario.


dec = int(input('Informe o Número em Decimal para a Conversão: '))
dec = abs(dec)
binario = ''
for x in range(dec+1):
    if dec > 0:
        resto = dec%2 
        dec = dec//2
        binario = str(resto)+binario 
print(f'\nSeu Número em Binário é correspondente a: {binario}')

