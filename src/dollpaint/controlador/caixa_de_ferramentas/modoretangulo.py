from modelo.retangulo import retangulo
from .ferramentas import ferramenta

class modoretangulo(ferramenta):

    def iniciar_figura_nova(self, event, controladordesenho):

          # busco na gaveta de novo
        cor_traco =controladordesenho.cor_traço
        cor_preenchimento = controladordesenho.cor_preenchimento
                 # pego os dados fornecidos pelo event e aplico no molde
        controladordesenho.figura_atual=retangulo([event.x, event.y, event.x, event.y], cor_traco, cor_preenchimento)
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()
    def atualizar_figura_nova(self, event, controladordesenho):
         if controladordesenho.figura_atual is not None:
             controladordesenho.figura_atual.pontos[2] = event.x
             controladordesenho.figura_atual.pontos[3] = event.y
             controladordesenho.desenhar_figuras()
             controladordesenho.desenhar_figura_nova()
         else:
             return
    
    
    def incluir_figura_nova(self, event, controladordesenho):
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
