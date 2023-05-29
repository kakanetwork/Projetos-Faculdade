
# Código para realizar commit e push automatico no GITHUB

import subprocess, time

print('='*100)

modo = input('\nEscolha o Modo Automatico(A) ou modo Único(U): ').upper()

commit_name = 'Atualizado'
branch_origin = 'master'

if modo == 'A':
    while True:
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', commit_name])
        subprocess.call(["git", "push", "-u", "origin", branch_origin])
        time.sleep(120) 
elif modo == 'U':
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_name])
    subprocess.call(["git", "push", "-u", "origin", branch_origin])
else:
    print('Escolha um modo válido!')