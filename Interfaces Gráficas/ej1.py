# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 08:16:34 2022
EJERCICIO 1
@author: lucia
"""
from tkinter import *

root = Tk() #crear rectangulito
ventananueva = Toplevel(root)

def ocultar(ventana):ventana.withdraw()#withdraw esconde la ventana sin destruirla
def ejecutar(f): root.after(200,f)

b1 = Button(root,text="TERMINAR APLICACION", command = root.destroy).pack()  
b2 = Button(ventananueva,text="OCULTAR VENTANA", command=lambda:
            ejecutar(ocultar(ventananueva))).pack()

root.mainloop()

