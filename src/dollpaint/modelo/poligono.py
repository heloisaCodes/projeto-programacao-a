from .figura import figura

class poligono(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos

    def desenhar(self, canvas, **kwargs):
        canvas.create_polygon(self.pontos, outline=self.c_traco, fill=self.c_preenchimento, **kwargs)

    def imcompleta(self):
        return len(figura.pontos) < 6