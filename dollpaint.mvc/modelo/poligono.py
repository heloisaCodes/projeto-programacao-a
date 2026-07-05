from modelo.figura import figura
from controlador.canvascontroller import *

class poligono(figura):
    def __init__(self,pontos,c_traco,c_preenchimento):
        super().__init__(c_traco,c_preenchimento)

        self.pontos=pontos
        self.controlador = ControladorDesenho(canvas=self.area_desenho.canvas, figura_atual='poligono')

    def desenhar(self, canvas, **kwargs):
    # Se kwargs tiver 'dash' (usado para a figura nova em rastro), aplica ele
        canvas.create_polygon(self.pontos, outline=self.c_traco, fill=self.c_preenchimento, **kwargs)

class EstadoPoligono:
    def __init__(self, controlador):
        self.controlador = controlador
        self.figura_nova = None

    def iniciar_figura_nova(self, event):
        if self.figura_nova is None:
            self.figura_nova = poligono([event.x, event.y, event.x, event.y], "#000000", "")
        else:
            self.figura_nova.iniciar_figura_nova(event)
        
        self.controlador.desenhar_figuras()
        if self.figura_nova:
            self.figura_nova.desenhar(self.controlador.canvas, dash=(4, 2))

    def atualizar_figura_nova(self, event):
        if self.figura_nova:
            self.figura_nova.atualizar_figura_nova(event)
            self.controlador.desenhar_figuras()
            self.figura_nova.desenhar(self.controlador.canvas, dash=(4, 2))

    def incluir_figura_nova(self, event):
        pass # Polígono não faz nada ao soltar o clique

    def finalizar_poligono(self, event):
        if self.figura_nova:
            self.figura_nova.finalizar_poligono()
            if not self.controlador.incompleta(self.figura_nova):
                self.controlador.figuras.append(self.figura_nova)
            self.figura_nova = None
            self.controlador.desenhar_figuras()