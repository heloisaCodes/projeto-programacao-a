from .figura import figura

class circulo(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos  

    def desenhar(self, canvas, dash=None):
        x_centro = self.pontos[0]
        y_centro = self.pontos[1]
        raio = self.pontos[2]
        
        canvas.create_oval(
            x_centro - raio,
            y_centro - raio,
            x_centro + raio,
            y_centro + raio,
            outline=self.c_traco,
            fill=self.c_preenchimento,
            dash=dash
        )
