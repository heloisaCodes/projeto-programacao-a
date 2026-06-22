from figura import figura

#  if fig == "linha":
#         canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=c_traço)
class linha(figura):

    def __init__(self,x1,y1,x2,y2,c_traco,c_preenchimento):
        super().__init__(c_traco,c_preenchimento)
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def desenhar(self,canvas,dash=None):
        canvas.create_line(self.x1,
                           self.y1,
                           self.x2,
                           self.y2,
                           dash=dash,
                           fill=self.c_traco)