#!/bin/bash

#==================================================================================================
echo '\n====================\n'

# DECLARAÇÃO DE VARIAVÉIS:

varstr01=texto
varint01=100
varfloat01=10.0
num1=10
num2=10

# $ -> buscar variavel  (utilizar em conjunto com aspas duplas)
echo "String: $varstr01\nInteiro: $varint01\nFloat: $varfloat01"

# Utilização das aspas simples retorna na tela apenas a string sem expressão/variavel 
echo 'String: $varstr01' 

#==================================================================================================
echo '\n====================\n'

# SOMA/SUBTRAÇÃO/MULTIPLICAÇÃO/DIVISÃO - ENTRE INTEIROS
# utilizar parentêses duplos com $ ao inicio (posso realizar no echo ou jogar na variavel)

echo 'Soma:' $((num1 + num2))
result01=$((num1 - num2))
result02=$((num1 * num2))
result03=$((num1 / num2))
echo "A subtração é igual: $result01\nA multiplicação é igual: $result02\nA Divisão é igual: $result03"

#==================================================================================================
echo '\n====================\n'

# INPUT em Shellscript = read  (o -n é para ele não escrever na linha debaixo, e sim na mesma linha)
echo -n "Digite um valor inteiro: " 
# o read tanto guarda/salva a variavel, quanto também atribui um valor a ela com um tipo de 'input'
read varint02

# dando echo no valor digitado e informando o seu dobro com $((valor*2))
echo "O valor digitado foi: $varint02 e o seu dobro é $((varint02*2))" 

#==================================================================================================
echo '\n====================\n'

# COMPARADORES 
# -o -> ou/or
# -a -> e/and
# = -> igual
# != -> diferente 
# -n -> não é nulo
# -z -> é nulo
# -lt -> menor que
# -gt -> maior que
# -le -> menor ou igual
# -ge -> maior ou igual
# -eq -> igual
# -ne -> diferente

#==================================================================================================
echo '\n====================\n'

# CONDICIONAIS

echo -n "Digite o número: "
read num3

# dessa forma ele verifica se a var num3 é igual a 100, se sim então (then) será executado o echo
# se não o else, e o (fi) indica o  final
if [ "$num3" = "100" ];then
    echo "O número digitado é 100!\n"
elif [ "$num3" = 10 ];then
    echo "O número digitado foi $num3 e o seu dobro é $((num3*2))\n"
elif [ "$num3" = 5 -o "$num3" = 0];then
    echo "foi digitado 5 ou 0\n"
else
    echo "O número digitado não é o valor 100!\n"
fi

#==================================================================================================
echo '\n====================\n'

# UTILIZAR FUNÇÕES

# Utilizando o $() para jogar o resultado da função whoami para a variavel função01
função01=$(whoami)
# para executar apenas a função é só inserir o nome dela normalmente
whoami 
