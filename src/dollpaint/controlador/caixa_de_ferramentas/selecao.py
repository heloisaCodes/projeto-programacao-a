from .ferramentas import ferramenta

class modoselecao(ferramenta):
    def __init__(self):
        self.pontos = [0, 0]
        #retangulo temporario de selecao
        self.rettemp = None 
        self.cntrl_pressionado = None

    def ao_clicar(self, event, controladordesenho):
        # 1. Identifica se clicou em uma figura
        figura_clicada = None
        for f in reversed(controladordesenho.figuras):
            if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                figura_clicada = f
                print("pertence")
                break
<<<<<<< HEAD

        # 2. Verifica CTRL
        ctrl_pressionado = (event.state & 0x0004) != 0
=======
                
        #garantindo que o clique comeca  no canvas     
        if figura_clicada is None:
            #salvando os pontos estaticos
            self.x_inicial = event.x 
            self.y_inicial = event.y
            #desenhando um retangulo parecido com o da figura, mas tracejado
            self.rettemp = controladordesenho.canvas.create_rectangle(self.x_inicial,self.y_inicial,
            event.x,event.y,dash=(2, 2), outline="blue")
            
        
        # 2. Verifica CTRL
        self.ctrl_pressionado = (event.state & 0x0004) != 0
>>>>>>> cc44bc329b42a2f2145ed68a779ac6adaa81dc8c

        # 3. Lógica de Seleção
        if not self.ctrl_pressionado:
            # Seleção Simples: Limpa tudo e seleciona apenas a clicada
            for f in controladordesenho.figuras_selecionadas:
                f.restaurar()
            controladordesenho.figuras_selecionadas = []
            
            if figura_clicada:
                figura_clicada.destacar()
                controladordesenho.figuras_selecionadas.append(figura_clicada)
        else:
            # Seleção Múltipla (com CTRL):
            if figura_clicada:
                if figura_clicada in controladordesenho.figuras_selecionadas:
                    figura_clicada.restaurar()
                    controladordesenho.figuras_selecionadas.remove(figura_clicada)
                else:
                    figura_clicada.destacar()
                    controladordesenho.figuras_selecionadas.append(figura_clicada)

        self.pontos = [event.x, event.y]

    def ao_mover(self, event, controladordesenho):
        #primeiro verifica se tem o rettemp
        if self.rettemp:
            #entrega as coordenadas para o rettemp ser atualizado
            #mantem as estaticas e atualiza a nova
            controladordesenho.canvas.coords(self.rettemp, self.x_inicial, self.y_inicial, event.x, event.y)
            self.pontos = [event.x, event.y]
            return #ou break, para nao rodar o restante
            
        # Calcula a diferença do movimento do mouse
        dx = event.x - self.pontos[0]
        dy = event.y - self.pontos[1]
        
        # O movimento acontece se houver algo selecionado, 
        # independentemente de teclas pressionadas
        if controladordesenho.figuras_selecionadas:
            for figura in controladordesenho.figuras_selecionadas:
                if hasattr(figura, 'mover'):
                    figura.mover(controladordesenho.canvas, dx, dy)
        
        # Atualiza o ponto de referência para o próximo cálculo
     
    def ao_soltar(self, event, controladordesenho):
<<<<<<< HEAD

        pass
=======
        if self.rettemp:
            #pergunta se o cntrl ta pressionado pra nao dar conflito
            if not self.ctrl_pressionado:
                controladordesenho.figuras_selecionadas = [] #esvazia selecoes antigas
            for figura in controladordesenho.figuras:
            #verifica todos os pontos  de alguma das figuras esta no retangulo
                if self.x_inicial <= figura.x <= event.x and self.y_inicial <= figura.y <= event.y:
                    figura.destacar()
                    controladordesenho.figuras_selecionadas.append(figura) #add como selecionada se estiver dentro
            controladordesenho.desenhar_figuras()
            controladordesenho.canvas.delete(self.rettemp) #deleta o rettamp para ser recriado a partir daqui
            self.rettemp = None 
                
>>>>>>> cc44bc329b42a2f2145ed68a779ac6adaa81dc8c

    def copiar(self, controladordesenho):
        self.copia_buffer = [f.clonar() for f in controladordesenho.figuras_selecionadas if hasattr(f, 'clonar')]

    def colar(self, controladordesenho):
        if hasattr(self, 'copia_buffer'):
            for f in self.copia_buffer:
                controladordesenho.figuras.append(f)
                f.desenhar(controladordesenho.canvas)
    
    def finalizar_poligono(self, event, controladordesenho):
        # Como seleção não lida com polígonos, pode deixar vazio
        pass
