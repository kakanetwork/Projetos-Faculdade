# Comentario: O codigo abaixo esta definindo as vogais acentuadas e solicitando que o usuario informe uma palavra. 
# Apos isso, ele transforma todas as letras da palavra em letras minusculas. Em seguida, ele verifica quantas vogais existem na palavra informada pelo usuario.


# Definindo as vogais acentuadas
vogais = 'aáâeéêiíoóôuú'
var = str(input('Informe a Palavra na qual deseja encontrar as vogais: '))
var1 = var.lower()
qnt = 0
cont = 1
cont1 = 0
cont2 = 1 
while cont <= len(var):
        caracter = var1[cont1:cont2]
        find = vogais.find(caracter)
        cont += 1
        cont1 += 1
        cont2 += 1
        if find != -1:
            qnt+=1
print(f'A Palavra {var} possui um total de -> {qnt} vogais!')


