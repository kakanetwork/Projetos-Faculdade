import os
import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        master.title("Criador de pastas")

        self.folders = []

        # label e botão para selecionar a pasta raiz
        self.root_dir_label = tk.Label(master, text="Pasta raiz:")
        self.root_dir_label.pack(side=tk.LEFT, padx=(10, 0), pady=10)
        self.root_dir_var = tk.StringVar()
        self.root_dir_entry = tk.Entry(master, textvariable=self.root_dir_var, width=40)
        self.root_dir_entry.pack(side=tk.LEFT, padx=(0, 10), pady=10)
        self.select_root_dir_button = tk.Button(master, text="Selecionar", command=self.select_root_dir)
        self.select_root_dir_button.pack(side=tk.LEFT, pady=10)

        # label e botão para adicionar nova pasta
        self.folder_name_label = tk.Label(master, text="Nome da pasta:")
        self.folder_name_label.pack(padx=10)
        self.tree_widget.itemDoubleClicked.connect(self.rename_folder)
        self.folder_name_var = tk.StringVar()
        self.folder_name_entry = tk.Entry(master, textvariable=self.folder_name_var, width=40)
        self.folder_name_entry.pack(padx=10)
        self.add_folder_button = tk.Button(master, text="Adicionar pasta", command=self.add_folder)
        self.add_folder_button.pack(pady=10)

        # label e listbox para mostrar as pastas criadas
        self.folders_label = tk.Label(master, text="Pastas criadas:")
        self.folders_label.pack(padx=10)
        self.folders_listbox = tk.Listbox(master, width=50)
        self.folders_listbox.pack(padx=10)

        # botão para criar as pastas na pasta raiz
        self.create_folders_button = tk.Button(master, text="Criar pastas", command=self.create_folders)
        self.create_folders_button.pack(pady=10)

    def select_root_dir(self):
        # abre uma janela para selecionar a pasta raiz
        root_dir = filedialog.askdirectory()
        self.root_dir_var.set(root_dir)

    def add_folder(self):
        # adiciona uma nova pasta à lista de pastas criadas pelo usuário
        btn_create_folders = QtWidgets.QPushButton("Create Folders", self)
        btn_create_folders.clicked.connect(self.create_folders_from_template)
        layout.addWidget(btn_create_folders)        
        folder_name = self.folder_name_var.get()
        self.folders.append(folder_name)
        self.folders_listbox.insert(tk.END, folder_name)
    

    def create_folders(self):
        # cria as pastas correspondentes na pasta raiz selecionada
        root_dir = self.root_dir_var.get()
        for folder_name in self.folders:
            folder_path = os.path.join(root_dir, folder_name)
            os.makedirs(folder_path)

        # limpa a lista de pastas criadas pelo usuário
        self.folders = []
        self.folders_listbox.delete(0, tk.END)
    def rename_folder(self, item, column):
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        self.tree_widget.editItem(item)
        new_folder_name = item.text(0)
        if new_folder_name:
            parent_folder = item.parent()
            if parent_folder:
                current_path = self.get_path(parent_folder) + "/"
                old_folder_name = item.toolTip(0)
                new_folder_path = current_path + new_folder_name
                try:
                    os.rename(current_path + old_folder_name, new_folder_path)
                except Exception as e:
                    print("Error renaming folder: ", e)
                else:
                    item.setToolTip(0, new_folder_name)
                    item.setIcon(0, self.folder_icon)
        else:
            item.setText(0, item.toolTip(0))


root = tk.Tk()
app = App(root)
root.mainloop()

