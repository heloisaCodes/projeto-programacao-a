from figura import figura

class poligono(figura):
    def __init__(self,pontos,c_traco,c_preenchimento):
        super().__init__(c_traco,c_preenchimento)
        self.pontos=pontos
    def desenhar(self, canvas, dash=0):
        canvas.create_polygon(self.pontos,
                              outline=self.c_traco,
                              fill=self.c_preenchimento)