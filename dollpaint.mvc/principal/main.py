# Tkinter
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

#Import do Controlador
from controlador.main import *
from controlador.controla import *


# Definição das cores iniciais padrão
cor_traço = "#000000"          # Preto para as bordas/linhas
cor_preenchimento = ""         # Sem preenchimento inicial

#Mostrar Janela
if __name__ == "__main__":
    app = JanelaPrincipal()

    app.mainloop()