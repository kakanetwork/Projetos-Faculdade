# Coment�rio: var1 = int(input('Informe o valor inicial da P.G: '))
raz = float(input('Informe a Razao da P.G: '))
qnt = int(input('Quantos termos vc deseja encontrar: '))
posi = int(input(f'Informe a Posicao do valor que voce quer saber\n(A posicao deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
prog = var1
cont = 1
posi = 0
soma = 0
for x in range(cont,qnt+1):
    print(f'{prog:.2f}', end = ' , ')
    soma = prog + soma
    prog *= raz
    cont += 1
    if cont == posi and posi <= qnt:
        posi = prog
print('P.G encerrada!')       
print(f'\nA soma da P.G e igual a {soma}!')
print(f'O numero correspondente a {posi}deg posicao na P.G, e o = {posi}!')
if raz > 1:
    print('E Sua P.G e crescente!')
elif 0 < raz < 1:
    print('P.G descrescente!')
elif raz == 1: 
    print('P.G constante!')
elif raz < 0: 
    print('P.G oscilante!')
else: 
    print('Insira um var1 diferente de 0!')


var1 = int(input('Informe o valor inicial da P.G: '))
raz = float(input('Informe a Razão da P.G: '))
qnt = int(input('Quantos termos vc deseja encontrar: '))
posi = int(input(f'Informe a Posição do valor que você quer saber\n(A posição deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
prog = var1
cont = 1
posi = 0
soma = 0
for x in range(cont,qnt+1):
    print(f'{prog:.2f}', end = ' , ')
    soma = prog + soma
    prog *= raz
    cont += 1
    if cont == posi and posi <= qnt:
        posi = prog
print('P.G encerrada!')       
print(f'\nA soma da P.G é igual á {soma}!')
print(f'O número correspondente a {posi}° posição na P.G, é o = {posi}!')
if raz > 1:
    print('E Sua P.G é crescente!')
elif 0 < raz < 1:
    print('P.G descrescente!')
elif raz == 1: 
    print('P.G constante!')
elif raz < 0: 
    print('P.G oscilante!')
else: 
    print('Insira um var1 diferente de 0!')

