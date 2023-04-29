import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Criar Árvore de Pastas")
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

label_frame = ttk.LabelFrame(main_frame, text="Criar Template de Árvore de Pastas")
label_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label = ttk.Label(label_frame, text="Digite o nome da pasta raiz:")
label.pack(padx=10, pady=10)

entry = ttk.Entry(label_frame)
entry.pack(padx=10, pady=10)

button_frame = ttk.Frame(label_frame)
button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

add_button = ttk.Button(button_frame, text="Adicionar Pasta")
add_button.pack(side=tk.LEFT, padx=10)

remove_button = ttk.Button(button_frame, text="Remover Pasta")
remove_button.pack(side=tk.LEFT, padx=10)

rename_button = ttk.Button(button_frame, text="Renomear Pasta")
rename_button.pack(side=tk.LEFT, padx=10)

treeview_frame = ttk.Frame(label_frame)
treeview_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

treeview = ttk.Treeview(treeview_frame)
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
def add_folder():
    selected_item = treeview.focus()
    if not selected_item:
        parent_item = ""
    else:
        parent_item = selected_item
    treeview.insert(parent_item, "end", text="Nova Pasta")

def remove_folder():
    selected_item = treeview.focus()
    treeview.delete(selected_item)

def rename_folder():
    selected_item = treeview.focus()
    treeview.item(selected_item, open=True)
    treeview.edit(selected_item)
add_button.config(command=add_folder)
remove_button.config(command=remove_folder)
rename_button.config(command=rename_folder)

root.mainloop()
