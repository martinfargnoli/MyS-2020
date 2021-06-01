# Modelos y Simulación - UNNOBA 2021 - Martín Fargnoli
# Proyecto de cursada: Números aleatorios

# ------------------------------------------------------------------------------------------------------------------ #

# Importo "tkinter" que va a ser mi gestor de GUI, "turtle" para dibujar los circulos, y la libreria "random" para usar los números aleatorios de Python.
from tkinter import *
from turtle import *
import random

# Inicializo las variables.
a = int
b = int
attempts = 10
score = 0
answer = int

# ------------------------------------------------------------------------------------------------------------------ #

def juegoTile():

    # Especifico que las variables son globales (aunque no lo sean), de esta forma el Garbage Collector no las borra.
    global contador, aciertos, answer_list, answer_dict

    tile = Tk()
    tile.title('Botonera de memoria')
    tile.geometry("550x500")

    numeros = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

    random.shuffle(numeros)

    my_frame = Frame(tile)
    my_frame.pack(pady=10)

    contador = 0
    aciertos = 0
    answer_list = []
    answer_dict = {}

    # Lógica del juego.
    def button_click(b, number):
        global contador, aciertos, answer_list, answer_dict

        if b["text"] == ' ' and contador < 2:
            b["text"] = numeros[number]
            answer_list.append(number)
            answer_dict[b] = numeros[number]
            contador += 1

        if len(answer_list) == 2:
            if numeros[answer_list[0]] == numeros[answer_list[1]]:
                my_label.config(text="Muy bien!")
                for key in answer_dict:
                    key["state"] = "disabled"
                contador = 0
                aciertos += 1
                answer_list = []
                answer_dict = {}
                if aciertos == 6:
                    my_label.config(text="GANASTE!")
            else:
                my_label.config(text="Intenta de nuevo!")
                contador = 0
                answer_list = []
                for key in answer_dict:
                    key["text"] = " "
                answer_dict = {}

        return

    # Armo el grid para las botoneras.
    b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b0, 0))
    b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b1, 1))
    b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b2, 2))
    b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b3, 3))
    b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b4, 4))
    b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b5, 5))
    b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b6, 6))
    b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b7, 7))
    b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b8, 8))
    b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b9, 9))
    b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b10, 10))
    b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b11, 11))

    b0.grid(row=0, column=0)
    b1.grid(row=0, column=1)
    b2.grid(row=0, column=2)
    b3.grid(row=0, column=3)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=1, column=3)

    b8.grid(row=2, column=0)
    b9.grid(row=2, column=1)
    b10.grid(row=2, column=2)
    b11.grid(row=2, column=3)

    my_label = Label(tile, text="")
    my_label.pack(pady=10)

    salirTile = Button(tile, text="Salir", command=tile.destroy)
    salirTile.pack(pady=10)

    tile.mainloop()

# ------------------------------------------------------------------------------------------------------------------ #

def randomCirculos():

    t1 = Turtle()
    t1.up()
    t1.speed(10)
    colores = ["blue", "red", "green", "yellow", "purple", "orange"]

    while True:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)

        tamaño = random.randint(1, 200)
        color = random.choice(colores)

        t1.goto(x, y)
        t1.down()
        t1.color(color)
        t1.begin_fill()
        t1.circle(tamaño)
        t1.end_fill()
        t1.up()

# ------------------------------------------------------------------------------------------------------------------ #

# Función donde se chequea el ingreso de nombre e intervalo de números.
def check_start():

    global a
    global b
    global answer

    name = str(entry_player.get())

    if not name or name.isspace():
        textstart.set("Error, debe ingresar un nombre!")
        return
    elif name.isdigit():
        textstart.set("Error, debe ingresar un nombre válido!")
        return

    try:
        int(entry_desde.get())
        int(entry_hasta.get())
    except ValueError:
        textstart.set("Error, debe ingresar un número valido!")
        return

    if int(entry_desde.get()) > int (entry_hasta.get()):
        textstart.set("Error, la cota inferior no puede ser más grande que la cota superior!")
        return

    a = int(entry_desde.get())
    b = int(entry_hasta.get())

    answer = random.randint(a, b)

    entry_player.config(state="disabled")
    player.pack_forget()
    desde.pack_forget()
    entry_desde.pack_forget()
    hasta.pack_forget()
    entry_hasta.pack_forget()
    btn_start.pack_forget()
    textoinicio.pack_forget()
    textodiv.pack_forget()
    btn_tile.pack_forget()
    btn_circulos.pack_forget()

    textaux.set("Adivina un número entre " + str(a) + " y " + str(b) + ".")
    label.pack(pady=5)
    entry_window.pack(pady=10)
    btn_check.pack(pady=10)
    guess_attempts.pack(pady=10)
    btn_quit.pack(pady=10)

    adi.geometry("400x270")

    return

# Función donde esta la lógica del juego.
def check_answer():

    global a
    global b
    global attempts
    global score
    global text

    try:
        int(entry_window.get())
    except ValueError:
        text.set("Error, debe ingresar un número valido!")
        return

    name = str(entry_player.get())
    guess = int(entry_window.get())

    if guess < a or guess > b:
        text.set("Error, ingresa un número entre " + str(a) + " y " + str(b) + "!")
        return

    attempts -= 1
    score += 1

    if answer == guess:
        text.set("Felicidades, " + name + "! Has ganado! Tu puntaje es: " + str(score))
        btn_check.pack_forget()
        btn_restart.pack(pady=10)
    elif attempts == 0:
        text.set("Te quedaste sin intentos! :(")
        btn_check.pack_forget()
        btn_restart.pack(pady=10)
    elif guess < answer:
        text.set("Incorrecto! Te quedan " + str(attempts) + " intentos... Intenta con un número más grande!")
    elif guess > answer:
        text.set("Incorrecto! Te quedan " + str(attempts) + " intentos... Intenta con un número más chico!")

    return

# Función para reiniciar el juego.
def restart_game():

    global attempts
    global textstart
    global text
    global score
    global name

    textstart.set("Bienvenid@! Adivine el número!")
    text.set("Tenes 10 intentos, buena suerte!")
    attempts = 10
    score = 0
    name = None

    entry_player.pack_forget()
    textoinicio.pack(pady=15)
    player.pack(pady=5)
    entry_player.pack(pady=5)
    entry_player.config(state="normal")
    entry_player.delete(0, END)
    desde.pack(pady=5)
    entry_desde.pack(pady=5)
    entry_desde.delete(0, END)
    hasta.pack(pady=5)
    entry_hasta.pack(pady=5)
    entry_hasta.delete(0, END)
    btn_start.pack(pady=5)
    textodiv.pack(pady=15)
    btn_tile.pack(pady=10)
    btn_circulos.pack(pady=10)

    label.pack_forget()
    entry_window.pack_forget()
    btn_check.pack_forget()
    guess_attempts.pack_forget()
    btn_quit.pack_forget()
    btn_restart.pack_forget()

    adi.geometry("400x450")

    return

# ------------------------------------------------------------------------------------------------------------------ #

# Inicializo la ventana.
adi = Tk()
adi.title("MyS - UNNOBA 2021")
adi.geometry("400x450")
textstart = StringVar()
textstart.set("Bienvenid@! Adivine el número!")
textoinicio = Label(adi, textvariable=textstart)
textoinicio.pack(pady=15)

# Ingreso el nombre del jugador.
player = Label(adi, text="Ingrese su nombre")
player.pack(pady=5)
entry_player = Entry(adi, width=30, borderwidth=4)
entry_player.pack(pady=5)

# Ingreso el intervalo de números.
desde = Label(adi, text="Ingrese el limite inferior")
desde.pack()
entry_desde = Entry(adi, width=30, borderwidth=4)
entry_desde.pack(pady=5)
hasta = Label(adi, text="Ingrese el limite superior")
hasta.pack()
entry_hasta = Entry(adi, width=30, borderwidth=4)
entry_hasta.pack(pady=5)

# Boton para asignar el nombre del jugador y el intervalo de números.
btn_start = Button(adi, text="Siguiente", command=check_start)
btn_start.pack(pady=10)

# Pongo un prompt (con su respectivo texto) para ingresar un número.
textaux = StringVar()
textaux.set(" ")
label = Label(adi, textvariable=textaux)
# label.pack()
entry_window = Entry(adi, width=50, borderwidth=4)
# entry_window.pack(pady=10)

# Boton para enviar el número a adivinar.
btn_check = Button(adi, text="Adivinar", command=check_answer)
# btn_check.pack(pady=10)

# Boton para salir.
btn_quit = Button(adi, text="Salir", command=adi.destroy)
# btn_quit.pack(pady=10)

# Boton para reiniciar.
btn_restart = Button(adi, text="Reiniciar", command=restart_game)
# btn_restart.pack(pady=10)

# Texto que muestra la cantidad de intentos.
text = StringVar()
text.set("Tenes " + str(attempts) + " intentos, buena suerte!")
guess_attempts = Label(adi, textvariable=text)
# guess_attempts.pack(pady=10)

# ------------------------------------------------------------------------------------------------------------------ #

textodiv = Label(adi, text="----- Otras cositas -----")
textodiv.pack(pady=15)

btn_tile = Button(adi, text="Botonera de memoria", command=juegoTile)
btn_tile.pack(pady=10)

btn_circulos = Button(adi, text="Circulos aleatorios", command=randomCirculos)
btn_circulos.pack(pady=10)

# Ejecuto en la ventana "adi".
adi.mainloop()
