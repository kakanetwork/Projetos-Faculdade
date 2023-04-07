# Coment: A variavel "senha_padrao" armazena a string 'swordfish'. Enquanto o valor booleano "True" for mantido, 
#o laco while sera executado. O usuario e solicitado a digitar uma senha e, caso o valor digitado seja igual ao valor armazenado na variavel 
#"senha_padrao", a string 'Senha Correta!' e impressa na tela e o laco e quebrado. Se o valor digitado for diferente, a string 'A senha esta incorreta, 
#tente novamente!' e impressa na tela e o laco e executado novamente.


senha_padrao = 'swordfish'
while True:
    password = input('Digite uma senha: ')
    if password == senha_padrao:
        print('Senha Correta!\n')
        break
    else: 
        print('A senha está incorreta, tente novamente!\n')

