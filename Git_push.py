
# Código para realizar commit e push automatico no GITHUB

import subprocess, time
while True:
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Atualizado'])
    subprocess.call(["git", "push", "-u", "origin", "master"])
    print("Tempo passando:", time.strftime("%H:%M:%S", time.gmtime()))
    time.sleep(60)
    