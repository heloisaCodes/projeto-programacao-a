from caixa_de_ferramentas.ferramentas import ferramenta

# meu pensamento é que essa classe so seja ativada com o bota oboolenao
class selecao(ferramenta):

    # dentro de cada figura vai ter um contem
    def ao_clicar(self, event, controladordesenho):
        self.pontos=[event.x,event.y]
        for f in controladordesenho.figuras:
          if f.conten(event.x,event.y):
            controladordesenho.figura_selecionada=f
            break
          
    def ao_mover(self, event, controladordesenho):
       if controladordesenho.figura_selecionada:
          # so calculo basico ate agora
          dx= event.x - self.event[0]
          dy=event.y - self.event[1]
          controladordesenho.figura_selecionada.mover(dx,dy)

    def ao_soltar(self, event, controladordesenho):
       controladordesenho.figura_selecionada=None
          
             
        


