

frase = str(input('Insira uma frase: '))
palavra_nova = str(input('Insira uma palavra para substituir na frase: '))
palavra_antiga = str(input(f'Insira a palavra que deseja retirar da frase -> {frase}\ne substituir pela -> {palavra_nova}: '))
print(f'A frase era: {frase}')
print(f'A palavra antiga da frase era: {palavra_antiga}')
print(f'A palavra nova da frase é: {palavra_nova}')
frase = frase.replace(palavra_antiga, palavra_nova)
print(f'A frase nova é: {frase}\n')

