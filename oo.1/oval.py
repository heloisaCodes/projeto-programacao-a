from figura import figura

#elif fig == "oval":
            # canvas.create_oval(values[0], values[1], values[2], values[3], outline=c_traço, fill=c_preenchimento)
class oval(figura):
    
    def __init__(self,x1,y1,x2,y2,c_traco,c_preechimento):
        super().__init__(c_traco,c_preechimento)
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def desenhar(self,canvas,dash=None):
        canvas.create_oval(self.x1,
                           self.y1,
                           self.x2,
                           self.y2,
                           outline=self.c_traco,
                           fill=self.c_preenchimento,
                           dash=dash) 