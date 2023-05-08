import os, shutil, winshell
import tkinter as tk
from tkinter import scrolledtext, messagebox

lista = [
    "%userprofile%\\AppData\\Local\\Temp",
    "%LOCALAPPDATA%\\Microsoft\\Windows\\INetCache",
    "%windir%\\temp",
    "C:\\Windows\\Prefetch",
    "C:\\Users\\USUARIO\\Recent",
]

def clear_cache():
    total_size = 0
    log.tag_config("white", foreground="white")
    for x in lista:
        nomes = tuple(os.listdir(x))
        for a in nomes:
            file_path = os.path.join(x, a)
            try:
                file_size = os.path.getsize(file_path)
                os.remove(file_path)
                total_size += file_size
                log.insert(tk.END, f"Apagando...: {a}\n", "white")
            except:
                shutil.rmtree(file_path)
                log.insert(tk.END, f"Apagando Pasta...: {a}\n", "white")
    total_size_mb = round(total_size / 1048576, 2)

    # Define a cor do texto do log para a tag "white"
    log.insert(tk.END, f"Limpeza de cache concluída com sucesso. Total excluído: {total_size_mb} MB\n", "white")
    
def esvaziar_lixeira():
    if messagebox.askyesno("Atenção", "Deseja esvaziar a lixeira permanentemente?"):
        winshell.recycle_bin().empty(confirm=False, show_progress=False)
        messagebox.showinfo("Concluído", "Lixeira esvaziada com sucesso!")
        aviso_label.configure(text="Lixeira esvaziada com sucesso!", fg="white")

root = tk.Tk()
root.geometry("400x400")
root.title("Limpeza de Cache e Esvaziamento de Lixeira - By Kakanetwork")
root.configure(bg='#20B2AA')

btn_clear_cache = tk.Button(root, text="Limpar Cache", command=clear_cache, bg="white")
btn_clear_cache.pack(pady=20)

lixeira_button = tk.Button(root, text="Esvaziar Lixeira", command=esvaziar_lixeira, bg="white")
lixeira_button.pack()

aviso_label = tk.Label(
    root,
    text="Cuidado!\n Ao clicar em Sim, todos os arquivos da sua \nlixeira serão apagados permanentemente.\n\n Informações:",
    fg="white", bg='#20B2AA')
aviso_label.pack()

log = scrolledtext.ScrolledText(root, width=40, height=10, bg='#008B8B')
log.pack(pady=10)

aviso_label = tk.Label(
    root,
    text="### created by Kakanetwork ###",
    fg="white", bg='#20B2AA')
aviso_label.pack()

root.mainloop()
