from .figura import figura

class poligono(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos

    def desenhar(self, canvas, **kwargs):
        if len(self.pontos) < 6:
         return
        return canvas.create_polygon(self.pontos, outline=self.c_traco, fill=self.c_preenchimento, **kwargs)

    def pertence(self,px,py):

        if len(self.pontos) < 6:
            return False

        dentro = False
        num_pontos = len(self.pontos) // 2

        j = num_pontos - 1

        for i in range(num_pontos):
            xi,yi = self.pontos[i*2], self.pontos[i*2 +1]
            xj,yj = self.pontos[j*2], self.pontos[j*2 +1]

            if ((yi > py) != (yj > py)) and (px < (xj - xi) * (py - yi) / (yj - yi + 1e-9) + xi):
                dentro = True
                
            j = i
            
        return dentro

    def mover(self,canvas,dx,dy):
        for i in range(len(self.pontos)):
            if i % 2 == 0:
                self.pontos[i] += dx #eixo x
            else:
                self.pontos[i] += dy #eixo y
        canvas.delete("all")  # Limpa o canvas
        self.desenhar(canvas)
        
