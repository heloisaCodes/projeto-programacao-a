# Tkinter
from tkinter import *
from tkinter import colorchooser

# Caminho pra o Python não se perder tadinho 
import sys
import os
import_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if import_path not in sys.path:
    sys.path.append(import_path)

#Imports de Modelo
from modelo.figuras import *
from modelo.figura import *

#Import de Visao
from visao.main import *
from visao.barradeferramentas import *
from visao.areadesenho import *

class ControladorDesenho:
    def __init__(self, canvas, figura_atual):
        self.canvas = canvas
        self.figura_atual = figura_atual
        self.figuras = []
        
        # estado inicial padrão
        self.estado_atual = None 
    
    def mudar_estado(self, novo_estado):
        # função para alternar o estado
        self.estado_atual = novo_estado

    def vincular_eventos(self):
        self.canvas.bind("<Button-1>", self.iniciar_figura_nova)
        self.canvas.bind("<B1-Motion>", self.atualizar_figura_nova) 
        self.canvas.bind("<Motion>", self.atualizar_figura_nova)
        self.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)

    def iniciar_figura_nova(self, event): 
        self.estado_atual.iniciar_figura_nova(event)

    def atualizar_figura_nova(self, event):  
        self.estado_atual.atualizar_figura_nova(event)

    def incluir_figura_nova(self, event): 
        self.estado_atual.incluir_figura_nova(event)
    
    def finalizar_poligono(self, event):
        self.estado_atual.finalizar_poligono(event)

    def desenhar_figuras(self):
        self.canvas.delete("all")
        for fig in self.figuras:
            fig.desenhar(self.canvas)

    def selecionar_cor_traco(self):
        selectedColor = colorchooser.askcolor(title="Cor do Traço")
        if selectedColor[1]: 
            self.cor_traço = selectedColor[1]
            if self.tracoBoxFrame:
                self.tracoBoxFrame.config(bg=self.cor_traço)

    def selecionar_cor_preenchimento(self):
        selectedColor = colorchooser.askcolor(title="Cor de Preenchimento")
        if selectedColor[1]: 
            self.cor_preenchimento = selectedColor[1]
            if self.preenchimentoBoxFrame:
                self.preenchimentoBoxFrame.config(bg=self.cor_preenchimento)