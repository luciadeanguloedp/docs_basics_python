# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:06:43 2022
PRACTICA PARA EXAMEN
EJERCICIO 1

Ejercicio 1: Desarrollar un programa que permita crear una lista de palabras y que, a 
continuación, me presente un menú con las siguientes opciones:
1. Contar: Me pide una palabra (cadena), y me dice cuántas veces aparece en la lista
2. Modificar: Me pide una palabra(cadena), y otra cadena a modificar, y modifica todas a
las apariciones de la primera por la segunda en la lista.
3. Eliminar: Me pide una cadena, y la elimina de la lista.
4. Mostrar: Muestra la lista de cadenas
5. Terminar

@author: Lucía de Angulo, Paula Diz, Jimena Miniño
"""
n = int(input("Introduzca cuántas palabras tiene la lista: "))
lista = []

#bucle que rellena la lista
for i in range(n):
    palabra = input(f"Dígame la palabra {i+1}:")
    lista += [palabra]

#menu para que el usuario elija qué desea hacer
op = 0
while(op!=5):
    
    op = int(input("\nINTRODUZCA UNA OPCIÓN\n\t1. CONTAR\n\t2. MODIFICAR\n\t3. ELIMINAR\n\t4. MOSTRAR\n\t5. TERMINAR\n"))
    if(op == 1):
        pal = input("Introduzca una palabra para contar cuántas veces aparece en la lista: ")
        cont = 0
        for i in lista:
            if i == pal:
                cont += 1
        print(f"La palabra \"{pal}\" aparece {cont} veces en la lista")
    elif(op == 2):
        palab = input("¿Qué palabra de la lista desea cambiar?\n");
        change = input("¿Qué palabra desea poner en su lugar?\n");
        for i in range(len(lista)):
            if (lista[i] == palab):
                lista[i]=change
        print(f"La lista nueva es: {lista}")
    elif(op == 3):
        elim = input("¿Qué palabra desea eliminar de la lista?\n")
        for i in range(len(lista)-1,-1,-1):
            if (lista[i]==elim):
                del lista[i]
        print(f"La lista nueva es: {lista}")
    elif(op == 4):
        print(f"La lista creada es: {lista}")
    
    elif(op == 5):
        print("\nSaliendo...")
    
    else:
        print("\nOpción incorrecta...")
    