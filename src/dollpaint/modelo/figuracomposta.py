from .figura import figura

class figuracomposta(figura):
    def __init__(self, c_traco, c_preenchimento):
      self.figuras=[]  
      super().__init__(c_traco, c_preenchimento)

    def desenhar(self, canvas, **kwargs):
       for figura in self.figuras:
          figura.desenhar(canvas,**kwargs)

    def pertence(self, px, py):
       for figura in self.figuras:
        if figura.pertece(px,py):
           return True
        return False
    def mover(self,dx,dy):
       for figura in self.figuras:
          figura.mover(dx,dy)
           
      
    
