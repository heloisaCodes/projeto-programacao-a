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
   def destacar(self):
        for figura in self.figuras:
            figura.destacar()

   def restaurar(self):
        for figura in self.figuras:
            figura.restaurar()
       
   def mover(self,canvas,dx,dy):
       for figura in self.figuras:
          figura.mover(canvas,dx,dy)

   # tive que adiconar aqui porque nao tava conseguindo mudar a cor
   def mudar_traco(self, cor):
    for figura in self.figuras:
        if isinstance(figura, figuracomposta):
            figura.mudar_traco(cor)
        else:
            figura._cor_traco_original = cor
            figura.c_traco = cor

   def mudar_preenchimento(self, cor):
     for figura in self.figuras:
        if isinstance(figura, figuracomposta):
            figura.mudar_preenchimento(cor)
        else:
            figura.c_preenchimento = cor
      
    
