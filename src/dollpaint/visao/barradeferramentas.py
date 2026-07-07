
# Parte  dos botoes

import tkinter  as tk
from tkinter import ttk

# caminho pro python
import sys
import os
import_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if import_path not in sys.path:
    sys.path.append(import_path)

from controlador.canvascontroller import *
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

        #controlador e canvas
        self.area_desenho = AreaDesenho(self)
        self.controlador = ControladorDesenho(canvas=self.area_desenho.canvas, escolha_atual=self.escolha_menu)
        # nosso sensor, ele vai capturar e mandar pro controler

        ### preciso mudar isso ainda o segundo argumento é o nome dafunçao que  vai ter no controlador responsavel por mudar 
        self.escolha_menu.trace_add("write", self.escolha_menu.mudar_estado)

        # menu
        self.option_menu = ttk.OptionMenu(self, self.escolha_menu, 'linha', 'linha', 'rabisco', 'retângulo', 'oval', 'círculo', 'poligono')
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
    
        