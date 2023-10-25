import tkinter as tk 
from tkinter import *
import pandas as pd
import random
import numpy as np
import pprint
import math
'''''
#Inicialmente creamos nuestra ventana principal
ventana=tk.Tk()
ventana.geometry('600x400')
ventana.title('Matriz En Python')

#Creamos el visualizador de nuetsra matriz
visualizador_matriz=LabelFrame(ventana)
visualizador_matriz.place(x=0, y=50)

# Creamos nuestro boton del canal Rojo
boton_2 = tk.Button(text="          R         ",fg='red')
boton_2.place(x=500, y=40)

# Creamos nuestro boton del canal verde
boton_2 = tk.Button(text="          V         ",fg='green')
boton_2.place(x=500, y=100)

# Creamos nuestro boton del canal Azul
boton_2 = tk.Button(text="          B         ",fg='blue')
boton_2.place(x=500, y=160)

# Creamos nuestro boton de filtro
boton_2 = tk.Button(text="       Filtro      ")
boton_2.place(x=500, y=230)

ventana.mainloop()'''


matriz = []
for y in range(8):
    fila=[]
    for x in range(8):
        color=[]
        for _ in range(3):
            numero=random.randint(0,255)
            color.append(numero)
        fila.append(color)
    matriz.append(fila)
print (matriz)

for i in range(8):
    print(matriz[i])
