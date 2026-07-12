from .figura import figura

class oval(figura):
    def __init__(self, pontos, c_traco, c_preenchimento):
        super().__init__(c_traco, c_preenchimento)
        self.pontos = pontos  

    def desenhar(self, canvas, dash=None):
        canvas.create_oval(
            self.pontos[0], self.pontos[1], 
            self.pontos[2], self.pontos[3], 
            outline=self.c_traco, fill=self.c_preenchimento, dash=dash
        )

    def pertence(self,px,py):
        x1, y1, x2, y2 = self.pontos[0], self.pontos[1], self.pontos[2], self.pontos[3]

        # 1. Calcula o centro da elipse
        h = (x1 + x2) / 2
        k = (y1 + y2) / 2

        # 2. Calcula os semi-eixos (raios horizontal e vertical)
        a = abs(x2 - x1) / 2
        b = abs(y2 - y1) / 2

        if a == 0 or b == 0:
            return False

        # 3. Aplica a equação canônica da elipse: ((x-h)^2 / a^2) + ((y-k)^2 / b^2) <= 1
        resultado = ((px - h) ** 2) / (a ** 2) + ((py - k) ** 2) / (b ** 2)

        return resultado <= 1


    def mover(self,canvas,dx,dy):
        self.pontos[0] += dx  # x1
        self.pontos[1] += dy  # y1
        self.pontos[2] += dx  # x2
        self.pontos[3] += dy  # y2   
        canvas.delete("all")  # Limpa o canvas
        self.desenhar(canvas)                      

        
