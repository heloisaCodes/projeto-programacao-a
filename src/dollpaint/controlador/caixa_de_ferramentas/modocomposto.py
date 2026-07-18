from modelo.figuras import*
from .ferramentas import ferramenta


class figuracomposta(ferramenta):
    def __init__(self):
       self.figuras=[]
    def ao_clicar(self, event, controladordesenho):
        self.x_inicial = event.x
        self.y_inicial = event.y
        figura_clicada = None
        for f in reversed(controladordesenho.figuras):
                if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                    figura_clicada = f
                    self.figuras.append(f)
    
    def ao_mover(self, event, controladordesenho):
        for f in self.figuras:
            dx = event.x - self.x_inicial
            dy = event.y - self.y_inicial
            f.mover()
                
