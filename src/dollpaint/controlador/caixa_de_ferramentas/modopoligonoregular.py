
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

    # clique direito
def aumentarvertices(self, event, controladordesenho):
        figura = controladordesenho.figura_atual
        if figura is not None:
            figura.lados += 1
            # Recalcula as coordenadas com o novo número de lados
            figura.pontos = figura._tratamento_pontos()
            # Atualiza o desenho 
            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()

def dimnuirvertices(self, event, controladordesenho):
        figura = controladordesenho.figura_atual
        if figura is not None and figura.lados > 3: # minha trava
            figura.lados -= 1
            # 
            figura.pontos = figura._tratamento_pontos()
            # Atualiza o desenho 
            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()

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