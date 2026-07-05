# caminho pro python
import sys
import os
import_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if import_path not in sys.path:
    sys.path.append(import_path)

# visao import
from visao.main import *

# mostrar janela
if __name__ == "__main__":
    app = JanelaPrincipal()

    app.mainloop()