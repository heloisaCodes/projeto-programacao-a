# Tkinter
from tkinter import *
import tkinter as tk

# Caminho pra o Python não se perder tadinho 
import sys
import os
import_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if import_path not in sys.path:
    sys.path.append(import_path)

#Import de Visao
from visao.barradeferramentas import *
from visao.areadesenho import *


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
        self.controlador = ControladorDesenho(canvas=self.area_desenho.canvas, figura_atual=self.barra.figura_atual)
        
        # referências dos pequenos frames coloridos para o controlador atualizar
        self.controlador.tracoBoxFrame = self.barra.tracoBoxFrame
        self.controlador.preenchimentoBoxFrame = self.barra.preenchimentoBoxFrame
        
        # commands dos botões de cor da barra de ferramentas
        self.barra.tracoButton.config(command=self.controlador.selecionar_cor_traco)
        self.barra.preenchimentoButton.config(command=self.controlador.selecionar_cor_preenchimento)
        
        # ativa os binds
        self.controlador.vincular_eventos()
        