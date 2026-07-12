from .figura import figura
import math

class rabisco(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos

    def desenhar(self, canvas, dash=None):
        if len(self.pontos) < 4:
            return
        canvas.create_line(self.pontos,
                           fill=self.c_traco,
                           dash=dash)
    def pertence(self,px,py):
        if len(self.pontos) < 4:
            return False

        margem = 5
        num_pontos = len(self.pontos) // 2

        for i in range(num_pontos - 1):
            x1, y1 = self.pontos[i*2], self.pontos[i*2 + 1]
            x2, y2 = self.pontos[(i+1)*2], self.pontos[(i+1)*2 + 1]

            if not (min(x1, x2) - margem <= px <= max(x1, x2) + margem and
                min(y1, y2) - margem <= py <= max(y1, y2) + margem):     
                continue
            
            #reta infinita
            numerador = abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1)
            denominador = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

            if denominador == 0:
                distancia = math.sqrt((px - x1)**2 + (py - y1)**2)
            else:
                distancia = numerador / denominador

            if distancia <= margem:
                return True
                
        return False

    def mover(self,canvas,dx,dy):
        for i in range(len(self.pontos)):
            if i % 2 == 0:
                self.pontos[i] += dx
            else:
                self.pontos[i] += dy
        canvas.delete("all")  # Limpa o canvas
        self.desenhar(canvas)
            
                    
        
