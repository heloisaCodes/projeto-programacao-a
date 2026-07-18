from modelo.linha import linha
from .ferramentas import ferramenta

class modolinha (ferramenta):
    


    def ao_clicar(self, event, controladordesenho):
       cor_traco = controladordesenho.cor_traço
       cor_preenchimento = controladordesenho.cor_preenchimento
     #guardado dentro da caixinha os dados obtidos com o molde
       controladordesenho.figura_atual= linha([event.x, event.y, event.x, event.y], cor_traco, cor_preenchimento)
       controladordesenho.desenhar_figuras()
       controladordesenho.desenhar_figura_nova()
    # atualizar as figuras     
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
 

