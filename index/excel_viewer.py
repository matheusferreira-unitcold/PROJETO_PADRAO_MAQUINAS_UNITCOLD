import pandas as pd
import tkinter as tk
from tkinter import ttk

class ExcelViewerApp:
    def __init__(self, root, excel_file):
        self.root = root
        self.root.title("Visualizador de Planilha Excel")
        
        # Carregar os dados do Excel
        try:
            self.df = pd.read_excel(excel_file)
            self.create_widgets()
        except Exception as e:
            tk.Label(root, text=f"Erro ao carregar arquivo: {e}", fg="red").pack()
    
    def create_widgets(self):
        # Frame para os controles
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Adicionar um campo de pesquisa
        tk.Label(control_frame, text="Pesquisar:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(control_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.update_search)
        
        # Treeview para mostrar os dados
        self.tree = ttk.Treeview(self.root)
        
        # Configurar as colunas
        self.tree["columns"] = list(self.df.columns)
        self.tree.column("#0", width=0, stretch=tk.NO)  # Coluna fantasma
        
        for col in self.df.columns:
            self.tree.column(col, anchor=tk.W, width=100)
            self.tree.heading(col, text=col, anchor=tk.W)
        
        # Adicionar os dados
        for index, row in self.df.iterrows():
            self.tree.insert("", tk.END, values=list(row))
        
        # Adicionar barra de rolagem
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def update_search(self, event):
        search_term = self.search_entry.get().lower()
        
        # Limpar a treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Filtrar e adicionar os dados que correspondem à pesquisa
        for index, row in self.df.iterrows():
            if any(str(cell).lower().find(search_term) != -1 for cell in row):
                self.tree.insert("", tk.END, values=list(row))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    
    # Substitua pelo caminho do seu arquivo Excel
    excel_file = "C:\\Users\\unitc\\Unitcold\\TI Unitcold - Documentos\\PROJETO_PADRAO_MAQUINAS_UNITCOLD\\Relacao_acessorios.xlsx"

    app = ExcelViewerApp(root, excel_file)
    root.mainloop()