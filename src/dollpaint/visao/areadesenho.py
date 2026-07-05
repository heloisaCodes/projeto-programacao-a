import tkinter  as tk

# Area desenho

class AreaDesenho(tk.Frame):
    def __init__(self,master):
        #faltou um parenteses...
        super().__init__(master)

        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)


