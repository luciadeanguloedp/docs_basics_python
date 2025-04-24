# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:24:41 2022

Ejercicio 5: Desarrollar una Interfaz de un formulario que me permita cumplimentar lo 
siguiente: (deberás tener librería Pandas, y para abrir excel) 

@author: lucia
"""

from tkinter import*

def send_data():
    pass

win = Tk()
win.title("FORMULARIO")
name=Label(win,text="Nombre")
name.grid(row=1,column=0)
name.config(padx=10,pady=10)
cuadro_name=Entry(win) #en esta variable guardo el nombre
cuadro_name.grid(row=1,column=1)


surname=Label(win,text="Apellido")
surname.grid(row=2,column=0)
surname.config(padx=10,pady=10)
cuadro_surname=Entry(win) #en esta variable guardo el nombre
cuadro_surname.grid(row=2,column=1)


age=Label(win,text="Edad")
age.grid(row=3,column=0)
age.config(padx=10,pady=10)
cuadro_age=Entry(win) #en esta variable guardo el nombre
cuadro_age.grid(row=3,column=1)

email=Label(win,text="Correo")
email.grid(row=4,column=0)
email.config(padx=10,pady=10)
cuadro_email=Entry(win) #en esta variable guardo el nombre
cuadro_email.grid(row=4,column=1)

num=Label(win,text="Teléfono")
num.grid(row=5,column=0)
num.config(padx=10,pady=10)
cuadro_num=Entry(win) #en esta variable guardo el nombre
cuadro_num.grid(row=5,column=1)

but1=Button(win,text="Agregar", command=send_data, width="30", height="2",bg="#00CD63")
but1.place(x=18,y=200)

win.geometry("500x500")
win.mainloop()






