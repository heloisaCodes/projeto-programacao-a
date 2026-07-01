from modelo.figura import figura

#     canvas.create_line(values, dash=(4, 2), fill=c_traço)

class rabisco(figura):

    def __init__(self,pontos,c_traco,c_preenchimento):
        super().__init__(c_traco,c_preenchimento)
        self.pontos=pontos
    def desenhar(self,canvas,dash=None):
        canvas.create_line(self.pontos,
                           fill=self.c_traco,
                           dash=dash)