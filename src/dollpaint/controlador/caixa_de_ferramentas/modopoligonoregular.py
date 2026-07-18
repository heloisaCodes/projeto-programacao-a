
from .ferramentas import ferramenta
from modelo.poligonoregular import poligonoregular
import math
import time

class modopoligonoregular(ferramenta):
     def __init__(self):
        # Inicializa a variável para rastrear o tempo entre os cliques
            self.ultimo_clique = 0
     def ao_clicar(self, event, controladordesenho):
        tempo_atual = time.time()
        diferenca_tempo = tempo_atual - self.ultimo_clique
        self.ultimo_clique = tempo_atual

        if controladordesenho.figura_atual and diferenca_tempo < 0.5:
         figura=controladordesenho.figura_atual
        
         if figura.lados >3:
          figura.lados -= 2
         figura.pontos = figura._tratamento_pontos()
         self.finalizar_poligono( event, controladordesenho)
         return
        # so aceita nessa conversao
        if controladordesenho.figura_atual is None:
           angulo_inicial=math.pi
                 # pego os dados fornecidos pelo event e aplico no molde
                 #        self, centro_x, centro_y, raio, lados, angulo_inicial, c_traco, c_preenchimento
           controladordesenho.figura_atual=poligonoregular(event.x, event.y,50,3,angulo_inicial, controladordesenho.cor_traço,controladordesenho. cor_preenchimento)
           controladordesenho.desenhar_figuras()
           controladordesenho.desenhar_figura_nova()
        else:
        
              figura = controladordesenho.figura_atual
              print("aumentou")
              figura.lados += 1
            # Recalcula as coordenadas com o novo número de lados
              figura.pontos = figura._tratamento_pontos()
            # Atualiza o desenho 
              controladordesenho.desenhar_figuras()
              controladordesenho.desenhar_figura_nova()

    # clique esquerdo
     def diminuirvertices(self, event, controladordesenho):
        figura=controladordesenho.figura_atual
        if controladordesenho.figura_atual is not None:
            figura = controladordesenho.figura_atual
            if figura is not None and figura.lados > 3: # minha trava
                figura.lados -= 1
                # 
                figura.pontos = figura._tratamento_pontos()
                # Atualiza o desenho 
                controladordesenho.desenhar_figuras()
                controladordesenho.desenhar_figura_nova()

    # ao mover o mouse diferente 

        
     def ao_mover(self, event, controladordesenho):
        # verificando se a gaveta nao é vazia
        if controladordesenho.figura_atual is not None:
          # Pega o centro direto da figura que está sendo desenhada
         x_centro = controladordesenho.figura_atual.x_centro
         y_centro = controladordesenho.figura_atual.y_centro
  
         raio = ((x_centro - event.x)**2 + (y_centro - event.y)**2) ** 0.5
        
        # Atualiza o raio no molde
         controladordesenho.figura_atual.raio = raio
         novo_angulo = math.atan2(event.y - y_centro, event.x - x_centro)

         controladordesenho.figura_atual.angulo_primeiro_vertice = novo_angulo
         controladordesenho.figura_atual.pontos = controladordesenho.figura_atual._tratamento_pontos()
        
        # Redesenha na tela
         controladordesenho.desenhar_figuras()
         controladordesenho.desenhar_figura_nova()
    
    # assim como o poligono essa nao é usada
     def ao_soltar(self, event, controladordesenho):
        pass

     def finalizar_poligono(self, event, controladordesenho):
        if controladordesenho.figura_atual is not None:
         controladordesenho.figuras.append(controladordesenho.figura_atual)
            # limpar para o proximo desenho
         controladordesenho.figura_atual=None
         controladordesenho.desenhar_figuras()
         controladordesenho.desenhar_figura_nova()