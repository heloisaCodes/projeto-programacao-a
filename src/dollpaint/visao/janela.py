# Tkinter
from tkinter import *
import tkinter as tk
import tkinter.filedialog as filedialog
#Import de Visao
from .barradeferramentas import BarraFerramentas
from .areadesenho import *
from .paletadecores import *
from controlador.controladordesenho import *

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Tamanho da janela
        self.geometry("800x400")
        self.title("DollPaint")
        
        # Criando a barra de ferramentas e colocando no lugar
        self.barra = BarraFerramentas(self)
        self.barra.pack(anchor=tk.W, fill=tk.X)
        
        # Área de Desenho
        self.area_desenho = AreaDesenho(self)
        self.area_desenho.pack(expand=True, fill=tk.BOTH)
        
        #CONTROLADOR
        
        # instancia o controlador passando o Canvas e a gavarya com a escolha
        # para vc poder acessar as gavetas do controlador desenho , tera que chmar: self.controlador
        self.controlador = controladordesenho(canvas=self.area_desenho.canvas, escolha_atual=self.barra.escolha_menu,)
        self.controlador.var_selecao = self.barra.var_selecao
        
        # gaveta das cores
        self.paleta = PaletadeCores(self,self.controlador)
        self.controlador.tracoBoxFrame = self.barra.tracoBoxFrame
        self.controlador.preenchimentoBoxFrame = self.barra.preenchimentoBoxFrame

        #paleta atualizada
        self.paleta = PaletadeCores(self, self.controlador)
        self.paleta.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
                        
    
        # commands dos botões de cor da barra de ferramentas
        self.barra.tracoButton.config(command=lambda: self.paleta.definir_modo("traco"))
        self.barra.preenchimentoButton.config(command=lambda: self.paleta.definir_modo("preenchimento"))
        
        # ativa os binds
        self.controlador.vincular_eventos()
        # gaveta dos botoes salvar e abrir
        self.conectar_botoes_arquivo()
        # interface de salvar e abrir

    def solicitar_salvar_desenho(self):
           # para abrir a janela para a escolha de salvar
            caminho = filedialog.asksaveasfilename(
                defaultextension=".dol",
                filetypes=[("Arquivos DollPaint", "*.dol"), ("Todos os arquivos", "*.*")])
            if caminho:
                self.controlador.salvar_arquivo_desenho(caminho)

    def solicitar_abrir_desenho(self):
            #para selecionar a pasta onde ta o desenho
            caminho = filedialog.askopenfilename(
                filetypes=[("Arquivos DollPaint", "*.dol"), ("Todos os arquivos", "*.*")])
        # se tem algo ele ativa
            if caminho:
                self.controlador.abrir_arquivo_desenho(caminho)

    def conectar_botoes_arquivo(self):
            # para conectar as funçoes com os botoes
            self.barra.btn_salvar.config(command=self.solicitar_salvar_desenho)
            self.barra.btn_abrir.config(command=self.solicitar_abrir_desenho)
