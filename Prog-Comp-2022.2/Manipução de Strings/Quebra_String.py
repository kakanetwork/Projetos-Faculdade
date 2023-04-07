# Comentario: O codigo abaixo solicita que o usuario insira uma palavra, e imprime a palavra letra por letra.


var = str(input('Insira uma palavra: '))
cont = 1
while cont <= len(var):
    print(var[:cont])
    cont+=1

