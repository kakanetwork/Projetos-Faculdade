import tkinter as tk
from tkinter import messagebox
import os

class FolderTemplate:
    def __init__(self, master):
        self.master = master
        self.master.title("Folder Template")
        
        self.template_frame = tk.Frame(self.master)
        self.template_frame.pack(side=tk.TOP, padx=10, pady=10)
        
        self.root_label = tk.Label(self.template_frame, text="Root Folder:")
        self.root_label.grid(row=0, column=0, sticky="W")
        
        self.root_entry = tk.Entry(self.template_frame, width=50)
        self.root_entry.grid(row=0, column=1, pady=5)
        
        self.template_label = tk.Label(self.template_frame, text="Folder Template:")
        self.template_label.grid(row=1, column=0, sticky="W")
        
        self.template_text = tk.Text(self.template_frame, width=50, height=10)
        self.template_text.grid(row=1, column=1, pady=5)
        
        self.add_button = tk.Button(self.template_frame, text="Add Folder", command=self.add_folder)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.rename_button = tk.Button(self.template_frame, text="Rename Folder", command=self.rename_folder)
        self.rename_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.create_button = tk.Button(self.template_frame, text="Create Folders", command=self.create_folders)
        self.create_button.grid(row=3, column=1, pady=10)
        
        self.folder_list = []
        self.folder_count = 1
        
    def add_folder(self):
        self.folder_list.append("Folder " + str(self.folder_count))
        self.folder_count += 1
        self.template_text.insert(tk.END, self.folder_list[-1] + "\n")
        
    def rename_folder(self):
        selected_folder = self.template_text.get("sel.first", "sel.last")
        if selected_folder:
            new_folder_name = simpledialog.askstring("Rename Folder", "Enter a new name for the folder", parent=self.master)
            if new_folder_name:
                self.template_text.delete(selected_folder)
                self.template_text.insert(selected_folder, new_folder_name)
        else:
            messagebox.showwarning("No folder selected", "Please select a folder to rename.")
            
    def create_folders(self):
        root_folder = self.root_entry.get()
        if not root_folder:
            messagebox.showwarning("No root folder specified", "Please specify a root folder.")
            return
        
        folder_template = self.template_text.get("1.0", tk.END).strip()
        if not folder_template:
            messagebox.showwarning("Empty folder template", "Please specify a folder template.")
            return
        
        folder_list = folder_template.split("\n")
        
        for folder in folder_list:
            folder_path = os.path.join(root_folder, folder)
            try:
                os.makedirs(folder_path)
            except FileExistsError:
                pass
            
        messagebox.showinfo("Folders created", "Folders created successfully.")

root = tk.Tk()
app = FolderTemplate(root)
root.mainloop()
