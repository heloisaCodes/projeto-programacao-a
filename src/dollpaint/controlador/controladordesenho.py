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
        # nossa gaveta que vai guardar a escolha do menu, la na visão
        self.escolha_menu=escolha_atual
        # gaveta das cores
        self.cor_traço = "black"          
        self.cor_preenchimento = ""  
        
        # estado inicial padrão 
        # o paranteses pq ta devolvendo um objeto vivo que sera posso aplicar os metodos
        self.estado_atual = modorabisco() 
        self.estado_anterior= None
        
        # guardar o id da figura que esta selecionada
        # obs: tkinter cria um id auromatico para todas as figuras salvas
        self.figura_selecionada = None # nao tem figura selecionada
        self.selecao_ativa=False
        self.var_selecao = tk.BooleanVar(value=False)




        
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


            

    #gerenciamento de cliques, deixando o nome mais genérico
    def vincular_eventos(self):
        self.canvas.bind("<Button-1>", self.ao_clicar) #iniciar
        self.canvas.bind("<B1-Motion>", self.ao_mover) #atualizar
        self.canvas.bind("<ButtonRelease-1>", self.ao_soltar) #incluir
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)
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
                                                       


    def ao_clicar(self, event):
            self.canvas.focus_set() #prioridade em receber atalhos do teclado
            self.estado_atual.ao_clicar(event,self) 
            self.desenhar_figuras()
            self.desenhar_figura_nova()
            


    
    def ao_mover(self, event):  
            self.estado_atual.ao_mover(event,self)
            self.desenhar_figuras()
            # movi essa trava pra aqui, ja que isso so vai ser uado no modo desenho
            if self.figura_atual is not None:
             self.desenhar_figura_nova()



             
    def ao_soltar(self, event): 
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
        # Desenha a figura da gaveta com linha tracejada        
        if self.figura_atual is not None:
            self.figura_atual.desenhar(self.canvas, dash=(4, 2))




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


    #funcao geral para verificar erros e acertos das funcoes sem print
    def notificacoes(self,mensagem,cor="purple"):

        largura = self.canvas.winfo_width() // 2
        texto_id = self.canvas.create_text(largura, 30, text=mensagem, 
                                            fill=cor,font=("Arial", 10, "bold"))
        self.canvas.after(1500, lambda: self.canvas.delete(texto_id))


    
    def copiar(self, event):
    
        if self.selecao_ativa and self.figura_selecionada:
            #import de copy para copiar a ficha tecnica completa
            #gaveta das figuras copiadas
            self.area_transferencia = copy.deepcopy(self.figura_selecionada)
            self.notificacoes("COPIADO COM SUCESSO")
        else:
            self.notificacoes("ERRO EM COPIAR")



    def colar(self, event):

        if self.area_transferencia:
        
            nova_figura = copy.deepcopy(self.area_transferencia)
            
            mouse_x = event.x
            mouse_y = event.y

            lista_x = [nova_figura.pontos[i] for i in range(len(nova_figura.pontos)) if i % 2 == 0]
            lista_y = [nova_figura.pontos[i] for i in range(len(nova_figura.pontos)) if i % 2 != 0]

            #calculo separado para o circulo
            if nova_figura.__class__.__name__ == 'circulo':
                centro_original_x = nova_figura.pontos[0]
                centro_original_y = nova_figura.pontos[1]

            #calculo normal da media central para as outras figuras
            else:                           
                centro_original_x = sum(lista_x) / len(lista_x)
                centro_original_y = sum(lista_y) / len(lista_y)

            #distancia final da original para nova
            dx = mouse_x - centro_original_x
            dy = mouse_y - centro_original_y
            nova_figura.mover(self.canvas, dx, dy)  

            #para deixar selecionada             
            if self.selecao_ativa:
                if self.figura_selecionada:
                    self.figura_selecionada.restaurar()
                self.figura_selecionada = nova_figura

            #atualizacao da figura
            self.figuras.append(nova_figura)
            self.desenhar_figuras()
            self.notificacoes("COLADO COM SUCESSO")
            
        else:
            self.notificacoes("ERRO EM COLAR")
            

                                            
