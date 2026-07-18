# Tkinter
from tkinter import *

#Imports de Modelo
from modelo.figuras import *
from modelo.borracha import *
from modelo.cores import listadecores

#Import de Visao
from visao.areadesenho import *

# import das ferramentas
# aqui que vamos puxar  as ferramentas para trabalhar
from controlador.caixa_de_ferramentas.caixaprincipal import*

# Outros imports
import pickle #salvar e abrir
import copy #copiar e colar





##### é o nosso contexto, as ferramentas contruidas serão feitas para mudar o estado atual
# configuraçoes da tela de inicializaçao

class controladordesenho:


    def __init__(self, canvas, escolha_atual):
    
        self.canvas = canvas
        self.figura_atual = None  # vai comecar com none pq nao vai inicializar nehuma figura # gaveta temporaria 
        self.figuras = []     # figuras salvas
        self.figuras_selecionadas = []
        # nossa gaveta que vai guardar a escolha do menu, la na visão
        self.escolha_menu=escolha_atual
        # gaveta das cores
        self.cor_traço = "black"          
        self.cor_preenchimento = ""
        self.cores = listadecores
        
        # estado inicial padrão 
        # o paranteses pq ta devolvendo um objeto vivo que sera posso aplicar os metodos
        self.estado_atual = modorabisco() 
        self.estado_anterior= None
        
        # guardar o id da figura que esta selecionada
        # obs: tkinter cria um id automatico para todas as figuras salvas
        self.figura_selecionada = None # nao tem figura selecionada
        self.figura_ante=None
        self.selecao_ativa=False

        self.var_selecao = tk.BooleanVar(value=False)
        
        self.lista_undo = []
        self.lista_redo = []




        
    # o botao selecionar vai chamar essa  
    def selecao(self):
        # cada vez que clicar vai alterar o estado do botao
        self.selecao_ativa=not self.selecao_ativa

        if self.selecao_ativa:
            self.estado_anterior=self.estado_atual
            self.estado_atual=modoselecao()
        else:
            if self.figura_selecionada:
             self.figura_selecionada.restaurar()
             self.figura_selecionada=None
             self.var_selecao.set(False)
            self.desenhar_figuras()
            self.estado_atual=self.estado_anterior
           

    
      
    # parte da logistica da mudança
    # pegando o que o que o menu enviou
    def ao_mudar_selecao(self,opcao):
        # Se tiver uma figura selecionada, limpa o destaque dela antes
        if getattr(self, 'figura_selecionada', None) is not None:
            self.figura_selecionada.restaurar()
            self.figura_selecionada = None

        self.selecao_ativa = False
        # Força o botão de seleção a se desmarcar visualmente na tela
        self.var_selecao.set(False)
        if not self.selecao_ativa : 
            texto = self.escolha_menu.get()
        
            tradutor_ferramentas = {
                "Rabisco": modorabisco,
                "Oval": modooval,
                "Polígono": modopoligono,
                "Linha": modolinha,
                "Círculo": modocirculo,
                "Retângulo": modoretangulo,
                "Borracha": Modoborracha,
                "Poligono Regular": modopoligonoregular
            }

            self.estado_atual = None  # Esvazia a gaveta
            self.estado_atual = tradutor_ferramentas[texto]()
            self.figura_atual=None
                
            self.desenhar_figuras()
            self.desenhar_figura_nova()


            

    #gerenciamento de cliques, deixando o nome mais genérico
    def vincular_eventos(self):

        #desenhar e selecionar
        self.canvas.bind("<Button-1>", self.ao_clicar) #iniciar
        self.canvas.bind("<B1-Motion>", self.ao_mover) #atualizar
        self.canvas.bind("<ButtonRelease-1>", self.ao_soltar) #incluir
       #

        #copiar e colar
        self.canvas.bind("<Control-c>", self.copiar)
        self.canvas.bind("<Control-C>",self.copiar)
        self.canvas.bind("<Control-v>", self.colar)
        self.canvas.bind("<Control-V>",self.colar)

        #eventos para excluir e mover a figura
        self.canvas.bind("<Delete>", self.excluir_figura)
        self.canvas.bind("<Right>", self.mover_frente)
        self.canvas.bind("<Left>", self.mover_tras)
        self.canvas.bind("<Up>", self.mover_topo)
        self.canvas.bind("<Down>", self.mover_fundo)

        #refazer e desfazer
        self.canvas.bind("<Control-y>",self.redo)
        self.canvas.bind("<Control-Y>",self.redo)
        self.canvas.bind("<Control-z>",self.undo)
        self.canvas.bind("<Control-Z>",self.undo)
        #  do poligono regular
        


    def ao_clicar(self, event):
            self.canvas.focus_set() #prioridade em receber atalhos do teclado
            self.lista_undo.append(copy.deepcopy(self.figuras))
            self.lista_redo.clear()
            self.estado_atual.ao_clicar(event,self) 
            self.desenhar_figuras()
            self.desenhar_figura_nova()

            self.pontos = [event.x, event.y]
            


    
    def ao_mover(self, event):
        if self.estado_atual:
            self.estado_atual.ao_mover(event, self)
        
        self.desenhar_figuras()
        if self.figura_atual is not None:
            self.desenhar_figura_nova()



    #adapando para undo e redo    
    def ao_soltar(self, event):
            self.lista_undo.append(copy.deepcopy(self.figuras))
            self.lista_redo.clear()
            self.estado_atual.ao_soltar(event,self)
            self.desenhar_figuras()
            self.desenhar_figura_nova()


        
    
    def finalizar_poligono(self, event):
            self.estado_atual.finalizar_poligono(event,self)
            self.desenhar_figuras()
            self.desenhar_figura_nova()




    def desenhar_figuras(self):
        # Limpa o canvas e redesenha as figuras salvas
        self.canvas.delete("all")
        for fig in self.figuras:
            fig.desenhar(self.canvas)
            



    def desenhar_figura_nova(self):
        # A borracha não tem uma figura_atual, então só desenhamos se não for borracha
        if self.figura_atual is not None and not isinstance(self.estado_atual, Modoborracha):
            self.figura_atual.desenhar(self.canvas, dash=(4, 2))
            


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


    #funcao geral para verificar erros e acertos das funcoes sem print
    def notificacoes(self,mensagem,cor="purple"):

        largura = self.canvas.winfo_width() // 2
        texto_id = self.canvas.create_text(largura, 30, text=mensagem, 
                                            fill=cor,font=("Arial", 10, "bold"))
        self.canvas.after(1500, lambda: self.canvas.delete(texto_id))


    
    def copiar(self, event):
        # Verifica se a seleção está ativa e se há itens na lista
        if self.selecao_ativa and self.figuras_selecionadas:
            # Usa o método copiar da própria ferramenta (modoselecao)
            # ou faz a cópia manual aqui:
            self.area_transferencia = [copy.deepcopy(f) for f in self.figuras_selecionadas]
            self.notificacoes(f"{len(self.area_transferencia)} figura(s) copiada(s)")
        else:
            self.notificacoes("ERRO EM COPIAR: Selecione algo primeiro")



    def colar(self, event):
        if hasattr(self, 'area_transferencia') and self.area_transferencia:
            for figura in self.area_transferencia:
                # Cria a cópia da figura
                nova_figura = copy.deepcopy(figura)
                
                # Move a nova figura um pouco para o lado para não ficar em cima da original
                nova_figura.mover(self.canvas, 20, 20) 
                
                # Adiciona à lista de figuras desenhadas
                self.figuras.append(nova_figura)
                self.desenhar_figuras()
                self.notificacoes("COLADO COM SUCESSO")
        else:
            self.notificacoes("NADA PARA COLAR")

            
    #novas funcionalidades
    #excluir e mover figura
    def excluir_figura(self, event):
        if self.selecao_ativa and self.figuras_selecionadas:
            for figura in self.figuras_selecionadas:
                if figura in self.figuras:
                    self.figuras.remove(figura)
            self.figuras_selecionadas = [] # Limpa a lista após excluir
            self.desenhar_figuras()
            self.notificacoes("FIGURA EXCLUÍDA", cor="red")

    def mover_topo(self, event):
        if self.selecao_ativa and self.figura_selecionada and (self.figura_selecionada in self.figuras):
            self.figuras.remove(self.figura_selecionada)
            self.figuras.append(self.figura_selecionada) # Joga para o fim (desenha por último/topo)
            self.desenhar_figuras()
            self.notificacoes("MOVIDO PARA O TOPO", cor="blue")

    def mover_fundo(self, event):
        if self.selecao_ativa and self.figura_selecionada and (self.figura_selecionada in self.figuras):
            self.figuras.remove(self.figura_selecionada)
            self.figuras.insert(0, self.figura_selecionada) # Joga para o início (desenha primeiro/fundo)
            self.desenhar_figuras()
            self.notificacoes("MOVIDO PARA O FUNDO", cor="blue")

    def mover_frente(self, event):
        if self.selecao_ativa and self.figura_selecionada and (self.figura_selecionada in self.figuras):
            idx = self.figuras.index(self.figura_selecionada)
            if idx < len(self.figuras) - 1: # Verifica se já não é a última
                # Troca de posição com a da frente
                self.figuras[idx], self.figuras[idx+1] = self.figuras[idx+1], self.figuras[idx]
                self.desenhar_figuras()
                self.notificacoes("MOVIDO PARA FRENTE", cor="green")

    def mover_tras(self, event):
        if self.selecao_ativa and self.figura_selecionada and (self.figura_selecionada in self.figuras):
            idx = self.figuras.index(self.figura_selecionada)
            if idx > 0: # Verifica se já não é a primeira
                # Troca de posição com a de trás
                self.figuras[idx], self.figuras[idx-1] = self.figuras[idx-1], self.figuras[idx]
                self.desenhar_figuras()
                self.notificacoes("MOVIDO PARA TRÁS", cor="green")


    #substitutas de selecionar
    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor
        self.lista_undo.append(copy.deepcopy(self.figuras))
        if self.figura_selecionada:
            self.figura_selecionada.c_preenchimento = cor
            
            self.desenhar_figuras() # Limpa o canvas e redesenha com as novas cores

            
    def mudar_traco(self,cor):
        self.cor_traço = cor
        self.lista_undo.append(copy.deepcopy(self.figuras))
        
        if self.figura_selecionada:
            #salva o traco original para nao entrar em conflito com o destacar
            self.figura_selecionada._cor_traco_original = cor
            self.figura_selecionada.c_traco = cor
            
            self.desenhar_figuras() 

    def undo(self):
        if self.lista_undo:
            #copy copia todas as info necessarias
            #salvando a lista que é apagada em desenhar_figuras
            self.lista_redo.append(copy.deepcopy(self.figuras))
            if self.figura_selecionada:
                self.figura_selecionada = None
            #pega o ultimo estado da lista
            self.figuras = self.lista_undo.pop()

            self.desenhar_figuras()

    def redo(self):
        if self.lista_redo:
            self.lista_undo.append(copy.deepcopy(self.figuras))
            self.figuras = self.lista_redo.pop()
            self.desenhar_figuras()                             
