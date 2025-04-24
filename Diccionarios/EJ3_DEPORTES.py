# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:33:54 2022

DICCIONARIOS
EJERCICIO 3 Escribir un programa que implemente una lista de deportes hasta que el usuario no quiera meter mas

@author: lucia
"""




#funcion que me muestra el menu
def menuOpciones(op):
    if(op ==1):
        print("MOSTRAR UN DEPORTE")
    elif(op ==2):
        print("ELIMINAR NUMERO.")
    elif(op==3):
        print("IMPRIMIR DICCIONARIO")
    elif(op==4):
        print("\nSALIR")
    elif(op>4):
        print("\nPor favor, introduzca un numero correcto.")
            
            
deportes = {}

y = 1 #para llenar el diccionario por teclado
while y == 1:
    deporte = input("Introduzca el deporte: ")
    lugar = input("Introduzca el lugar donde se juega: ")
    deportes[deporte]= lugar
    cont = int(input("Si desea introducir más deportes pulse 1, si no pulse cualquier otro número:  "))
    if (cont != 1):
        y = 0
        

            

x=1
deportesElim ={}
while (x==1):
    op =  int(input("\nIntroduzca la opción que desea. \n1. Mostrar deporte.\n2.Eliminar un deporte.\n3. Mostrar todos los deportes.\n4. Salir  "))
    menuOpciones(op)
    
    if(op ==1):
        buscar = input("\nIntroduzca el deporte que desea buscar: ")
        print(buscar, ":", deportes[buscar])
        
    elif(op ==2):
        elim = input("\nIntroduzca el deporte que desea eliminar: ")
        confirm = int(input("\nEstá seguro de querer eliminarlo?  Si es así, escriba 1, si no, escriba 0: "))
        if (confirm==1):
            deportesElim = deportes.copy()  #copia del diccionario
            del deportesElim[elim]
            print(deportesElim)
    elif(op==3):
        print(deportes)
    elif(op==4):
        print("\nFIN")
        x=0


            
            
            
            
            
            
            