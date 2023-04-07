# Comentario: O codigo solicita que o usuario digite uma senha. Se a senha digitada for "swordfish", 
# a mensagem "Senha Correta!" e exibida. Se a senha digitada for incorreta, o usuario e solicitado a digitar novamente.


senha_padrao = 'swordfish'
password = input('Digite uma senha: ')
for cont in range(100000000000):
    if password == senha_padrao:
        print('Senha Correta!\n')
        break
    else: 
        password = input('\nSenha incorreta!\nDigite uma senha: ')

