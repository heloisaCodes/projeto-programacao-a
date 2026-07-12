
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
    
    def destacar(self):
        self._cor_traco_original=self.c_traco
        self.c_traco="red"

    def restaurar(self):
        self.c_traco=self._cor_traco_original
