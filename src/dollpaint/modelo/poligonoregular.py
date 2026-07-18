import math
from .poligono import poligono

class poligonoregular(poligono):
    # o que vai ser usado no controlador
    def __init__(self, centro_x, centro_y, raio, lados, angulo_inicial, c_traco, c_preenchimento):
    
        # A parte responsavel por delimitar
        # primeiro clique
        self.x_centro = centro_x
        self.y_centro = centro_y
        self.raio = raio
        
        self.lados = lados
        # 180 ja que a gente vai começar com um triangulo
        self.angulo_primeiro_vertice = angulo_inicial
        
        # Gera os pontos iniciais baseados na circunferência invisível
        # ele chama a funçao de baixo pra gente  ter os pontos
        # para gerar a primeira lista de pontos que a mother poligono pede
        pontos_iniciais = self._tratamento_pontos()
        super().__init__(pontos_iniciais, c_traco, c_preenchimento)


        # tratamento dos pontos
    def _tratamento_pontos(self):
      # desenhar os desenhos com os limites, foi basicamente copiar os codigos de circulo ,adiconar as contas dos angulos e armazenar
        pontos = []
        # quanto cada lado vai ter de angulos, como se fosse uma pizza
        # a formula basica mesmo
        fatia = (2 * math.pi) / self.lados
        # essa parte é resposavel pela soma de todos os angulos internos
        for i in range(self.lados):
            # o i esta reprensentando a quantidade de lados
            # somar com os angulos que ja estavam 
            angulo_vertice = self.angulo_primeiro_vertice + (i * fatia)
            # aqui ele ta fazendo cada angulos do vertice, e convertendo 
            # a parte reponsavel  pelos lados lateriais
            # tive que ir pesquisar na parte game dev

            # onde vai ficar os vertices,vai ser clique inicial + o raio x o cosseno que é responsavel pelo eixo x
            x = self.x_centro + self.raio * math.cos(angulo_vertice)
            #  ou seja o tamanho do lado de cima para baixo
            y = self.y_centro + self.raio * math.sin(angulo_vertice)
            pontos.extend([x,y])
            
        return pontos

    def desenhar(self, canvas, **kwargs):
        # atualizando os pontos
        self.pontos = self._tratamento_pontos()
        
        # to puxando da classe mae , a funçao desenhar
        super().desenhar(canvas, **kwargs)

    # lembrar que o px é dado no modo
    def pertence(self,px,py):
        dp=(self.x_centro - px,self.y_centro- py)
        # centro do poligono - o raio
        dr=(self.x_centro - self.raio,self.y_centro - self. raio)
        return dp <=dr

    def mover(self,canvas,dx,dy):
        # atualizei o centro
        self.x_centro+=dx
        self.y_centro+=dy

        # atualizar os vertice
        pontos_atuais=[]
        for i in range(0,len(self.pontos),2):
            #pegando cada
         pontos_atuais.extend ( [ self.pontos[i]+dx,
            self.pontos[i+1]+dy])
        self.pontos=pontos_atuais



        canvas.delete("all")  # Limpa o canvas
        self.desenhar(canvas)
     
    def destacar(self):
        if not hasattr(self, '_cor_traco_original'):
            self._cor_traco_original = self.c_traco
        self.c_traco = "red"

    def restaurar(self):
        if hasattr(self, '_cor_traco_original'):
            self.c_traco = self._cor_traco_original
            del self._cor_traco_original # Limpa para garantir que o próximo destaque salve a cor correta

 