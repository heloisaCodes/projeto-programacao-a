from figura import figura
class circulo(figura):

# elif fig == "circulo":
#         x, y, r = values
#         canvas.create_oval(x-r, y-r, x+r, y+r, dash=(4, 2), outline=c_traço, fill=c_preenchimento)
    def __init__(self,x_centro,y_centro,raio,c_traco,c_preenchimento):
        super().__init__(c_traco,c_preenchimento)
        self.x_centro=x_centro
        self.y_centro=y_centro
        self.raio=raio
    def desenhar(self,canvas,dash=None):
        canvas.create_oval(self.x_centro - self.raio,
                           self.y_centro - self.raio,
                           self.x_centro + self.raio,
                           self.y_centro + self.raio,
                           dash=dash,
                           outline=self.c_traco,
                           fill=self.c_preenchimento)
