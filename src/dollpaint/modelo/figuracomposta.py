from .figura import figura

class figuracomposta(figura):
   
   def __init__(self,*args):
     self.figuras=list(args)


   def adicionar(self,figuras):
      self.figuras.append(figuras)



   def desenhar(self, canvas, **kwargs):
       for figura in self.figuras:
          figura.desenhar(canvas,**kwargs)
   def pertence(self, px, py):
        for figura in self.figuras:
            # Se for outra figura composta  continua procurando
            sub_figura = figura.pertence(px, py)
            if sub_figura: 
                return sub_figura  # Retorna a figura clicada dentro da figura
        return None
  
       
   def mover(self,canvas,dx,dy):
       for figura in self.figuras:
          figura.mover(canvas,dx,dy)
           
      
    
