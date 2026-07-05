
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
        
        # substituindo as variáveis globais
        self.figuras = []
        self.figura_nova = None
        self.cor_traço = "#000000"        # Cor padrão: preto
        self.cor_preenchimento = ""     # Cor padrão: transparente/
        
        self.tracoBoxFrame = None
        self.preenchimentoBoxFrame = None  # Referências para os frames de feedback visual (opcional)
     

    def vincular_eventos(self):
        self.canvas.bind("<Button-1>", self.iniciar_figura_nova)
        self.canvas.bind("<B1-Motion>", self.atualizar_figura_nova)  # Arrastar para figuras normais
        self.canvas.bind("<Motion>", self.atualizar_figura_nova)     # Mover livre para o polígono
        self.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)

    def iniciar_figura_nova(self, event): 
        tipo = self.figura_atual.get().lower()
        
        # Adiciona pontos a cada clique se for polígono
        if tipo == "poligono":
            if self.figura_nova is None or type(self.figura_nova).__name__.lower() != 'poligono':
                # Primeiro ponto do polígono
                self.figura_nova = poligono([event.x, event.y, event.x, event.y], self.cor_traço, self.cor_preenchimento)
            else:
                # Já existe um polígono em construção, adiciona o novo ponto clicado
                self.figura_nova.pontos[-2] = event.x
                self.figura_nova.pontos[-1] = event.y
                self.figura_nova.pontos.extend([event.x, event.y])
            
            self.desenhar_figuras()
            self.desenhar_figura_nova()
            

        # Lógica normal para as outras figuras (arrastar e soltar)
        if tipo == 'círculo':
            self.figura_nova = circulo([event.x, event.y, 0], self.cor_traço, self.cor_preenchimento)
        elif tipo == 'linha':
            self.figura_nova = linha([event.x, event.y, event.x, event.y], self.cor_traço, self.cor_preenchimento)
        elif tipo == 'retângulo':
            self.figura_nova = retangulo([event.x, event.y, event.x, event.y], self.cor_traço, self.cor_preenchimento)
        elif tipo == 'oval':
            self.figura_nova = oval([event.x, event.y, event.x, event.y], self.cor_traço, self.cor_preenchimento)
        else: # rabisco
            self.figura_nova = rabisco([event.x, event.y], self.cor_traço, self.cor_preenchimento)

    def atualizar_figura_nova(self, event):
        if self.figura_nova is None: 
            return
            
        tipo = type(self.figura_nova).__name__.lower()
            
        if tipo == 'rabisco':
            self.figura_nova.pontos.extend([event.x, event.y])
                
        elif tipo == 'circulo':
            x_centro = self.figura_nova.pontos[0]
            y_centro = self.figura_nova.pontos[1]
            raio = ((x_centro - event.x)**2 + (y_centro - event.y)**2) ** 0.5
            self.figura_nova.pontos[2] = raio
                
        elif tipo == 'poligono':
            # Atualiza a linha elástica guiada pela posição atual do mouse
            self.figura_nova.pontos[-2] = event.x
            self.figura_nova.pontos[-1] = event.y
                
        else: # Oval, Retângulo, Linha
            self.figura_nova.pontos[2] = event.x
            self.figura_nova.pontos[3] = event.y

        self.desenhar_figuras()
        self.desenhar_figura_nova()

    def incluir_figura_nova(self, event): 
        if self.figura_nova is None:  
            return
            
        tipo = type(self.figura_nova).__name__.lower()
        # Se for polígono, ignore o evento de soltar o botão (ele fecha no duplo clique)
        if tipo == 'poligono':
            return
            
        if not self.incompleta(self.figura_nova): 
            self.figuras.append(self.figura_nova) 
            
        self.figura_nova = None  
        self.desenhar_figuras()

    def finalizar_poligono(self, event):
        if self.figura_nova is None:
            return
            
        tipo = type(self.figura_nova).__name__.lower()
        if tipo == 'poligono':
            # Remove o último par de pontos temporários criados pelo rastro do mouse
            if len(self.figura_nova.pontos) >= 6:
                self.figura_nova.pontos = self.figura_nova.pontos[:-2]
                if not self.incompleta(self.figura_nova):
                    self.figuras.append(self.figura_nova)
            
            self.figura_nova = None
            self.desenhar_figuras()

    def desenhar_figuras(self):
        self.canvas.delete("all")
        for fig in self.figuras:
            fig.desenhar(self.canvas)

    def desenhar_figura_nova(self):
        if self.figura_nova is not None:
            self.figura_nova.desenhar(self.canvas, dash=(4, 2))

    def incompleta(self, figura):
        tipo = type(figura).__name__.lower()

        if tipo in ("linha", "retangulo", "oval"):
            return (figura.pontos[0], figura.pontos[1]) == (figura.pontos[2], figura.pontos[3])
        elif tipo == "circulo":
            return figura.pontos[2] < 1.0
        elif tipo == "poligono":
            return len(figura.pontos) < 6
        else: # rabisco
            return len(figura.pontos) <= 2

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