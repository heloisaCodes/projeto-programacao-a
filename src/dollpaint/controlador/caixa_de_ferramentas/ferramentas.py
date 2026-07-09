

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

    def iniciar_figura_nova(self, event,controladordesenho): 
        pass
    @ abstractmethod

    def atualizar_figura_nova(self, event,controladordesenho):
        pass
    @abstractmethod
    def incluir_figura_nova(self,event,controladordesenho):
        pass
    @abstractmethod
    def finalizar_poligono(self,event,controladordesenho):
        pass

