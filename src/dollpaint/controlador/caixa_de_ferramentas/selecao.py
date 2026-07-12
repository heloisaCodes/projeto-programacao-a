from .ferramentas import ferramenta

# meu pensamento é que essa classe so seja ativada com o bota oboolenao
class modoselecao(ferramenta):

    # dentro de cada figura vai ter um contem
    def ao_clicar(self, event, controladordesenho):
        self.pontos=[event.x,event.y]
        for f in controladordesenho.figuras:
          if f.pertence(event.x,event.y):
            controladordesenho.figura_selecionada=f
            print('figura adiconada')
            break
          
    def ao_mover(self, event, controladordesenho):
       if controladordesenho.figura_selecionada:
          # so calculo basico ate agora
          dx= event.x - self.event[0]
          dy=event.y - self.event[1]
          controladordesenho.figura_selecionada.mover(dx,dy)

    def ao_soltar(self, event, controladordesenho):
       controladordesenho.figura_selecionada=None
    def finalizar_poligono(self,event,controladordesenho):
        pass
          
             
        


