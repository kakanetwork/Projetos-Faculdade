
user=$(whoami)

echo "\nBem vindo $user - Calculadora Simples\n"
echo -n 'Informe um valor inteiro para a equação: '
read var1
echo -n 'Informe um segundo valor inteiro para a equação: '
read var2

echo "\nO número digitado foi: $var1 e $var2"
echo "\nA soma é igual: $((var1+var2))\nA Subtração é igual: $((var1-var2))\n\
A Multiplicação é igual: $((var1*var2))\nA Divisão é igual: $((var1/var2))\n"