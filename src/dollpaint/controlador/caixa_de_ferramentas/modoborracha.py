# é so o rabisco com o fundo branco
from modelo.borracha import borracha
from .ferramentas import ferramenta
# em homenagem a heloisa
class Modoborracha(ferramenta):
   
     def ao_clicar(self, event,controladordesenho):

        # buscar na gaveta qual é a cor atual
        cor_traco ="white"
        cor_preenchimento = "white"
        # pego os dados fornecidos pelo event e aplico no moldenic
        controladordesenho.figura_atual = borracha([event.x, event.y, event.x, event.y])
            # dupliquei patra nao dar erro
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()

     def ao_mover(self, event,controladordesenho):
        # verificando se a gaveta nao é vazia
        if controladordesenho.figura_atual is not None:
            controladordesenho.figura_atual.pontos.extend([event.x, event.y])

            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()
        else:
         return

     def ao_soltar(self, event,controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()
    # nao se aplica
     def finalizar_poligono(self, event,controladordesenho):
        pass
