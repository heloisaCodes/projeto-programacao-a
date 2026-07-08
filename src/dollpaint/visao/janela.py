# Tkinter
from tkinter import *
import tkinter as tk

#Import de Visao
from .barradeferramentas import BarraFerramentas
from .areadesenho import *
from controlador.controladordesenho import *

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Tamanho da janela
        self.geometry("1200x800")
        self.title("DollPaint")
        
        # Criando a barra de ferramentas e colocando no lugar
        self.barra = BarraFerramentas(self)
        self.barra.pack(anchor=tk.W, fill=tk.X)
        
        # Área de Desenho
        self.area_desenho = AreaDesenho(self)
        self.area_desenho.pack(expand=True, fill=tk.BOTH)
        
        
        #CONTROLADOR
        
        # instancia o controlador passando o Canvas e a Variável de controle de tipo de figura
        self.controlador = controladordesenho(canvas=self.area_desenho.canvas, escolha_atual=self.barra.escolha_menu)
        
        # referências dos pequenos frames coloridos para o controlador atualizar
        self.controlador.tracoBoxFrame = self.barra.tracoBoxFrame
        self.controlador.preenchimentoBoxFrame = self.barra.preenchimentoBoxFrame
        
        # commands dos botões de cor da barra de ferramentas
        self.barra.tracoButton.config(command=self.controlador.selecionar_cor_traco)
        self.barra.preenchimentoButton.config(command=self.controlador.selecionar_cor_preenchimento)
        
        # ativa os binds
        self.controlador.vincular_eventos()
        