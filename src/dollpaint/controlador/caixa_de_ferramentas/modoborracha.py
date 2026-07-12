from .ferramentas import ferramenta

class Modoborracha(ferramenta):
    def ao_clicar(self, event, controladordesenho):
        self.apagar(event, controladordesenho)

    def ao_mover(self, event, controladordesenho):
        self.apagar(event, controladordesenho)

    def ao_soltar(self, event, controladordesenho):
        pass

    # A implementação deste método é obrigatória porque a classe base 'ferramenta' exige
    def finalizar_poligono(self, event, controladordesenho):
        pass

    def apagar(self, event, controladordesenho):
        # Percorre a lista de figuras e remove as que colidem com o mouse
        for f in controladordesenho.figuras[:]:
            if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                controladordesenho.figuras.remove(f)
        
        # Redesenha a tela SEM a figura removida
        controladordesenho.desenhar_figuras()