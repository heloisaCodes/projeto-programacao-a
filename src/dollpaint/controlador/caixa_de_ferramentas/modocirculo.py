from modelo.circulo import circulo
from .ferramentas import ferramenta
        
class modocirculo(ferramenta):

    def iniciar_figura_nova(self, event, controladordesenho):
        # busco na gaveta de novo
        cor_traco =controladordesenho.cor_traço
        cor_preenchimento = controladordesenho.cor_preenchimento

                # pego os dados fornecidos pelo event e aplico no molde
        controladordesenho.figura_atual=circulo([event.x, event.y, 0], cor_traco, cor_preenchimento)
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()

    def atualizar_figura_nova(self, event, controladordesenho):
        # verificando se a gaveta nao é vazia
        if controladordesenho.figura_atual is not None:
            x_centro = controladordesenho.figura_atual.pontos[0]
            y_centro = controladordesenho.figura_atual.pontos[1]
            raio = ((x_centro - event.x)**2 + (y_centro - event.y)**2) ** 0.5
            # índice [2] com o novo raio calculado
            controladordesenho.figura_atual.pontos[2] = raio
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