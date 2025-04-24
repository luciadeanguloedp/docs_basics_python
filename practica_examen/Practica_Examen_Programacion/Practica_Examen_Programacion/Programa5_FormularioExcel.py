# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:24:41 2022

Ejercicio 5: Desarrollar una Interfaz de un formulario que me permita cumplimentar lo 
siguiente: (deberás tener librería Pandas, y para abrir excel) 

@author: Lucía de Angulo, Paula Diz, Jimena Miniño
"""

from tkinter import*
import pandas as pd

win = Tk()
win.config(bg='pink')
win.geometry('560x400')
win.title('Guardar datos en Excel')
nombre1,apellido1,edad1,correo1,telf1 = [],[],[],[],[]

def agregardatos():
	global nombre1, apellido1, dni1, correo1, telf1

	nombre1.append(nombre.get())
	apellido1.append(apellido.get())
	edad1.append(edad.get())
	correo1.append(correo.get())
	telf1.append(telf.get())

    #se borran los elementos de la interfaz para poder añadir otros nuevos 
	nombre.delete(0,END)
	apellido.delete(0,END)
	edad.delete(0,END)
	correo.delete(0,END)
	telf.delete(0,END)

def guardardatos():	
	global nombre1,apellido1,edad1,correo1,telf1
	datos = {'Nombres':nombre1,'Apellidos':apellido1, 'Edad':edad1, 'Correo':correo1, 'Telefono':telf1 } 
	nomfich  = str(fich.get() + ".xlsx")	
	df = pd.DataFrame(datos,columns = ['Nombres', 'Apellidos', 'Edad', 'Correo', 'Telefono']) 
	df.to_excel(nomfich)
	fich.delete(0,END)

frame1 = Frame(win, bg='pink')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(win, bg='pink')
frame2.grid(column=1, row=0, sticky='nsew')

nombre = Label(frame1, text ='Nombre', width=10).grid(column=0, row=0, pady=20, padx= 10)
nombre = Entry(frame1,  width=20, font = ('Arial',12))
nombre.grid(column=1, row=0)

apellido = Label(frame1, text ='Apellido', width=10).grid(column=0, row=1, pady=20, padx= 10)
apellido = Entry(frame1, width=20, font = ('Arial',12))
apellido.grid(column=1, row=1)

edad = Label(frame1, text ='Edad', width=10).grid(column=0, row=2, pady=20, padx= 10)
edad = Entry(frame1,  width=20, font = ('Arial',12))
edad.grid(column=1, row=2)

correo = Label(frame1, text ='Correo', width=10).grid(column=0, row=3, pady=20, padx= 10)
correo = Entry(frame1,  width=20, font = ('Arial',12))
correo.grid(column=1, row=3)

telefono = Label(frame1, text ='Telefono', width=10).grid(column=0, row=4, pady=20, padx= 10)
telf = Entry(frame1, width=20, font = ('Arial',12))
telf.grid(column=1, row=4)

agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='pink',bd=5, command =agregardatos)
agregar.grid(columnspan=2, row=5, pady=20, padx= 10)

archivo = Label(frame2, text ='Ingrese Nombre del archivo', width=25, bg='pink',font = ('Arial',12, 'bold'), fg='black')
archivo.grid(column=0, row=0, pady=10, padx= 10)

fich = Entry(frame2, width=23, font = ('Arial',12),highlightbackground = "green", highlightthickness=4)
fich.grid(column=0, row=1, pady=1, padx= 10)

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='pink',bd=5, command =guardardatos)
guardar.grid(column=0, row=2, pady=20, padx= 10)
win.mainloop()








