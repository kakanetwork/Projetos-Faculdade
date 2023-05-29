import subprocess

for i in range(60):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Atualizado'])
    subprocess.call(["git", "push", "-u", "origin", "master"])
    
    print(f"Tempo passando: {i+1} segundos")
    
    # Aguarda 1 segundo
    subprocess.call(["ping", "-n", "2", "127.0.0.1", ">nul"])
