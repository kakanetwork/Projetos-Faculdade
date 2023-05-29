
# Código para realizar commit e push automatico no GITHUB

import subprocess, time

print('='*100)
modo = input('\nEscolha o Modo Automatico(A) ou modo Único(U): ')

if modo == 'A':
    while True:
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'Atualizado'])
        subprocess.call(["git", "push", "-u", "origin", "master"])
        time.sleep(120) 
elif modo == 'U':
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Atualizado'])
    subprocess.call(["git", "push", "-u", "origin", "master"])
else:
    print('Escolha um modo válido!')