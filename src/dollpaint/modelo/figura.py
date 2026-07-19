
#molde

class figura:
    def __init__(self, c_traco, c_preenchimento):
        self.c_traco = c_traco
        self.c_preenchimento = c_preenchimento
    
    def desenhar(self, canvas, dash=None):
        pass

    def pertence(self,px,py):
        pass
        
    def mover(self, canvas, dx, dy):
        # Mantenha o canvas como parâmetro se precisar atualizar o desenho na tela
        pass
    
    def destacar(self):
        if not hasattr(self, '_cor_traco_original'):
            self._cor_traco_original = self.c_traco
        self.c_traco = "red"

    def restaurar(self):
        if hasattr(self, '_cor_traco_original'):
            self.c_traco = self._cor_traco_original
            del self._cor_traco_original # Limpa para garantir que o próximo destaque salve a cor correta
          
    def clonar(self):
        return figura(self.c_traco, self.c_preenchimento)
