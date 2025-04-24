# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:01:39 2022

@author: lucia
"""

#EJERCICIO 4
"""Para tributar un determinado impuesto se 
debe ser mayor de 16 años y tener unos ingresos 
superiores a 1000 € mensuales. Escribir un programa 
que pregunte al usuario su edad y sus ingresos 
mensuales y muestre por pantalla si el usuario tiene que 
tributar o no"""

edad = input("Introduzca su edad: ")
ing = input("Introduzca sus ingresos mensuales: ")
edad1 = int(edad)
ing1 = int(ing)

if edad1 > 16 :
    if ing1 > 1000:
        print("Usted tiene que tributar")
    else:
        print("Usted no tiene que tributar")
else:
    print("Usted no tiene que tributar")
