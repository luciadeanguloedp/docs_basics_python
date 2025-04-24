# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 23:07:22 2023
CURSO INTERFACES GRÁFICAS: ventanas con las que interactuamos
con los programas siendo usuarios.

Trabajamos con libreria tkinter.  Puente entre python y la libreria
tcl/tk.

ESTRUCTURA: raíz(ventana), frame (aglutinador de elementos) que 
contiene widgets (casillas, botones, texto, el propio frame...)

RAIZ,FRAME,LABEL,ENTRY,BUTTON, GRID(TABLA)
@author: lucia
"""
from tkinter import*
raiz = Tk()
raiz.title("Ventana de prueba")
#raiz.resizable(0,0) no se puede cambiar la forma, false,false(0,0)
raiz.iconbitmap("playlist.ico") 
#raiz.geometry("650x350") #el tamaño de la raiz siempre se adecuara solo
raiz.config(bg="blue") #bg es background

miFrame = Frame() #construimos el frame
miFrame.pack() #empaquetamos el frame dentro de la raiz pero aun no tiene tamaño
miFrame.config(bg="pink")
miFrame.config(width="1000", height="1000")
miFrame.config(bd=40)

#variablelabel = Label(contenedor,opciones)
cancion = Label(miFrame, text="Cancion")
cancion.grid(row=0,column=0,padx=10,pady=10)

cuadrotextocancion = Entry(miFrame)
cuadrotextocancion.grid(row=0,column=1,padx=10,pady=10) #padx pixeles a izq y dcha de la palabra

autor = Label(miFrame, text="Autor")
autor.grid(row=1,column=0,padx=10,pady=10)

cuadrotextoautor = Entry(miFrame)
cuadrotextoautor.grid(row=1,column=1,padx=10,pady=10)

album = Label(miFrame, text="Album")
album.grid(row=3,column=0,padx=10,pady=10)

cuadrotextoalbum = Entry(miFrame)
cuadrotextoalbum.grid(row=3,column=1,padx=10,pady=10)

raiz.mainloop() #metodo, ventana en bucle infinito siempre lo ultimo

