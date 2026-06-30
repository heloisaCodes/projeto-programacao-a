

import tkinter  as tk
from tkinter import ttk

# Area desenho

class areadesenho(tk.frame):
    def __init__(self,master):
        super.__init__(master)

        self.pack(expand=True, fill=tk.BOTH)

        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        

