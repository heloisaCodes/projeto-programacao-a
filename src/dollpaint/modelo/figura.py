
#molde
class figura:
    def __init__(self, c_traco, c_preenchimento):
        self.c_traco = c_traco
        self.c_preenchimento = c_preenchimento
    
    def desenhar(self, canvas, dash=None):
        pass

    #recebe os pontos 
    def pertence(self,px,py):
        pass

    #recebe a distancia
    def mover(self,dx,dy):
        pass
