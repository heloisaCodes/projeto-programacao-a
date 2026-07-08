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
from visao.areadesenho import *
# import das ferramentas

from .ferramentas import modocirculo,modolinha,modopoligono,modorabisco,modoretangulo,modooval


##### é o nosso contexto, as ferramentas contruidas serão feitas para mudar o estado atual
# configuraçoes da tela de inicializaçao

class ControladorDesenho:
    def __init__(self, canvas, escolha_atual):
        self.canvas = canvas
        self.figura_atual = None  # vai comecar com none pq nao vai inicializar nehuma figura # gaveta temporaria 
        self.figuras = []     # figuras salvas
        # nossa gaveta que vai guardar a escolha do menu, la na visão
        self.escolha_menu=escolha_atual
        # gaveta das cores
        self.cor_traço = "black"          
        self.cor_preenchimento = ""       
        
        # Estado inicial padrão 
        # o paranteses pq ta devolvendo um objeto vivo que sera possovel aplicar os metodos
        self.estado_atual = modorabisco() 
    # parte da logistica da mudança
# o args serve para idicar que vai chegar parametros mas vc nao sabe quantos
    def ao_mudar_selecao(self,*args):
        texto=self.escolha_menu.get()
        if texto == "rabisco":
            novo_estado=modorabisco()
        elif texto == "oval":
            novo_estado=modooval
        elif texto == "poligono":
            novo_estado=modopoligono()
        elif texto == linha:
            novo_estado=modolinha()
        elif texto == "círculo":
            novo_estado=modocirculo()
        elif texto == "retângulo":
            novo_estado=modoretangulo()
        else:
          novo_estado = modorabisco()
        # to acessando a classe e aplicando o metodo com o novo resultado
        self.mudar_estado(novo_estado)

    def mudar_estado(self, novo_estado):
        # Função para alternar o estado/ferramenta
        self.estado_atual = novo_estado

    # tudo ok nessa parte
    def vincular_eventos(self):
        self.canvas.bind("<Button-1>", self.iniciar_figura_nova)
        self.canvas.bind("<B1-Motion>", self.atualizar_figura_nova) 
        self.canvas.bind("<Motion>", self.atualizar_figura_nova)
        self.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)

    def iniciar_figura_nova(self, event): 
        if self.estado_atual is not None:
            self.estado_atual.iniciar_figura_nova(event, self) 
            self.desenhar_figuras()
            self.desenhar_figura_nova()

    def atualizar_figura_nova(self, event):  
        if self.estado_atual is not None:
            self.estado_atual.atualizar_figura_nova(event, self)
            self.desenhar_figuras()
            self.desenhar_figura_nova()

    def incluir_figura_nova(self, event): 
        if self.estado_atual is not None:
            self.estado_atual.incluir_figura_nova(event, self)
            self.desenhar_figuras()
            self.desenhar_figura_nova()
    
    def finalizar_poligono(self, event):
        if self.estado_atual is not None:
            self.estado_atual.finalizar_poligono(event, self)
            self.desenhar_figuras()
            self.desenhar_figura_nova()

    def desenhar_figuras(self):
        # Limpa o canvas e redesenha as figuras salvas
        self.canvas.delete("all")
        for fig in self.figuras:
            fig.desenhar(self.canvas)

    def desenhar_figura_nova(self):
        # Desenha a figura da gaveta com linha tracejada        
        if self.figura_atual is not None:
            self.figura_atual.desenhar(self.canvas, dash=(4, 2))

        def incompleta(self, figura):
            return figura.esta_incompleta()

    def selecionar_cor_traco(self):
        selectedColor = colorchooser.askcolor(title="Cor do Traço")
        if selectedColor[1]: 
            self.cor_traço = selectedColor[1]
            if hasattr(self, 'tracoBoxFrame') and self.tracoBoxFrame:
                self.tracoBoxFrame.config(bg=self.cor_traço)

    def selecionar_cor_preenchimento(self):
        selectedColor = colorchooser.askcolor(title="Cor de Preenchimento")
        if selectedColor[1]: 
            self.cor_preenchimento = selectedColor[1]
            if hasattr(self, 'preenchimentoBoxFrame') and self.preenchimentoBoxFrame:
                self.preenchimentoBoxFrame.config(bg=self.cor_preenchimento)
