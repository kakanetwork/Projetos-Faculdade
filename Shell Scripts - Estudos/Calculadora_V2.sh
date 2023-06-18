#!/bin/bash
#!/bin/bash

user=$(whoami)

echo "\nBem vindo $user - Calculadora Simples\n"
echo -n 'informe o tipo de equação 1(+), 2(-), 3(*) ou 4(/): '
read option

echo -n 'Informe um valor inteiro para a equação: '
read var1
echo -n 'Informe um segundo valor inteiro para a equação: '
read var2
echo "\nO número digitado foi: $var1 e $var2"

if [ $option -eq 1 ];then
    echo "A soma é igual: $((var1+var2))\n"
elif [ $option -eq 2 ];then
    echo "A Subtração é igual: $((var1-var2))\n"
elif [ $option -eq 3];then
    echo "A Multiplicação é igual: $((var1*var2))\n"
elif [ $option -eq 4 ];then
    echo "A Divisão é igual: $((var1/var2))\n"
else 
    echo "Informe um número correto!\n"
fi

