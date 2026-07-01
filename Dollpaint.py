from tkinter import *
from tkinter import ttk
from tkinter import colorchooser 

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get().lower()
    
    # Agora guardamos: (tipo, valores, cor_do_traco, cor_de_preenchimento)
    if tipo == 'círculo':
        figura_nova = ("circulo", (event.x, event.y, 0), cor_traço, cor_preenchimento)
    elif tipo in ('linha', 'retângulo', 'oval'):
        figura_nova = (tipo, (event.x, event.y, event.x, event.y), cor_traço, cor_preenchimento)
    else: # rabisco
        figura_nova = ("rabisco", [(event.x, event.y)], cor_traço, cor_preenchimento)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    tipo = figura_nova[0]
    
    if tipo == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif tipo == "circulo":
        x_centro, y_centro = figura_nova[1][0], figura_nova[1][1]
        raio = ((x_centro - event.x)*2 + (y_centro - event.y)*2) * 0.5
        figura_nova = ("circulo", (x_centro, y_centro, raio), figura_nova[2], figura_nova[3])
    else: 
        figura_nova = (tipo, (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])
        
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, c_traço, c_preenchimento in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=c_traço)
        elif fig == "retângulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=c_traço, fill=c_preenchimento)
        elif fig == "oval":
            canvas.create_oval(values[0], values[1], values[2], values[3], outline=c_traço, fill=c_preenchimento)
        elif fig == "circulo":
            x, y, r = values
            canvas.create_oval(x-r, y-r, x+r, y+r, outline=c_traço, fill=c_preenchimento)
        else : # rabisco
            canvas.create_line(values, fill=c_traço)

def desenhar_figura_nova():
    fig, values, c_traço, c_preenchimento = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=c_traço)
    elif fig == "retângulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2), outline=c_traço, fill=c_preenchimento)
    elif fig == "oval":
        canvas.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2), outline=c_traço, fill=c_preenchimento)
    elif fig == "circulo":
        x, y, r = values
        canvas.create_oval(x-r, y-r, x+r, y+r, dash=(4, 2), outline=c_traço, fill=c_preenchimento)
    else : # rabisco
        canvas.create_line(values, dash=(4, 2), fill=c_traço)

def incompleta(figura):
    fig, values, c_traço, c_preenchimento = figura
    if fig in ("linha", "retângulo", "oval"):
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "circulo":
        return values[2] < 1.0 
    else : 
        return len(values) <= 1

# Função para selecionar a cor do traço (borda)
def selecionar_cor_traco():
    global cor_traço
    selectedColor = colorchooser.askcolor(title="Cor do Traço")
    if selectedColor[1]: 
        cor_traço = selectedColor[1]
        tracoBoxFrame.config(bg=cor_traço)

# Função para selecionar a cor do preenchimento
def selecionar_cor_preenchimento():
    global cor_preenchimento
    selectedColor = colorchooser.askcolor(title="Cor de Preenchimento")
    if selectedColor[1]: 
        cor_preenchimento = selectedColor[1]
        preenchimentoBoxFrame.config(bg=cor_preenchimento)


#*** MAIN ***#

figuras = []       
figura_nova = None 

# Definição das cores iniciais padrão
cor_traço = "#000000"          # Preto para as bordas/linhas
cor_preenchimento = ""         # Sem preenchimento inicial

root = Tk()
root.geometry("1920x1920")
root.title("DollDraw")


paddings = {'padx': 5, 'pady': 5} 

frame1 = Frame(root)
frame1.pack(anchor=W)

# Tipo de Figura
label = ttk.Label(frame1, text='Tipo de Figura:')
label.grid(column=0, row=0, sticky=W, **paddings)
tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(frame1, tipo_figura_var, 'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Círculo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Controle da Cor do Traço
tracoButton = Button(frame1, text="Cor do Traço", width=12, command=selecionar_cor_traco)
tracoButton.grid(column=2, row=0, sticky=W, **paddings)
tracoBoxFrame = Frame(frame1, height=25, width=25, relief=SUNKEN, borderwidth=3, bg=cor_traço)
tracoBoxFrame.grid(column=3, row=0, sticky=W, **paddings)

# Controle da Cor de Preenchimento
preenchimentoButton = Button(frame1, text="Preenchimento", width=12, command=selecionar_cor_preenchimento)
preenchimentoButton.grid(column=4, row=0, sticky=W, **paddings)
preenchimentoBoxFrame = Frame(frame1, height=25, width=25, relief=SUNKEN, borderwidth=3, bg="white") # Mostra branco para indicar vazio
preenchimentoBoxFrame.grid(column=5, row=0, sticky=W, **paddings)

# Área de Desenho
frame2 = Frame(root)
frame2.pack()
canvas = Canvas(root, bg='white')
canvas.pack(expand=True,fill=BOTH,padx=20 ,pady=20)
# Ações
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()