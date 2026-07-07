

# aqui ta guardado todas as ferramentas
# classse mae das ferramentas

from abc import ABC , abstractmethod
from modelo.rabisco import rabisco
from modelo.linha import linha
from modelo.oval import oval
from modelo.poligono import poligono
from modelo.retangulo import retangulo
from modelo.circulo import circulo

# aqui vamos colocar todas as funçoes que tem is e elif e colocar um pass
# obs; como é uma classe abstrata nao precisa de init

# o que cada classe filha vai precisar obrigatoriamente
class ferramenta(ABC):

    @abstractmethod

    def iniciar_figura_nova(self, event,controladordesenho): 
        pass
    @ abstractmethod

    def atualizar_figura_nova(self, event,controladordesenho):
        pass
    @abstractmethod
    def incluir_figura_nova(self,event,controladordesenho):
        pass
    @abstractmethod
    def finalizar_poligono(self,event,controladordesenho):
        pass

class modorabisco(ferramenta):
    # o controlador desenho esta sendo passado como um armario
    def iniciar_figura_nova(self, event,controladordesenho):

        # buscar na gaveta qual é a cor atual
        cor_traco =controladordesenho.cor_traço
        cor_preenchimento = controladordesenho.cor_preechimento
        # pego os dados fornecidos pelo event e aplico no moldenic
        controladordesenho.figura_atual=rabisco( [event.x, event.y], cor_traco, cor_preenchimento)
    
    def atualizar_figura_nova(self, event,controladordesenho):
        # verificando se a gaveta nao é vazia
        if controladordesenho.figura_atual is not None:
            controladordesenho.figura_atual.extend([event.x,event.y])

    def incluir_figura_nova(self, event,controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
    # nao se aplica
    def finalizar_poligono(self, event):
        pass
        
class modocirculo(ferramenta):

    def iniciar_figura_nova(self, event, controladordesenho):
        # busco na gaveta de novo
        cor_traco =controladordesenho.cor_traço
        cor_preenchimento = controladordesenho.cor_preechimento

                # pego os dados fornecidos pelo event e aplico no molde
        controladordesenho.figura_atual=circulo([event.x, event.y, 0], cor_traco, cor_preenchimento)

    def atualizar_figura_nova(self, event, controladordesenho):
        # verificando se a gaveta nao é vazia
        if controladordesenho.figura_atual is not None:
            # Pegamos o centro que foi salvo no clique (índices 0 e 1)
            x_centro = controladordesenho.figura_atual.pontos[0]
            y_centro = controladordesenho.figura_atual.pontos[1]
            # Aplicamos exatamente a fórmula do main antigo
            raio = ((x_centro - event.x)**2 + (y_centro - event.y)**2) ** 0.5
            # índice [2] com o novo raio calculado
            controladordesenho.figura_atual.pontos[2] = raio
    
    def incluir_figura_nova(self, event, controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None

    def finalizar_poligono(self, event, controladordesenho):
        pass
class modoretangulo(ferramenta):

    def iniciar_figura_nova(self, event, controladordesenho):

          # busco na gaveta de novo
        cor_traco =controladordesenho.cor_traço
        cor_preenchimento = controladordesenho.cor_preechimento
                 # pego os dados fornecidos pelo event e aplico no molde
        controladordesenho.figura_atual=retangulo([event.x, event.y, event.x, event.y], cor_traco, cor_preenchimento)
    
    def atualizar_figura_nova(self, event, controladordesenho):
         if controladordesenho.figura_atual is not None:
             controladordesenho.figura_nova.pontos[2] = event.x
             controladordesenho.figura_atual.pontos[3] = event.y
    
    def incluir_figura_nova(self, event, controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None

    
        