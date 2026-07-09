from modelo.rabisco import rabisco
from .ferramentas import ferramenta

class modorabisco(ferramenta):
    # o controlador desenho esta sendo passado como um armario
    def iniciar_figura_nova(self, event,controladordesenho):

        # buscar na gaveta qual é a cor atual
        cor_traco =controladordesenho.cor_traço
        cor_preenchimento = controladordesenho.cor_preenchimento
        # pego os dados fornecidos pelo event e aplico no moldenic
        controladordesenho.figura_atual=rabisco( [event.x, event.y], cor_traco, cor_preenchimento)

        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()

    def atualizar_figura_nova(self, event,controladordesenho):
        # verificando se a gaveta nao é vazia
        if controladordesenho.figura_atual is not None:
            controladordesenho.figura_atual.pontos.extend([event.x, event.y])

            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()
        else:
         return

    def incluir_figura_nova(self, event,controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()
    # nao se aplica
    def finalizar_poligono(self, event):
        pass
