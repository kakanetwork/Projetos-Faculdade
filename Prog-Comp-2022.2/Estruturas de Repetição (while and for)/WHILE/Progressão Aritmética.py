# Comentario: O codigo abaixo solicita que o usuario informe o valor inicial, a razao e a quantidade de 
# termos da progressao aritmetica, alem da posicao do valor que o usuario deseja encontrar. Em seguida, o codigo imprime a progressao aritmetica, a 
# soma dos termos e o valor solicitado pelo usuario. Por fim, o codigo informa se a progressao aritmetica e crescente, decrescente ou constante.


val = int(input('Informe o Valor inicial da P.A: '))
raz = float(input('Informe a Razão da P.A: '))
qnt = int(input('Quantos termos vc deseja encontrar: '))
posi = int(input(f'Informe a Posição do valor que você quer saber\n(A posição deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
p_a=val
soma=0
cont=1
numposi=0
while cont <= qnt:
     print(p_a, end=' , ')
     soma = p_a + soma
     p_a+=raz
     cont+=1
     if cont == posi and posi <= qnt:
         numposi = p_a
print('FIM DA P.A!')       
print(f'\nA soma da P.A é igual á {soma}!')
print(f'O número correspondente a {posi}° Posição na P.A, é o {numposi}!')
if raz > 0: print('E Sua P.A é crescente!')
elif raz < 0: print('E Sua P.A é Descrescente!')
else: print('E Sua P.A é constante!')

