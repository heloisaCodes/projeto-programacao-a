from .figura import figura

class retangulo(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos

    def desenhar(self, canvas, dash=None):
        return canvas.create_rectangle(self.pontos[0],
                                self.pontos[1],
                                self.pontos[2],
                                self.pontos[3],
                                outline=self.c_traco,
                                fill=self.c_preenchimento,
                                dash=dash)

    def pertence(self,px,py):
        x1, y1 = self.pontos[0], self.pontos[1]
        x2, y2 = self.pontos[2], self.pontos[3]

        dentro_x = min(x1, x2) <= px <= max(x1, x2)
        dentro_y = min(y1, y2) <= py <= max(y1, y2)

        return dentro_x and dentro_y

    def mover(self,canvas,dx,dy):
        self.pontos[0] += dx 
        self.pontos[1] += dy  
        self.pontos[2] += dx  
        self.pontos[3] += dy
        
        canvas.delete("all")  
        self.desenhar(canvas)
