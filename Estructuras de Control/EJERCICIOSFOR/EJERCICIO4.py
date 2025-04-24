# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:18:00 2022

Ejercicio 4: Solicitar al usuario que ingrese una frase y luego 
imprimir un listado de las vocales que aparecen en esa frase (sin 
repetirlas).

@author: LUCIA DE ANGULO, JIMENA MINIÑO, PAULA DIZ
"""

frase = input("Introduzca una frase:  ")
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
for i in frase:
    if(i =="a" or i =="e" or i =="i" or i =="o" or i =="u" or i =="U" or i =="O" or i =="I" or i =="E" or i =="A" ): #EVALUO SI HAY VOCALES
        if(i=="a" or i=="A"):#HAGO QUE NO SE IMPRIMAN REPETIDAS
            cont1 = cont1 +1
            if (cont1==1):
                print(i)
        if(i=="e" or i=="E"):
            cont2 = cont2 +1
            if (cont2==1):
                print(i)
        if(i=="I" or i=="i"):
            cont3 = cont3 +1
            if (cont3==1):
                print(i)
        if(i=="o" or i=="O"):
            cont4 = cont4 +1
            if (cont4==1):
                print(i)
        if(i=="U" or i=="u"):
            cont5= cont5 +1
            if (cont5==1):
                print(i)