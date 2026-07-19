from .ferramentas import ferramenta
from modelo.poligonoregular import poligonoregular
import math
import time

class modopoligonoregular(ferramenta):

    def __init__(self):
        self.ultimo_clique = 0

    def ao_clicar(self, event, controladordesenho):
        tempo_atual = time.time()
        diferenca_tempo = tempo_atual - self.ultimo_clique
        self.ultimo_clique = tempo_atual

        # se eu clicar duas vezes rapido e se tiver uma figura na gaveta eu faço isso
        if controladordesenho.figura_atual is not None and diferenca_tempo < 0.5:
            self.finalizar_poligono(event, controladordesenho)
            return

        # se nao tiver eu instancio ,parte normal 
        if controladordesenho.figura_atual is None:
            angulo_inicial = math.pi
            controladordesenho.figura_atual = poligonoregular(
                event.x, event.y, 50, 3, angulo_inicial,
                controladordesenho.cor_traço, controladordesenho.cor_preenchimento
            )
            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()
            return

        # o event num garda o numero do button que a gente clicou
        figura = controladordesenho.figura_atual
         #direita
        if event.num == 3:
            figura.lados += 1
        #esquerda
        elif event.num == 1:
            if figura.lados > 3:
                figura.lados -= 1

        figura.pontos = figura._tratamento_pontos()
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()

    def ao_mover(self, event, controladordesenho):
        if controladordesenho.figura_atual is not None:
            x_centro = controladordesenho.figura_atual.x_centro
            y_centro = controladordesenho.figura_atual.y_centro

            raio = ((x_centro - event.x)**2 + (y_centro - event.y)**2) ** 0.5
            controladordesenho.figura_atual.raio = raio

            novo_angulo = math.atan2(event.y - y_centro, event.x - x_centro)
            controladordesenho.figura_atual.angulo_primeiro_vertice = novo_angulo
            controladordesenho.figura_atual.pontos = controladordesenho.figura_atual._tratamento_pontos()

            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()

    def ao_soltar(self, event, controladordesenho):
        pass

    def finalizar_poligono(self, event, controladordesenho):
        # pra nao dar erro se clicar duas vezes rapido e nao tiver nada na gaveta
        if controladordesenho.figura_atual is not None:
            # adiconando  
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            controladordesenho.figura_atual = None
            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()