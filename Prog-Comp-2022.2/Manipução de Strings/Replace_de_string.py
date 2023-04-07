# Comentario:
# O codigo abaixo solicita que o usuario digite uma frase, e imprime a frase digitada e a frase com os espacos substituidos por tracos.


var = str(input('Digite uma frase: '))
print(f'\nA frase foi: {var}')
var = var.replace(' ', '_')
print(f'A frase corrigida é: {var}\n')

