from .ferramentas import ferramenta
from .selecao import *

#para adicionar retangulo temporario

class area_selecao(ferramenta):
    def __init__(self):
        #abreviacao de retangulo temporario
        #inicializa 
        self.rettemp = None
        self.x_inicial = 0
        self.y_inicial = 0

    def ao_clicar(self,event,controladordesenho):
        #salvando os pontos estaticos
        self.x_inicial = event.x
        self.y_inicial = event.y
        #cria o ret
        self.rettemp = controladordesenho.canvas.create_rectangle(self.x_inicial,self.y_inicial,
        event.x,event.y,dash=(2,2),outline="blue")

    def ao_mover(self,event,controladordesenho):
        #verifica se ja tem retangulo
        if self.rettemp:
            #testa se nao foi apagado no delete de desenhar
            try:
                controladordesenho.canvas.delete(self.rettemp)
            except:
                pass
                
            self.rettemp = controladordesenho.canvas.create_rectangle(self.x_inicial, self.y_inicial, 
            event.x, event.y,dash=(2,2), outline="blue")

    def ao_soltar(self,event,controladordesenho):
        if self.rettemp:
            #salva as coords do retangulo
            coords = controladordesenho.canvas.coords(self.rettemp)
            if len(coords) == 4:                              

                #apaga ele visualmente
                controladordesenho.canvas.delete(self.rettemp)

                #verifica se a figura completa esta dentro da area salva
                figuras_detectadas = controladordesenho.canvas.find_enclosed(coords[0], coords[1], coords[2], coords[3])

                if figuras_detectadas:
                    #se tiver figuras, ele pega o objeto atraves do id no dicionario
                    for fig_id in figuras_detectadas:
                        fig_objeto = controladordesenho.figuras_ids.get(int(fig_id))
                        if fig_objeto:
                        #verifica se realmete foi encontrado, e se ele n esta na lista
                            if fig_objeto not in controladordesenho.figuras_selecionadas:
                                fig_objeto.destacar() #se nao estiver, destaca e add na lista
                                controladordesenho.figuras_selecionadas.append(fig_objeto)

                
            self.rettemp = None #de certeza deixa sem rettemp nenhum
            

    def finalizar_poligono(self,event, controladordesenho):
        pass
