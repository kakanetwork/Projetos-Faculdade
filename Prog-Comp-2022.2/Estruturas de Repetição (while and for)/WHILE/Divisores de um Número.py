# Comentario:  O codigo abaixo e um programa que encontra todos os divisores de um numero informado pelo usuario e informa se o numero e primo.

valor = int(input('Informe um valor positivo: '))
valor = abs(valor)

if valor != 0: # Condição N°1 - Para que o Número informado seja diferente de ZERO
    divisor = 1
    contdiv = 0

    while divisor <= valor: # Estrutura de Repetição - Para que faça todas as divisões inteiras até o valor

        if valor % divisor == 0: # Condição N°2 - Onde Informa os divisores quando tiver resto igual a Zero
            print(f'Os divisores são {divisor}')
            contdiv += 1
        divisor += 1

    if contdiv == 2: print('E o Número é primo!') # Condição N°3 - Onde informa se ele é Primo ou Não
    else: print('E o Número não é Primo!')
    
else: print('Informe um Valor diferente de Zero!')



