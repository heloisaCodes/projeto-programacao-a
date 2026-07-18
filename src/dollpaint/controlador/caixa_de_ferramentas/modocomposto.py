from modelo.figuracomposta import figuracomposta
from .ferramentas import ferramenta


class modofiguracomposta(ferramenta):
 
    def ao_clicar(self, event, controladordesenho):
        self.x_inicial = event.x
        self.y_inicial = event.y
          
        for f in reversed(controladordesenho.figuras):
                if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                    # isso serve tanto para uma lista quanto para para um figura normal
                    # isso daqui é pra desmarcar
                    if f == controladordesenho.figura_ante:
                        controladordesenho.figura_ante=None
                        f.restaurar()
                        controladordesenho.desenhar_figuras()
                        controladordesenho.desenhar_figura_nova()

                        print("saiu a cor")
                      
                        break
                    controladordesenho.figura_ante=f
                    controladordesenho.figura_selecionada=f.destacar()

                    print("clicar funcionou")
                    break
        
    # atualizar as figuras, a lista das figuras atualizou ,ok
    def ao_mover(self, event, controladordesenho):
        if controladordesenho.figura_selecionada is not None:
                dx = event.x - self.pontos[0]
                dy = event.y - self.pontos[1]
                controladordesenho.figura_selecionada.mover(controladordesenho.canvas,dx,dy)
                print("chamou")
                controladordesenho.desenhar_figuras()
                controladordesenho.desenhar_figura_nova()
    #adicionar de volta na lista

    def ao_soltar(self, event, controladordesenho):
        if controladordesenho.figura_selecionada is not None:
            for f in reversed(controladordesenho.figuras):
                    if f is controladordesenho.figura_selecionada:
                        continue
                            # verificar se o ponto em que eu soltei era de  alguma figura
                    if hasattr(f, 'pertence') and f.pertence(event.x, event.y):
                        
                            # se for uma figura composta , ja tem uma lista entao é so adicionar
                        if  isinstance(f,figuracomposta):
                            f.adicionar(controladordesenho.figura_clicada)

                                # vai remover da lista normal
                            controladordesenho.figuras.remove(controladordesenho.figura_clicada)                
                            controladordesenho.figura_selecionada=None
                            controladordesenho.desenhar_figuras()
                            controladordesenho.desenhar_figura_nova()
                            return
                        else:
                                # se for uma figura simples eu apago as duas ja que vao virar so uma
                            nova_figura=figuracomposta(controladordesenho.figura_clicada,f)
                            controladordesenho.figuras.append(nova_figura.restaurar())
                            figuras_apagadas=[f,controladordesenho.figura_clicada]
                            controladordesenho.figuras=[figura for figura in controladordesenho.figuras if not figura in  figuras_apagadas]
                            controladordesenho.desenhar_figuras()
                            controladordesenho.desenhar_figura_nova()
                           
                            controladordesenho.figura_selecionada=None
                            print("milafre")
                            return
                        
    def finalizar_poligono(self, event, controladordesenho):
        pass
        
        