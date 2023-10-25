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

# Se crea una variable titulada como "R" y se designa como lista vacia, es decir =[] para el canal del rojo.
R = []

# La función "range(b)" genera una secuencia de números que va de 0 a b-1.
# Se crea un ciclo for que almacena en la variable "indice" los valores que se tiene al realizar el recorrido por "range(10)".
for matriz in range(8):
   
    # random.randint(a, b). Es una funcion que genera un número aleatorio de un interbalo de numeros.
    # Cada vez que se recorre el ciclo for se agrega un numero aleatorio a la variable titulada como lista.
    R.append(random.randint(0,255))
    
print (R)

# Se crea una variable titulada como "G" y se designa como lista vacia, es decir =[] para el canal del Verde.
G = []

for matriz in range(8):
   
    # random.randint(a, b). Es una funcion que genera un número aleatorio de un interbalo de numeros.
    # Cada vez que se recorre el ciclo for se agrega un numero aleatorio a la variable titulada como lista.
    G.append(random.randint(0,255))
    
print (G)

# Se crea una variable titulada como "B" y se designa como lista vacia, es decir =[] para el canal del Azul.
B = []

for matriz in range(8):
   
    # random.randint(a, b). Es una funcion que genera un número aleatorio de un interbalo de numeros.
    # Cada vez que se recorre el ciclo for se agrega un numero aleatorio a la variable titulada como lista.
    B.append(random.randint(0,255))
    
print (B)

#Creamos una matriz con los datos continidos en mi lista R
matriz = np.array(R)
print (matriz)