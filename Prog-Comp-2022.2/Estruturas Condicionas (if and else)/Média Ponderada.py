# Comentario: O codigo abaixoop solicita ao usuario que informe duas notas e seus respectivos pesos. 
# Em seguida, e calculada a media ponderada dessas notas. Por fim, e verificado se a media e maior ou igual a 60, o que indica aprovacao, ou se a media e menor que 20, 
# o que indica reprovacao, ou se a media esta entre esses valores, o que indica que o aluno pode fazer a prova final.


# Entrada de Dados
nota1 = int(input("\nInforme a Primeira nota: "))
nota2 = int(input("Informe a Segunda nota: "))
peso1 = float(input("\nInforme o Primeiro Peso: "))
peso2 = float(input("Informe o Segundo Peso: "))

# Condição onde as notas devem ser Números entre 0 e 100 e os Pesos devem ser Maiores ou igual a Zero
if nota1 >0 and nota1 <= 100 and nota2 >0 and nota2 <= 100 and peso1 >= 0 and peso2 >= 0:

    # Cálculo da Média Ponderada, onde multiplica as notas pelo peso e divide pela soma dos pesos
    media = (nota1*peso1 + nota2*peso2)/(peso1+peso2)
    if media >= 60:
        print(f'\nsua média foi {media}, Parabéns está Aprovado!\n')
    elif media < 20:
        print(f'\nsua média foi {media}, está Reprovado!\n')
    else:
        print(f'\nsua média foi {media}, pode fazer a Prova Final!\n')
else:
    print('\nNota não permitida!\n')

