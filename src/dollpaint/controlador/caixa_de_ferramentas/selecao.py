from .ferramentas import ferramenta

class modoselecao(ferramenta):

    def ao_clicar(self, event, controladordesenho):
        # 1. Limpa a seleção anterior, se houver
        if controladordesenho.figura_selecionada:
            if hasattr(controladordesenho.figura_selecionada, 'restaurar'):
                controladordesenho.figura_selecionada.restaurar()
            controladordesenho.figura_selecionada = None
              
        self.pontos = [event.x, event.y]
        
        # 2. reversed() garante que você selecione primeiro a figura que está por cima (topo)
        for f in reversed(controladordesenho.figuras):
            # hasattr protege o código para não quebrar com a 'borracha' ou figuras incompletas
            if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                controladordesenho.figura_selecionada = f
                if hasattr(f, 'destacar'):
                    f.destacar()
                break # Achou a figura, para a busca
  
    def ao_mover(self, event, controladordesenho):
        if controladordesenho.figura_selecionada:
            dx = event.x - self.pontos[0]
            dy = event.y - self.pontos[1]
            
            # Verifica se a figura sabe se mover
            if hasattr(controladordesenho.figura_selecionada, 'mover'):
                controladordesenho.figura_selecionada.mover(controladordesenho.canvas, dx, dy)
            
            self.pontos = [event.x, event.y]
     
    def ao_soltar(self, event, controladordesenho):
        pass
        
    def finalizar_poligono(self, event, controladordesenho):
        pass