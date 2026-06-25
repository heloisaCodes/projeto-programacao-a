from tkinter import *
from tkinter import ttk
from tkinter import colorchooser 
from figura import figura
from poligono import poligono
from retangulo import retangulo
from circulo import circulo
from oval import oval 
from linha import linha
from rabisco import rabisco


# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get().lower()
    
    if tipo == 'círculo':
        figura_nova = circulo([event.x, event.y, 0], cor_traço, cor_preenchimento)
    elif tipo == 'linha':
        figura_nova=linha([event.x, event.y, event.x, event.y], cor_traço, cor_preenchimento)
    elif tipo == 'retângulo':
        figura_nova=retangulo([event.x, event.y, event.x, event.y], cor_traço, cor_preenchimento)
    elif tipo == 'oval':
        figura_nova = oval([event.x, event.y, event.x, event.y], cor_traço, cor_preenchimento)
    elif tipo =="poligono":
        figura_nova = poligono([event.x, event.y, event.x, event.y], cor_traço, cor_preenchimento)
    else: # rabisco
        figura_nova = rabisco([event.x, event.y], cor_traço, cor_preenchimento)

#        Quando mouse é movido com o botão pressionado

def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:  # Proteção para não quebrar o código
        return
        
    tipo = type(figura_nova).__name__.lower()
        
    # apenas acumula os pontos de arrasto
    if tipo == 'rabisco':
        figura_nova.pontos.extend([event.x, event.y])
            
    # calcula o raio baseado no centro pontos[0] e pontos[1] e salva no pontos[2]
    elif tipo == 'circulo':
        x_centro = figura_nova.pontos[0]
        y_centro = figura_nova.pontos[1]
        raio = ((x_centro - event.x)**2 + (y_centro - event.y)**2) ** 0.5
        figura_nova.pontos[2] = raio
            
    # altera as coordenadas do último ponto inserido
    elif tipo == 'poligono':
        figura_nova.pontos[-2] = event.x
        figura_nova.pontos[-1] = event.y
            
    # 4. Formas de 4 pontos (Oval, Retângulo, Linha): atualiza pontos[2] e pontos[3]
    else:
        figura_nova.pontos[2] = event.x
        figura_nova.pontos[3] = event.y

    desenhar_figuras()
    desenhar_figura_nova()
            

# Quando mouse é solto
def incluir_figura_nova(event): 
    global figura_nova
    if figura_nova is None:  
        return
        
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
        
    figura_nova = None  
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig in figuras:
        fig.desenhar(canvas)
       

def desenhar_figura_nova():
    if figura_nova is not None:
        figura_nova.desenhar(canvas, dash=(4, 2))


def incompleta(figura):
    tipo = type(figura).__name__.lower() # pegar o nome da subclasse
    
    if tipo in ("linha", "retangulo", "oval"):
        return (figura.pontos[0], figura.pontos[1]) == (figura.pontos[2], figura.pontos[3])
        
    elif tipo == "circulo":
        return figura.pontos[2] < 1.0
    
    elif tipo == "poligono":
        return len(figura.pontos) < 6
        
    else: # rabisco
        return len(figura.pontos) <= 2

#                                      Função para selecionar a cor do traço (borda)
def selecionar_cor_traco():
    global cor_traço
    selectedColor = colorchooser.askcolor(title="Cor do Traço")
    if selectedColor[1]: 
        cor_traço = selectedColor[1]
        tracoBoxFrame.config(bg=cor_traço)

#                                    Função para selecionar a cor do preenchimento
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

#                                       Tipo de Figura

label = ttk.Label(frame1, text='Tipo de Figura:')
label.grid(column=0, row=0, sticky=W, **paddings)
#                                                Menu
tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(frame1, tipo_figura_var, 'linha', 'linha', 'rabisco', 'retângulo', 'oval', 'círculo','poligono')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

#                                       Controle da Cor do Traço

tracoButton = Button(frame1, text="Cor do Traço", width=12, command=selecionar_cor_traco)
tracoButton.grid(column=2, row=0, sticky=W, **paddings)
tracoBoxFrame = Frame(frame1, height=25, width=25, relief=SUNKEN, borderwidth=3, bg=cor_traço)
tracoBoxFrame.grid(column=3, row=0, sticky=W, **paddings)

#                                    Controle da Cor de Preenchimento
preenchimentoButton = Button(frame1, text="Preenchimento", width=12, command=selecionar_cor_preenchimento)
preenchimentoButton.grid(column=4, row=0, sticky=W, **paddings)
preenchimentoBoxFrame = Frame(frame1, height=25, width=25, relief=SUNKEN, borderwidth=3, bg="white") # Mostra branco para indicar vazio
preenchimentoBoxFrame.grid(column=5, row=0, sticky=W, **paddings)

#                                           Área de Desenho
frame2 = Frame(root)
frame2.pack()
canvas = Canvas(root, bg='white')
canvas.pack(expand=True,fill=BOTH,padx=20 ,pady=20)
# Ações
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
root.mainloop()