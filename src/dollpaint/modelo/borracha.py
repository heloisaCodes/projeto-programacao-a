
class borracha:
    def __init__(self, pontos, cor_traco="white", cor_preenchimento="white"):
        self.pontos = pontos
        self.cor_traco = "white"          
        self.cor_preenchimento = "white"  
       # saco sem fundo
    def desenhar(self, canvas,**kwargs):
        if len(self.pontos) >= 4:
            canvas.create_line(self.pontos, fill=self.cor_traco, width=20, capstyle="round", smooth=True)
            # par deixar a borracha mais bonitinha