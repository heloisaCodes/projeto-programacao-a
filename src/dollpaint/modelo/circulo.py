from .figura import figura
import math 

class circulo(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos  

    def desenhar(self, canvas, dash=None):
        x_centro = self.pontos[0]
        y_centro = self.pontos[1]
        raio = self.pontos[2]
        
        return canvas.create_oval(
            x_centro - raio,
            y_centro - raio,
            x_centro + raio,
            y_centro + raio,
            outline=self.c_traco,
            fill=self.c_preenchimento,
            dash=dash
        )
        
    def pertence(self,px,py):
        x_centro = self.pontos[0]
        y_centro = self.pontos[1]
        raio = self.pontos[2]

        #distancia euclidiana = d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        #obs: sqrt = square root (raiz quadrada)
        distancia = math.sqrt((px - x_centro)**2 + (py - y_centro)**2)
        print(distancia <= raio)
        #booleano que da o veredito
        return distancia <= raio

    def mover(self,canvas,dx,dy):
        self.pontos[0] += dx
        self.pontos[1] += dy
        canvas.delete("all")  # Limpa o canvas
        self.desenhar(canvas)
        #atualiza xcentro e ycentro
