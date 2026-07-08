

# aqui ta guardado todas as ferramentas
# classse mae das ferramentas

from abc import ABC , abstractmethod
from modelo.rabisco import rabisco
from modelo.linha import linha
from modelo.oval import oval
from modelo.poligono import poligono
from modelo.retangulo import retangulo
from modelo.circulo import circulo
from canvascontroller import ControladorDesenho
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
        cor_preenchimento = controladordesenho.cor_preenchimento
        # pego os dados fornecidos pelo event e aplico no moldenic
        controladordesenho.figura_atual=rabisco( [event.x, event.y], cor_traco, cor_preenchimento)

        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()

    def atualizar_figura_nova(self, event,controladordesenho):
        # verificando se a gaveta nao é vazia
        if controladordesenho.figura_atual is not None:
            controladordesenho.figura_atual.extend([event.x,event.y])

        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()

    def incluir_figura_nova(self, event,controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()
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
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()

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
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()
    
    def incluir_figura_nova(self, event, controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()
    def finalizar_poligono(self, event, controladordesenho):
        pass
class modoretangulo(ferramenta):

    def iniciar_figura_nova(self, event, controladordesenho):

          # busco na gaveta de novo
        cor_traco =controladordesenho.cor_traço
        cor_preenchimento = controladordesenho.cor_preechimento
                 # pego os dados fornecidos pelo event e aplico no molde
        controladordesenho.figura_atual=retangulo([event.x, event.y, event.x, event.y], cor_traco, cor_preenchimento)
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()
    def atualizar_figura_nova(self, event, controladordesenho):
         if controladordesenho.figura_atual is not None:
             controladordesenho.figura_nova.pontos[2] = event.x
             controladordesenho.figura_atual.pontos[3] = event.y
         ControladorDesenho.desenhar_figuras()
         ControladorDesenho.desenhar_figura_nova()
    
    def incluir_figura_nova(self, event, controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()

class modolinha (ferramenta):
    def iniciar_figura_nova(self, event, controladordesenho):
       cor_traco = controladordesenho.cor_traço
       cor_preenchimento = controladordesenho.cor_preechimento
     #guardado dentro da caixinha os dados obtidos com o molde
       controladordesenho.figura_atual= linha([event.x, event.y, event.x, event.y], cor_traco, cor_preenchimento)
       ControladorDesenho.desenhar_figuras()
       ControladorDesenho.desenhar_figura_nova()
         
    def atualizar_figura_nova(self, event, controladordesenho):
      
        controladordesenho.figura_atual.pontos[2] = event.x
        controladordesenho.figura_atual.pontos[3] = event.y
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()

    def incluir_figura_nova(self, event, controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()
    
    def finalizar_poligono(self, event, controladordesenho):
        pass
    
class modopoligono(ferramenta):
    def iniciar_figura_nova(self, event, controladordesenho):

    # se a gaveta estiver vazia significa que é o primeiro click
       if controladordesenho.figura_atual is None:
        # Criamos o polígono com os dois primeiros pontos (o fixo e o que vai mexer)
        controladordesenho.figura_atual = poligono(
            [event.x, event.y, event.x, event.y], 
            controladordesenho.cor_traço, 
            controladordesenho.cor_preenchimento
            # to acessando diretamente a cor
        )
       else:
        # SE ja tinha pontos na gaveta ou seja se o poligono ja estava em construçao
        # Adicionamos mais um par de X e Y na lista .pontos dele
        controladordesenho.figura_atual.pontos.extend([event.x, event.y])
       ControladorDesenho.desenhar_figuras()
       ControladorDesenho.desenhar_figura_nova()
   
    def atualizar_figura_nova(self, event, controladordesenho):
        # ENQUANTO O MOUSE MEXE (Efeito Elástico):
        if controladordesenho.figura_atual is not None:
            # Modificamos APENAS as duas últimas coordenadas da lista  pelos índices -2 e -1
            # para que a linha  siga a ponta do mouse!
            controladordesenho.figura_atual.pontos[-2] = event.x
            controladordesenho.figura_atual.pontos[-1] = event.y
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()

    def incluir_figura_nova(self, event, controladordesenho):
        pass
    # ta vazio porque o poligono vai ser adicionada por finalizar poligono

    def finalizar_poligono(self, event, controladordesenho):
        # fechar a forma
        if controladordesenho.figura_atual is not None:
            # Se tem pontos suficientes (3 vértices = 6 coordenadas)
            if len(controladordesenho.figura_atual.pontos) >= 6:
                # Remove o último ponto elástico que o duplo clique criou a mais,ele crioi a mais pq antes de ativar o duplo clique o computador entendeu que seria um clique simples
                controladordesenho.figura_atual.pontos = controladordesenho.figura_atual.pontos[:-2]
                # Salva o polígono definitivo no histórico
                controladordesenho.figuras.append(controladordesenho.figura_atual)
            
            # Limpa o armário para começar um polígono novo do zero depois
            controladordesenho.figura_atual = None
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()

class modooval(ferramenta):

    def iniciar_figura_nova(self, event, controladordesenho):
       
       controladordesenho.figura_atual=oval([event.x, event.y, event.x, event.y],
                                             controladordesenho.cor_traço,
                                             controladordesenho.cor_preenchimento)
       ControladorDesenho.desenhar_figuras()
       ControladorDesenho.desenhar_figura_nova()

    def atualizar_figura_nova(self, event, controladordesenho):
        
        if controladordesenho.figura_atual is not None:
         controladordesenho.figura_atual.pontos[2] = event.x
         controladordesenho.figura_atual.pontos[3] = event.y
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()
    def incluir_figura_nova(self, event, controladordesenho):
        # verifcando se tem algo
        if controladordesenho.figura_atual is not None:
            # adicionando na gaveta de figuras
            controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
            controladordesenho.figura_atual=None
        ControladorDesenho.desenhar_figuras()
        ControladorDesenho.desenhar_figura_nova()
    def finalizar_poligono(self, event, controladordesenho):
        pass