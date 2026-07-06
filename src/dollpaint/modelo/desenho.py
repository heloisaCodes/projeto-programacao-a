

# onde vamos guardar as figuras e as configuraçoes padrao


class Desenho:
    def __init__(self):
        self.figuras = []       
        self.figura_nova = None  
        self.cor_traco = "#000000"
        self.cor_preenchimento = ""

    def adicionar_figura(self, figura):
        if not figura.imcompleta():
            self.figuras.append(figura)

    def limpar_figura_nova(self):
        self.figura_nova = None