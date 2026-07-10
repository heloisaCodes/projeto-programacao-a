from modelo.oval import oval
from .ferramentas import ferramenta

class modooval(ferramenta):

    def ao_clicar(self, event, controladordesenho):
       
       controladordesenho.figura_atual=oval([event.x, event.y, event.x, event.y],
                                             controladordesenho.cor_traço,
                                             controladordesenho.cor_preenchimento)
       controladordesenho.desenhar_figuras()
       controladordesenho.desenhar_figura_nova()

    def ao_mover(self, event, controladordesenho):
        
        if controladordesenho.figura_atual is not None:
         controladordesenho.figura_atual.pontos[2] = event.x
         controladordesenho.figura_atual.pontos[3] = event.y
         controladordesenho.desenhar_figuras()
         controladordesenho.desenhar_figura_nova()
        else:
            return
    def ao_soltar(self, event, controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()
        
    def finalizar_poligono(self, event, controladordesenho):
        pass