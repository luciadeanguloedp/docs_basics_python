# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:39:55 2022
EJERCICIO 1 LISTAS

 Realizar un programa que me guarde n Nombres con su respectivo 
DNI, El usuario debe introducir dichos nombres y DNI de cada persona y 
mostrar el resultado de cada una de las personas.

@author: lucia
"""
x = input("Introduzca el numero de personas de las cuales incluirá los DNIs: ")
num = int(x)

#declaro lista para los nombres y para los dnis
nombres = []
dnis = []

for i in range(num):
    nombre = input("Introduzca el nombre: ")
    nombres.append(nombre)
    
    dni = input("Introduzca el DNI: ")
    dnis.append(dni)

for i,j in zip(nombres,dnis):
    print("El DNI de {0} es {1}.".format(i,j))

