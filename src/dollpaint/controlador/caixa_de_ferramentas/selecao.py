from .ferramentas import ferramenta

class modoselecao(ferramenta):
    def __init__(self):
        self.pontos = [0, 0]
        self.retangulo_temp = None # Para desenhar o retângulo de seleção

    def ao_clicar(self, event, controladordesenho):
        # 1. Identifica se clicou em uma figura
        figura_clicada = None
        for f in reversed(controladordesenho.figuras):
            if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                figura_clicada = f
                print("pertence")
                break

        # 2. Verifica CTRL
        ctrl_pressionado = (event.state & 0x0004) != 0

        # 3. Lógica de Seleção
        if not ctrl_pressionado:
            # Seleção Simples: Limpa tudo e seleciona apenas a clicada
            for f in controladordesenho.figuras_selecionadas:
                f.restaurar()
            controladordesenho.figuras_selecionadas = []
            
            if figura_clicada:
                figura_clicada.destacar()
                controladordesenho.figuras_selecionadas.append(figura_clicada)
        else:
            # Seleção Múltipla (com CTRL):
            if figura_clicada:
                if figura_clicada in controladordesenho.figuras_selecionadas:
                    figura_clicada.restaurar()
                    controladordesenho.figuras_selecionadas.remove(figura_clicada)
                else:
                    figura_clicada.destacar()
                    controladordesenho.figuras_selecionadas.append(figura_clicada)

        self.pontos = [event.x, event.y]

    def ao_mover(self, event, controladordesenho):
        # Calcula a diferença do movimento do mouse
        dx = event.x - self.pontos[0]
        dy = event.y - self.pontos[1]
        
        # O movimento acontece se houver algo selecionado, 
        # independentemente de teclas pressionadas
        if controladordesenho.figuras_selecionadas:
            for figura in controladordesenho.figuras_selecionadas:
                if hasattr(figura, 'mover'):
                    figura.mover(controladordesenho.canvas, dx, dy)
        
        # Atualiza o ponto de referência para o próximo cálculo
        self.pontos = [event.x, event.y]
     
    def ao_soltar(self, event, controladordesenho):

        pass

    def copiar(self, controladordesenho):
        self.copia_buffer = [f.clonar() for f in controladordesenho.figuras_selecionadas if hasattr(f, 'clonar')]

    def colar(self, controladordesenho):
        if hasattr(self, 'copia_buffer'):
            for f in self.copia_buffer:
                controladordesenho.figuras.append(f)
                f.desenhar(controladordesenho.canvas)
    
    def finalizar_poligono(self, event, controladordesenho):
        # Como seleção não lida com polígonos, pode deixar vazio
        pass