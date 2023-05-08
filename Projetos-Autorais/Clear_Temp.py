import os, shutil, winshell

lista = ["%userprofile%\AppData\Local\Temp", "%LOCALAPPDATA%\Microsoft\Windows\INetCache", "%windir%\temp", 
"C:\Windows\Prefetch", "C:\\Users\\USUARIO\Recent"]

def clear_temp():
    lista_teste = ["C:\\Users\\USUARIO\\OneDrive\\Documents\\s", "C:\\Users\\USUARIO\\OneDrive\\Documents\\a"]

    for x in lista_teste:
        nomes = tuple(os.listdir(x))
        for a in nomes:
            try:
                os.remove(f'{x}\\{a}')
            except:
                shutil.rmtree(f'{x}\\{a}')
                messagebox.showwarning(title="Aviso", message=f'Apagando Pasta...: {a}\n')
            else:
                messagebox.showwarning(title="Aviso", message=f'Apagando...: {a}\n')

    confirmar = messagebox.askyesno(title="Confirmação", message="Tem certeza que deseja esvaziar a lixeira?")
    if confirmar:
        winshell.recycle_bin().empty(confirm=True, show_progress=True)
        messagebox.showinfo(title="Sucesso", message="Lixeira esvaziada com sucesso!")
    else:
        messagebox.showinfo(title="Cancelado", message="Ação cancelada pelo usuário.")

# Cria a janela principal
root = tk.Tk()

# Cria o botão para esvaziar a lixeira
button = tk.Button(root, text="Esvaziar Lixeira", command=clear_temp)
button.pack()

# Inicia o loop principal da interface
root.mainloop()