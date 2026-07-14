from .ferramentas import ferramenta

class modoselecao(ferramenta):

    def ao_clicar(self, event, controladordesenho):
        
        # Identifica em qual figura o usuário clicou neste momento
        figura_clicada=None
        controladordesenho.figura_clicada = None
        for f in reversed(controladordesenho.figuras):
            if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                figura_clicada = f
                break # Encontrou a figura que está por cima, pode parar a busca

        # coordenada do clique atual 
        self.pontos = [event.x, event.y]
        
        # Se a figura ja estaa selecionada desmarca
        if figura_clicada and controladordesenho.figura_selecionada == figura_clicada:
            if hasattr(controladordesenho.figura_selecionada, 'restaurar'):
                controladordesenho.figura_selecionada.restaurar()
            controladordesenho.figura_selecionada = None
            return # Para aqui, o clique não passa para a seleção novamente

        #  Limpa a seleção antiga antes
        if controladordesenho.figura_selecionada:
            if hasattr(controladordesenho.figura_selecionada, 'restaurar'):
                controladordesenho.figura_selecionada.restaurar()
            controladordesenho.figura_selecionada = None

        #  Se o clique foi em cima de uma figura nova 
        if figura_clicada:
            controladordesenho.figura_selecionada = figura_clicada
            if hasattr(figura_clicada, 'destacar'):
                figura_clicada.destacar()

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