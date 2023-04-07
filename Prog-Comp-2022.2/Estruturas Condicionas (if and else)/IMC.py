# Comentario: O codigo abaixo calcula o IMC (Indice de Massa Corporal) de uma pessoa. 
# Para isso, ele primeiro pede que o usuario informe o seu peso e a sua altura. 
# Em seguida, usa a formula do IMC para calcular o valor. 
# Por fim, ele usa condicoes para verificar o "grau" do IMC, 
# ou seja, se a pessoa esta no peso normal, abaixo do peso, com sobrepeso, obesidade I, II ou III.


# Entrada de Dados
peso = float(input('\nInforme seu peso: '))
altura = float(input('Informe sua altura: '))

# Fórmula do IMC 
imc = peso/(altura**2)

# Condições para os Graus de IMC
if imc >= 40:
    print(f'\nSeu IMC é: {imc:.1f}, Obesidade III ou Mórbida!')
elif imc >= 35 and imc < 40:
    print(f'\nSeu IMC é: {imc:.1f}, Obesidade grau II!')
elif imc >= 30 and imc < 35:
    print(f'\nSeu IMC é: {imc:.1f}, Obesidade grau I!')
elif imc >= 25 and imc < 30:
    print(f'\nSeu IMC é: {imc:.1f}, Sobrepeso!')
elif imc > 18.5 and imc < 25:
    print(f'\nSeu IMC é: {imc:.1f}, Peso normal!')
else:
    print(f'\nSeu IMC é: {imc:.1f}, Abaixo do peso!')

