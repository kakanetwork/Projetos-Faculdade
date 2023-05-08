import os
import shutil
import winshell
import tkinter as tk
from tkinter import scrolledtext, messagebox

lista_teste = [
    "C:\\Users\\USUARIO\\OneDrive\\Documents\\s",
    "C:\\Users\\USUARIO\\OneDrive\\Documents\\a",
]

def clear_cache():
    for x in lista_teste:
        nomes = tuple(os.listdir(x))
        for a in nomes:
            try:
                os.remove(f"{x}\\{a}")
                log.insert(tk.END, f"Apagando...: {a}\n")
            except:
                shutil.rmtree(f"{x}\\{a}")
                log.insert(tk.END, f"Apagando Pasta...: {a}\n")

    log.insert(tk.END, "Limpeza de cache concluída com sucesso.\n")

def esvaziar_lixeira():
    if messagebox.askyesno("Atenção", "Deseja esvaziar a lixeira permanentemente?"):
        winshell.recycle_bin().empty(confirm=True, show_progress=True)
        messagebox.showinfo("Concluído", "Lixeira esvaziada com sucesso!")

root = tk.Tk()
root.geometry("600x400")
root.title("Limpeza de Cache e Esvaziamento de Lixeira - By Kakanetwork")
root.iconbitmap('D:\\USUARIO\Documentos\Faculdade\MeusProjetos.py\Projetos-Autorais\Clear-Temp\\limpar.ico')

btn_clear_cache = tk.Button(root, text="Limpar Cache", command=clear_cache)
btn_clear_cache.pack(pady=10)

lixeira_button = tk.Button(root, text="Esvaziar Lixeira", command=esvaziar_lixeira)
lixeira_button.pack()

aviso_label = tk.Label(
    root,
    text="Cuidado! Ao clicar em Sim, todos os arquivos na sua lixeira serão apagados permanentemente.",
    fg="red")
aviso_label.pack()

log = scrolledtext.ScrolledText(root, width=60, height=20)
log.pack(pady=10)

root.mainloop()
