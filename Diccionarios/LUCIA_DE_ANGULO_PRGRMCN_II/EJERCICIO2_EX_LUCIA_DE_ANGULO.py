# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:47:22 2022

@author: Lucía de Angulo Pelayo

EXAMEN PROGRAMACIÓN II

EJERCICIO 2.  OPCIONES
"""

def NOTAFINAL(): #funcion de la nota final
    print("Introduzca sus tres notas: ")
    nota1 = float(input("Introduzca la nota 1: "))
    nota2 = float(input("Introduzca la nota 2: "))
    nota3 = float(input("Introduzca la nota 3: "))
    notafinal = (nota1 * 0.3)+(nota2*0.25)+(nota3*0.45)
    return notafinal

def ComprobarValidacion(): #funcion contraseña
    contrasena = input("Introduzca la contraseña: ")
    for i in contrasena:
         suma = sum(i.count(c) for c in "0123456789")
    if(len(contrasena)<8):
        print("NO ES SEGURA.  Debe contener al menos 8 caracteres. ")
        ComprobarValidacion() #funcion recursiva, si la contraseña no es segura vuelve a pedirla
    elif(contrasena.islower()==True):
        print("NO ES SEGURA.  Introduzca al menos una mayúscula")
        ComprobarValidacion()
    elif(suma==0):
        print("NO ES SEGURA, introduzca al menos un numero: ")
        ComprobarValidacion()
    else:
        print("Contraseña válida!\n");
        
        
x = 0
while(x!=1):
    op = int(input("Elija una opción: \n1. - Eliges números impares\n 2- Obtén tu nota final\n 3 - Verifica tu contraseña\n 4 - Salir\n"))
    if(op==1):
        lista=[]
        num = int(input("Introduzca un número entero positivo: "))
        for i in range(1, num+1):
            if(i%2!=0):
               lista.append(i)
        print("Los números impares hasta el",num,"son:",lista)
        print("\n")
        
    elif(op==2):
        print("Su nota final es:",NOTAFINAL(), "\n")
      
    elif(op==3):
        ComprobarValidacion()
        
        
    elif(op==4):
        print("SALIENDO...")
        x=1
    else:
        print("Opción incorrecta.  Elija otra...")
    
