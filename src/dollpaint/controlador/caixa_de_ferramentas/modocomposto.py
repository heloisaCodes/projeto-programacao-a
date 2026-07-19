from modelo.figuracomposta import figuracomposta
from .ferramentas import ferramenta


class modofiguracomposta(ferramenta):
 
    
    def ao_clicar(self, event, controladordesenho):
        # gardando o primeiro clique
        self.x_inicial = event.x
        self.y_inicial = event.y

        for f in reversed(controladordesenho.figuras):
            # se pertencer 
            if f.pertence(event.x, event.y):
                # para tirar a seleçao
                if f == controladordesenho.figura_ante:
                    controladordesenho.figura_ante = None
                    f.restaurar()
                    controladordesenho.desenhar_figuras()
                    controladordesenho.desenhar_figura_nova()
                    break
                # parte normal 
                controladordesenho.figura_ante = f
                controladordesenho.figura_selecionada = f   
                f.destacar()                                 
                break

    def ao_mover(self, event, controladordesenho):
        if controladordesenho.figura_selecionada is not None:
            # copiei das figuras normais 
            dx = event.x - self.x_inicial   
            dy = event.y - self.y_inicial   
            controladordesenho.figura_selecionada.mover(controladordesenho.canvas, dx, dy)
            self.x_inicial = event.x        
            self.y_inicial = event.y
            controladordesenho.desenhar_figuras()
            controladordesenho.desenhar_figura_nova()

    def ao_soltar(self, event, controladordesenho):
        if controladordesenho.figura_selecionada is not None:
            for f in reversed(controladordesenho.figuras):
                    # vai ignorar a figura que eu ja selecionei
                    if f is controladordesenho.figura_selecionada:
                        continue
                            # verificar se o ponto em que eu soltei era de  alguma figura
                    if  f.pertence(event.x, event.y):
                        
                            # se for uma figura composta , ja tem uma lista entao é so adicionar
                        if  isinstance(f,figuracomposta):
                            f.adicionar(controladordesenho.figura_selecionada)

                                # vai remover da lista normal
                            controladordesenho.figuras.remove(controladordesenho.figura_selecionada)                
                            controladordesenho.figura_selecionada=None
                            controladordesenho.desenhar_figuras()
                            controladordesenho.desenhar_figura_nova()
                            return
                        else:
                                # se for uma figura simples eu apago as duas ja que vao virar so uma
                            nova_figura=figuracomposta(controladordesenho.figura_selecionada,f)
                            nova_figura.restaurar()                          # mudo a cor de volta 
                            controladordesenho.figuras.append(nova_figura)   
                            figuras_apagadas=[f,controladordesenho.figura_selecionada]
                            controladordesenho.figuras=[figura for figura in controladordesenho.figuras if not figura in  figuras_apagadas]
                            controladordesenho.desenhar_figuras()
                            controladordesenho.desenhar_figura_nova()
                           
                            controladordesenho.figura_selecionada=None
                            print("milafre")
                            return
                        
    def finalizar_poligono(self, event, controladordesenho):
        pass
        
        