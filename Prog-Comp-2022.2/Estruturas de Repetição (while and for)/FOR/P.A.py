# Comentario: O codigo abaixo solicita que o usuario informe um valor para iniciar uma Progressao Aritmetica (P.A), 
#a razao dessa progressao e a quantidade de termos que ela devera possuir. Apos isso, o codigo imprime a P.A. solicitada e, em seguida, 
# informa qual o valor que o usuario solicitou verificar e a posicao dele na progressao. Por fim, o codigo ainda informa se a progressao e crescente, decrescente ou constante.


val = int(input('Informe um valor parar iniciar a P.A: '))
raz = float(input('Agora informe a razão da P.A: '))
qnt = int(input('Quantos termos quer encontrar na P.A? '))
posi = int(input(f'Agora informe a posição do valor que deseja verificar\n(Lembrando que o valor deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
pa=val
soma=0
cont=1
posi=0
for x in range(cont,qnt+1):
     print(pa, end=' , ')
     soma = pa + soma
     pa+=raz
     cont+=1
     if cont == posi and posi <= qnt:
         posi = pa
print('P.A encerrada!')       
print(f'A soma da P.A é igual á {soma}!')
print(f'O número correspondente a {posi}° posição na P.A é = {posi}!')
if raz > 0: 
    print('P.A crescente!')
elif raz < 0: 
    print('P.A descrescente!')
else: 
    print('P.A constante!')

