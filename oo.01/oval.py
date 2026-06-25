from figura import figura


class oval(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos  

    def desenhar(self, canvas, dash=None):
        canvas.create_oval(
            # x               y
            self.pontos[0], self.pontos[1], 
            self.pontos[2], self.pontos[3], 
            outline=self.c_traco, fill=self.c_preenchimento, dash=dash
        )