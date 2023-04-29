import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class TreeView:
    def __init__(self, parent):
        self.parent = parent
        self.tree = ttk.Treeview(self.parent)
        self.tree.pack(side="left", fill="y")
        
        # Define um dicionário para armazenar os ids dos nodos e seus respectivos nomes
        self.id_to_name = {}

        # Cria um evento de duplo clique para renomear a pasta
        self.tree.bind("<Double-1>", self.rename_folder)

    def rename_folder(self, event):
        # Pega o item clicado
        item = self.tree.selection()[0]

        # Define o nome antigo da pasta
        old_name = self.id_to_name[item]

        # Cria uma janela de diálogo para pegar o novo nome
        new_name = tk.simpledialog.askstring("Renomear pasta", "Digite o novo nome para a pasta", initialvalue=old_name)

        if new_name:
            # Atualiza o nome no dicionário
            self.id_to_name[item] = new_name

            # Atualiza o nome na árvore
            self.tree.item(item, text=new_name)

            # Renomeia a pasta no sistema de arquivos
            path = self.get_path(item)
            new_path = os.path.join(os.path.dirname(path), new_name)
            os.rename(path, new_path)

    def add_folder(self, parent, name):
        # Adiciona a pasta na árvore
        folder_id = self.tree.insert(parent, "end", text=name)

        # Armazena o nome da pasta no dicionário
        self.id_to_name[folder_id] = name

        # Cria a pasta no sistema de arquivos
        path = self.get_path(folder_id)
        os.mkdir(path)

    def remove_folder(self):
        # Pega o item selecionado
        item = self.tree.selection()[0]

        # Pega o nome da pasta
        name = self.id_to_name[item]

        # Confirma se o usuário deseja realmente remover a pasta
        confirm = messagebox.askyesno("Remover pasta", f"Deseja remover a pasta '{name}'?")

        if confirm:
            # Remove a pasta da árvore
            self.tree.delete(item)

            # Remove a pasta do sistema de arquivos
            path = self.get_path(item)
            os.rmdir(path)

    def get_path(self, item):
        # Pega o caminho da pasta na árvore
        path_list = [self.id_to_name[item]]
        parent_item = self.tree.parent(item)

        while parent_item:
            path_list.insert(0, self.id_to_name[parent_item])
            parent_item = self.tree.parent(parent_item)

        # Retorna o caminho completo
        path = os.path.join(root_folder.get(), *path_list)
        return path


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Organizador de pastas")
        self.window.geometry("600x400")

        # Cria um Frame para a seleção da pasta raiz
        root_frame = ttk.Frame(self.window)
        root_frame.pack(pady=10)

        # Cria um Label para a pasta raiz
        ttk.Label(root_frame, text="Pasta raiz:").pack(side="left")

        # Cria um Entry para a seleção da pasta raiz
        self.root_folder = tk.StringVar()
        root_entry = ttk.Entry(root_frame, textvariable=self.root_folder)
        root
