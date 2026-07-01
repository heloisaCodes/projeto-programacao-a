import tkinter as tk
from barradeferramentas import BarraFerramentas
from areadesenho import AreaDesenho

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # tamanho da janela
        self.geometry("1920x1920")
        self.title("DollDraw")
        
        # criando a barra de ferramentas e colocando no lugar
        self.barra = BarraFerramentas(self)
        self.barra.pack(anchor=tk.W, fill=tk.X)
        
        # Área de Desenho dentro do canvas
        self.area_desenho = AreaDesenho(self)
        self.area_desenho.pack(expand=True, fill=tk.BOTH)