import subprocess


subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Atualizado'])
subprocess.call(["git", "push", "-u", "origin", "master"])