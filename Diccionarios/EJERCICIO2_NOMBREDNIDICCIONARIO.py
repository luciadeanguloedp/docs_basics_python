# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:16:06 2022

DICCIONARIOS
Realizar un programa que me guarde n Nombres con su respectivo 
DNI, El usuario debe introducir dichos nombres y DNI de cada persona y 
mostrar el resultado de cada una de las personas. 

@author: lucia
"""

diccionario = {}

x = input("Introduzca el numero de personas de las cuales incluirá los DNIs: ")
num = int(x)

for i in range(num):
        nombre = input("Introduzca el nombre")
        dni = input("Introduzca el dni")
        diccionario[nombre]= dni
        
print(diccionario)














