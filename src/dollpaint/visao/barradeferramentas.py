
# Parte  dos botoes

import tkinter  as tk
from tkinter import ttk

from controlador.controladordesenho import *
from visao.areadesenho import *

class BarraFerramentas(tk.Frame):
    def __init__(self, master):
        super().__init__(master,bg="#FCE4EC")
        paddings = {'padx': 5, 'pady': 5}

        # tipo de figuras
        #mudei pra tk pra aceitar fonte, cor e etc
        self.label = tk.Label(self, text='TIPO DE FIGURA :', 
                    font=("Arial", 8, "bold"),
                    bg="#FCE4EC")
        self.label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # gaveta do menu
        self.escolha_menu = tk.StringVar(value="Rabisco")# ta rabsico porque a gente vai inciar com isso
        self.var_selecao = tk.BooleanVar(value=False)
        self.var_areasele = tk.BooleanVar(value=False)
        # menu
        self.option_menu = ttk.OptionMenu (self, self.escolha_menu, 'Rabisco', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Círculo', 'Polígono',"Borracha","Poligono Regular",
                                          command=lambda opcao: self.master.controlador.ao_mudar_selecao(opcao))
                    # o commad recebe opçao que foi passado pela escolha e aplicada no metodochamdo la no controlador
        self.option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)
       

        # # cor do traço 
        self.tracoButton = tk.Button(self, text="Cor do Traço", width=12)
        self.tracoButton.grid(column=2, row=0, sticky=tk.W, **paddings)
        self.tracoBoxFrame = tk.Frame(self, height=25, width=25, relief=tk.SUNKEN, borderwidth=3, bg="#000000")
        self.tracoBoxFrame.grid(column=3, row=0, sticky=tk.W, **paddings)

        # # cor de preenchimento 
        self.preenchimentoButton = tk.Button(self, text="Preenchimento", width=12)
        self.preenchimentoButton.grid(column=4, row=0, sticky=tk.W, **paddings)
        self.preenchimentoBoxFrame = tk.Frame(self, height=25, width=25, relief=tk.SUNKEN, borderwidth=3, bg="white")
        self.preenchimentoBoxFrame.grid(column=5, row=0, sticky=tk.W, **paddings)

        # botao para selecao 
        self.selecionarButton = tk.Checkbutton(self, text="Selecionar", variable=self.var_selecao,command=lambda:self.master.controlador.selecao(),indicatoron=False,**paddings,selectcolor="lightblue")
        self.selecionarButton.grid(column=6, row=0, sticky=tk.W, **paddings)
        # colocando o botao no frame
        self.selecionarBoxFrame = tk.Frame(self, height=25, width=25, relief=tk.SUNKEN, borderwidth=3, bg="white")
        self.selecionarBoxFrame.grid(column=7, row=0, sticky=tk.W, **paddings)

        #botao para area selecao
        self.area_selecaoButton = tk.Checkbutton(self, text="Área de Seleção", variable=self.var_areasele,command=lambda:self.master.controlador.area_selecao(),indicatoron=False,**paddings,selectcolor="lightblue")
        self.area_selecaoButton.grid(column=6, row=1, sticky=tk.W, **paddings)
        
        # tudo o que for colocado debaixo dessa linha vai ser empurrado para a direita,lembrar para os nossos proximos botoes
        self.columnconfigure(6, weight=1)
        # # botao de salvar coluna 7 direita
        self.btn_salvar = ttk.Button(self, text="Salvar")
        self.btn_salvar.grid(column=7, row=0, sticky=tk.E, **paddings)

        # # botao abrir coluna 8 direita
        self.btn_abrir = ttk.Button(self, text="Abrir")
        self.btn_abrir.grid(column=8, row=0, sticky=tk.E, **paddings)

        #botoes e frames  do redo e undo
        self.undo_redo_frame = tk.Frame(self)
        self.undo_redo_frame.grid(column=6, row=0, sticky=tk.W, **paddings)
        
        self.btn_undo = tk.Button(self,text="↶",font=("Arial", 14))
        self.btn_undo.grid(column=5, row=1,sticky=tk.W,**paddings)
        self.btn_redo = tk.Button(self,text="↷", font=("Arial", 12))
        self.btn_redo.grid(column=4, row=1, sticky=tk.W, **paddings)
        
