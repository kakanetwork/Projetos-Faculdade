# Comentario: O codigo abaixo pede para o usuario inserir uma palavra e, em seguida, 
# imprime essa palavra de forma que a cada iteracao do loop a palavra seja imprimida uma vez a mais.


var = str(input('Insira uma palavra: '))
qnt = len(var)
cont = 1
cont1 = 1
cont2 = qnt-1
while cont1 <= (qnt * 2):
    if cont <= qnt:
        print(var[:cont])
        cont+=1
    elif cont > qnt:
        print(var[:cont2])
        cont2-=1
    cont1+=1

