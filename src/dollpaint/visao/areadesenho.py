import tkinter  as tk

# Area desenho
# responsavel por criar o quadro de desenho

class AreaDesenho(tk.Frame):
    def __init__(self,master):
        super().__init__(master,bg="#FCE4EC")

        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)


