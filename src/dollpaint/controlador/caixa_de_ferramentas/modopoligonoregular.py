
from .ferramentas import ferramenta
from modelo.poligonoregular import poligonoregular
import math

class modopoligonoregular(ferramenta):
    
    def ao_clicar(self, event, controladordesenho):

        # so aceita nessa conversao
        angulo_inicial=math.pi
                 # pego os dados fornecidos pelo event e aplico no molde
                 #        self, centro_x, centro_y, raio, lados, angulo_inicial, c_traco, c_preenchimento
        controladordesenho.figura_atual=poligonoregular(event.x, event.y,50,3,angulo_inicial, controladordesenho.cor_traço,controladordesenho. cor_preenchimento)
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()

    def aumentarvertices(self,event):
        self.vertices+=1
    def dimnuirvertices(self,event):
        self.vertices-=1


    
    def ao_mover(self, event, controladordesenho):
        pass
    def finalizar_poligono(self, event, controladordesenho):
        controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
        controladordesenho.figura_atual=None
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()
    
    def ao_soltar(self, event, controladordesenho):
        pass