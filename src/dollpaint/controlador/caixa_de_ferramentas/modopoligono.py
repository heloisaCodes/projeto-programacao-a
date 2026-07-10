
from modelo.poligono import poligono
from .ferramentas import ferramenta


class modopoligono(ferramenta):

    def ao_clicar(self, event, controladordesenho):

    # se a gaveta estiver vazia significa que é o primeiro click
       if controladordesenho.figura_atual is None:

        controladordesenho.figura_atual = poligono(
            [event.x, event.y, event.x, event.y], 
            controladordesenho.cor_traço, 
            controladordesenho.cor_preenchimento
            # to acessando diretamente a cor
        )
       else:
        # se ja tinha pontos na gaveta ou seja se o poligono ja estava em construçao
        # lembrar que a gaveta das cordenadas é ponto
        controladordesenho.figura_atual.pontos.extend([event.x, event.y])
       controladordesenho.desenhar_figuras()
       controladordesenho.desenhar_figura_nova()
   
    def ao_mover(self, event, controladordesenho):
        if controladordesenho.figura_atual is not None:
            controladordesenho.figura_atual.pontos[-2] = event.x
            controladordesenho.figura_atual.pontos[-1] = event.y
            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()
        else:
            return

    def ao_soltar(self, event, controladordesenho):
        pass
    # ta vazio porque o poligono vai ser adicionada por finalizar poligono

    def finalizar_poligono(self, event, controladordesenho):
        # fechar a forma
        if controladordesenho.figura_atual is not None:
        
            if len(controladordesenho.figura_atual.pontos) >= 6:
                # Remove o último ponto elástico que o duplo clique criou a mais,ele crioi a mais pq antes de ativar o duplo clique o computador entendeu que seria um clique simples
                controladordesenho.figura_atual.pontos = controladordesenho.figura_atual.pontos[:-2]
                # Salva o polígono definitivo no histórico
                controladordesenho.figuras.append(controladordesenho.figura_atual)
            
            # Limpa o armário para começar um polígono novo do zero depois
            controladordesenho.figura_atual = None
        controladordesenho.desenhar_figuras()
        controladordesenho.desenhar_figura_nova()