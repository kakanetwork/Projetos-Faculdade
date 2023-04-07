# Comentario: O codigo abaixo aparenta ser um programa que determina se um numero informado pelo usuario e 
# par ou impar. O programa pede para o usuario informar um numero, e este numero deve ser maior ou igual a zero. Se o numero informado for par, 
# o programa exibe a mensagem "Seu Numero e Par!". Se o numero informado for impar, o programa exibe a mensagem "Seu Numero e Impar!". Se o usuario informar o numero zero, 
# o programa exibe a mensagem "Voce Encerrou o Programa!" e encerra a execucao.


rep = 1
while rep != 0:
    rep = int(input('informe o Número: '))
    rep = abs(rep)
    if rep != 0:
        if rep%2 == 0: print('Seu Número é Par!\n')
        else: print('Seu Número é Impar!\n')
    else: print('Você Encerrou o Programa!')

