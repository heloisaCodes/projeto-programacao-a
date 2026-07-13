#imports
# Tkinter
from tkinter import *
import tkinter as tk
from controlador.controladordesenho import *
from tkinter import colorchooser

class PaletadeCores(tk.Frame):
    def __init__(self, master, controlador):
        super().__init__(master, relief=tk.RAISED, borderwidth=2,
                         bg="#FCE4EC") # fundo rosa pastel
        self.controlador = controlador

        #lista de cores
        self.cores = self.controlador.cores

        #indicador de cor atual
        self.frame_indicador = tk.Frame(self, width=40, height=40, bg="#FCE4EC", relief=tk.SUNKEN, borderwidth=2)
        self.frame_indicador.pack(side=tk.LEFT, padx=5, pady=5)
        self.frame_indicador.pack_propagate(False) # Mantém o tamanho fixo de 40x40

        #frame do indicador
        self.caixa_cor = tk.Frame(self.frame_indicador, bg="black", width=25, height=25, relief=tk.RAISED, borderwidth=2)
        self.caixa_cor.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #grade para a paleta
        self.grid_cores = tk.Frame(self, bg="#FCE4EC")
        self.grid_cores.pack(side=tk.LEFT, padx=5, pady=5)

        self.criar_botoes_paleta()

    def definir_modo(self,modo):
        self.modo_atual = modo
        if modo == "traco":
            self.caixa_cor.config(bg=self.controlador.cor_traço)
            self.controlador.notificacoes("MUDAR COR DO TRAÇO ATIVADO")
        if modo == "preenchimento":
            self.controlador.notificacoes("MUDAR COR DO PREENCHIMENTO ATIVADO")
            self.caixa_cor.config(bg=self.controlador.cor_preenchimento)
            

    def criar_botoes_paleta(self):
        #quantidade de colunas
        colunas = 14

        for indice, cor in enumerate(self.cores):
            linha = indice // colunas
            coluna = indice % colunas

             # cria cada quadradinho de cor
            btn_cor = tk.Label(self.grid_cores, bg=cor,activebackground=cor, width=2, height=1, relief=tk.RAISED, borderwidth=2)
            btn_cor.grid(row=linha, column=coluna, padx=1, pady=1,ipadx=6,ipady=4)
            #para ser clicavel
            btn_cor.bind("<Button-1>", lambda evento, c=cor: self.mudar_cor_clicada(c))
            #botao pra o colorchooser
            self.btn_rgb = tk.Button(self.grid_cores, text="MAIS CORES", font=("Arial", 10,
             "bold"), bg="#FCE4EC", activebackground="#FCE4EC", fg="#333333", 
            relief="flat", bd=0, highlightthickness=0, 
            command=self.abrir_seletor)        
            self.btn_rgb.grid(row=0, column=14, rowspan=2, padx=10, pady=5, sticky="ns")

    def abrir_seletor(self):
        cor_selecionada = colorchooser.askcolor(title="ESCOLHA A COR PERSONALIZADA")
        if cor_selecionada and cor_selecionada[1]:
            cor_hex = cor_selecionada[1]
            self.mudar_cor_clicada(cor_hex)

    def mudar_cor_clicada(self, cor):
        # verifica qual o modo ativo na paleta
        if self.modo_atual == "traco":
            self.controlador.mudar_traco(cor)
            self.controlador.tracoBoxFrame.config(bg=cor)
            self.caixa_cor.config(bg=cor)

        if self.modo_atual == "preenchimento":                                                                    
            self.controlador.mudar_preenchimento(cor)
            cor_p = self.controlador.cor_preenchimento
            # Atualiza o indicador de baixo
            self.caixa_cor.config(bg=cor_p if cor_p != "" and cor_p != "..." else "white")
            self.caixa_cor.config(bg=cor)
            #atualiza o de cima
            self.controlador.preenchimentoBoxFrame.config(bg=cor)
                                                                                                                                                            
                                                 
                                    
        
                          
