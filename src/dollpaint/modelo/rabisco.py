from .figura import figura

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
