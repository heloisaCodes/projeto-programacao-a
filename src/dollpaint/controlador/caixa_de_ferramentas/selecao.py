from .ferramentas import ferramenta

# meu pensamento é que essa classe so seja ativada com o bota oboolenao
class modoselecao(ferramenta):

    # dentro de cada figura vai ter um contem
    def ao_clicar(self, event, controladordesenho):
        if controladordesenho.figura_selecionada:
              controladordesenho.figura_selecionada.restaurar()
        self.pontos=[event.x,event.y]
        for f in controladordesenho.figuras:
          if f.pertence(event.x,event.y):
            controladordesenho.figura_selecionada=f
            f.destacar()
            print('figura adiconada')
            break
  
    def ao_mover(self, event, controladordesenho):
      
        if controladordesenho.figura_selecionada:
            dx = event.x - self.pontos[0]
            dy = event.y - self.pontos[1]
            controladordesenho.figura_selecionada.mover(controladordesenho.canvas, dx, dy)
            self.pontos = [event.x, event.y]
        
            # Atualiza self.pontos com a nova posição do mouse
            # Se não atualizar, a figura vai dar um salto gigante na tela
            self.pontos = [event.x, event.y]
     

    def ao_soltar(self, event, controladordesenho):
       pass
    def finalizar_poligono(self,event,controladordesenho):
        pass
          
             
        


