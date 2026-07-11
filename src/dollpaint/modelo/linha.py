from .figura import figura

class linha(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos

    def desenhar(self, canvas, dash=None):
        canvas.create_line(self.pontos[0],
                           self.pontos[1],
                           self.pontos[2],
                           self.pontos[3],
                           dash=dash,
                           fill=self.c_traco)
    def pertence(self,px,py):
        x1,y1 = self.pontos[0],self.pontos[1]
        x2,y2 = self.pontos[2],self.pontos[3]

        #definindo a qntd da margem
        margem = 5

        #definindo a margem
        if not (min(x1, x2) - margem <= x <= max(x1, x2) + margem  and 
        min(y1, y2) - margem  <= y <= max(y1, y2) + margem):
        
            #ja veredita se esta na margem ou nao
            return False

        #distancia do ponto ate a reta caso passe no teste
        numerador = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
        denominador = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

        if denominador == 0:
            return math.sqrt((x - x1)**2 + (y - y1)**2) <= margem
        distancia = numerador / denominador

        #bool para o veredito
        return distancia <= margem
        
    def mover(self,dx,dy):
        self.pontos[0] += dx
        self.pontos[1] += dy
        self.pontos[2] += dx
        self.pontos[3] += dy

    
