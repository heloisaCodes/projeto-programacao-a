

# aqui ta guardado todas as ferramentas
# classse mae das ferramentas

from abc import ABC , abstractmethod

# nao precisa mais mais pq o controladordesennho esta sendo passado como paramentro
#from .controladordesenho import controladordesenho
# aqui vamos colocar todas as funçoes que tem is e elif e colocar um pass
# obs; como é uma classe abstrata nao precisa de init

# o que cada classe filha vai precisar obrigatoriamente
class ferramenta(ABC):

    @abstractmethod
    def ao_clicar(self, event,controladordesenho): 
        pass
        
    @ abstractmethod
    def ao_mover(self, event,controladordesenho):
        pass
        
    @abstractmethod
    def ao_soltar(self,event,controladordesenho):
        pass
        
    @abstractmethod
    def finalizar_poligono(self,event,controladordesenho):
        pass

