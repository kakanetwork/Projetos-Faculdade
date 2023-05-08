import os, shutil, winshell

lista = ["%userprofile%\AppData\Local\Temp", "%LOCALAPPDATA%\Microsoft\Windows\INetCache", "%windir%\temp", 
"C:\Windows\Prefetch", "C:\\Users\\USUARIO\Recent"]

lista_teste = ["C:\\Users\\USUARIO\OneDrive\Documents\s", "C:\\Users\\USUARIO\OneDrive\Documents\\a"]

for x in lista_teste:
    nomes = tuple(os.listdir(x))
    for a in nomes:
        try:
            os.remove(f'{x}\\{a}')
        except:
            shutil.rmtree(f'{x}\\{a}')
            print(f'Apagando Pasta...: {a}\n')
        else:
            print(f'Apagando...: {a}\n')

winshell.recycle_bin().empty(confirm=True, show_progress=True)
