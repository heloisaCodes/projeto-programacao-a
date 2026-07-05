from modelo.figura import figura

#  if fig == "linha":
#         canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=c_traço)
class linha(figura):

    def __init__(self,pontos,c_traco,c_preenchimento):
        super().__init__(c_traco,c_preenchimento)
        self.pontos=pontos
        
    def desenhar(self,canvas,dash=None):
        canvas.create_line(self.pontos[0],
                           self.pontos[1],
                           self.pontos[2],
                           self.pontos[3],
                           dash=dash,
                           fill=self.c_traco)