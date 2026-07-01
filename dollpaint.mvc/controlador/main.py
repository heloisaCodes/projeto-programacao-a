## Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

# Caminho pra o Python não se perder tadinho 
import sys
import os
import_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if import_path not in sys.path:
    sys.path.append(import_path)

#Imports de Modelo
from modelo.main import *
from modelo.figura import figura
from modelo.figura import *

#Imports de Main
from principal.main import *

#Import de Visao
from visao.main import *
from visao.barradeferramentas import tipo_figura_var
from visao.barradeferramentas import tracoBoxFrame
from visao.barradeferramentas import preenchimentoBoxFrame
from visao.areadesenho import AreaDesenho
#Import do Controlador
from controlador.main import *

def desenhar_figuras():
    AreaDesenho.delete("all")
    for fig in figuras:
        fig.desenhar(AreaDesenho)


def desenhar_figura_nova():
    if figura_nova is not None:
        figura_nova.desenhar(AreaDesenho, dash=(4, 2))


def incompleta(figura):
    tipo = type(figura).__name__.lower() # pegar o nome da subclasse

    if tipo in ("linha", "retangulo", "oval"):
        return (figura.pontos[0], figura.pontos[1]) == (figura.pontos[2], figura.pontos[3])

    elif tipo == "circulo":
        return figura.pontos[2] < 1.0

    elif tipo == "poligono":
        return len(figura.pontos) < 6

    else: # rabisco
        return len(figura.pontos) <= 2

#Função para selecionar a cor do traço (borda)
def selecionar_cor_traco():
    global cor_traço
    selectedColor = colorchooser.askcolor(title="Cor do Traço")
    if selectedColor[1]: 
        cor_traço = selectedColor[1]
        tracoBoxFrame.config(bg=cor_traço)

#Função para selecionar a cor do preenchimento
def selecionar_cor_preenchimento():
    global cor_preenchimento
    selectedColor = colorchooser.askcolor(title="Cor de Preenchimento")
    if selectedColor[1]: 
        cor_preenchimento = selectedColor[1]
        preenchimentoBoxFrame.config(bg=cor_preenchimento)

