# Comentario: O codigo solicita que o usuario informe uma variavel e, em seguida, imprime essa variavel de acordo com o tamanho da string.


var1 = input('Informe uma var1: ')
for x in range(len(var1)+1):
    print(var1[:x])

