
from figura import figura
class retangulo(figura):
    def __init__(self,x1,y1,x2,y2,c_traco,c_preenchimento):
        super().__init__(c_traco,c_preenchimento)
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def desenhar(self,canvas,dash=None):
        canvas.create_retangle(self.x1,
                               self.y1,
                               self.x2,
                               self.y2,
                               outline=self.c_traco,
                               fill=self.c_preenchimento,
                               dash=dash)
        