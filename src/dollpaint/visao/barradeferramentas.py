
# Parte  dos botoes

import tkinter  as tk
from tkinter import ttk

from controlador.controladordesenho import *
from visao.areadesenho import *

class BarraFerramentas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        paddings = {'padx': 5, 'pady': 5}

        # tipo de figuras
        self.label = ttk.Label(self, text='Tipo de Figura :')
        self.label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # gaveta do menu
        self.escolha_menu = tk.StringVar(value="linha")# ta linha porque a gente vai inciar com isso


        # menu
        self.option_menu = ttk.OptionMenu (self, self.escolha_menu, 'linha', 'linha', 'rabisco', 'retângulo', 'oval', 'círculo', 'poligono',
                                          command=lambda opcao: self.master.controlador.ao_mudar_selecao(opcao))
        self.option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # cor do traço
        self.tracoButton = tk.Button(self, text="Cor do Traço", width=12)
        self.tracoButton.grid(column=2, row=0, sticky=tk.W, **paddings)
        self.tracoBoxFrame = tk.Frame(self, height=25, width=25, relief=tk.SUNKEN, borderwidth=3, bg="#000000")
        self.tracoBoxFrame.grid(column=3, row=0, sticky=tk.W, **paddings)

        # cor de preenchimento
        self.preenchimentoButton = tk.Button(self, text="Preenchimento", width=12)
        self.preenchimentoButton.grid(column=4, row=0, sticky=tk.W, **paddings)
        self.preenchimentoBoxFrame = tk.Frame(self, height=25, width=25, relief=tk.SUNKEN, borderwidth=3, bg="white") 
        self.preenchimentoBoxFrame.grid(column=5, row=0, sticky=tk.W, **paddings)
    
        