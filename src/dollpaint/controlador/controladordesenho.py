# Tkinter
from tkinter import *
from tkinter import colorchooser

#Imports de Modelo
from modelo.figuras import *
from modelo.borracha import *

#Import de Visao
from visao.areadesenho import *
# import das ferramentas

# aqui que vamos puxar  as ferramentas para trabalhar
from controlador.caixa_de_ferramentas.caixaprincipal import*
# para salvar e abrir
import pickle


##### é o nosso contexto, as ferramentas contruidas serão feitas para mudar o estado atual
# configuraçoes da tela de inicializaçao

class controladordesenho:
    def __init__(self, canvas, escolha_atual):
        self.canvas = canvas
        self.figura_atual = None  # vai comecar com none pq nao vai inicializar nehuma figura # gaveta temporaria 
        self.figuras = []     # figuras salvas
        # nossa gaveta que vai guardar a escolha do menu, la na visão
        self.escolha_menu=escolha_atual
        # gaveta das cores
        self.cor_traço = "black"          
        self.cor_preenchimento = ""       
        
        # estado inicial padrão 
        # o paranteses pq ta devolvendo um objeto vivo que sera posso aplicar os metodos
        self.estado_atual = modorabisco() 
      
    # parte da logistica da mudança
    # pegando o que o que o menu enviou
    def ao_mudar_selecao(self,opcao):
        texto = self.escolha_menu.get()
    
        tradutor_ferramentas = {
            "rabisco": modorabisco,
            "oval": modooval,
            "poligono": modopoligono,
            "linha": modolinha,
            "círculo": modocirculo,
            "retângulo": modoretangulo,
            "borracha": Modoborracha
        }

        self.estado_atual = None  # Esvazia a gaveta
        self.estado_atual = tradutor_ferramentas[texto]()
            
        self.desenhar_figuras()
        self.desenhar_figura_nova()

    # tudo ok nessa parte
    def vincular_eventos(self):
        self.canvas.bind("<Button-1>", self.iniciar_figura_nova)
        self.canvas.bind("<B1-Motion>", self.atualizar_figura_nova) 
        self.canvas.bind("<Motion>", self.atualizar_figura_nova)
        self.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)

    def iniciar_figura_nova(self, event): 
            self.estado_atual.iniciar_figura_nova(event, self) 
            self.desenhar_figuras()
            self.desenhar_figura_nova()
    
    def atualizar_figura_nova(self, event):  
        if self.figura_atual is not None:
            self.estado_atual.atualizar_figura_nova(event, self)
            self.desenhar_figuras()
            self.desenhar_figura_nova()
        else:
            return
    def incluir_figura_nova(self, event): 
            self.estado_atual.incluir_figura_nova(event, self)
            self.desenhar_figuras()
            self.desenhar_figura_nova()
        
    
    def finalizar_poligono(self, event):
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

    def salvar_arquivo_desenho(self, caminho):
        # Recebe o caminho da visão e salva a lista de figuras usando pickle
        try:
            with open(caminho, 'wb') as arquivo:
                # O pickle pega a lista inteira e transforma em bytes salvando no HD
                pickle.dump(self.figuras, arquivo)
            print("Desenho salvo com sucesso!")
            # importante para a gente ver qual é o erro
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")

    def abrir_arquivo_desenho(self, caminho):
        # recebe de visao ,carrega as figuras e atualiza a tela
        try:
            with open(caminho, 'rb') as arquivo:
                # O pickle lê os bytes do HD e reconstrói os objetos originais
                self.figuras = pickle.load(arquivo)
            
            # Limpa o Canvas para não misturar com o que já estava na tela
            self.canvas.delete("all")
            # controlador redesenhar tudo o que ele acabou de carregar do arquivo
            self.desenhar_figuras()
            print("Desenho carregado com sucesso!")
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")