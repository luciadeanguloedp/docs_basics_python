# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 02:09:38 2022

@author: LUCIA DE ANGULO, JIMENA MINIÑO, PAULA DIZ
"""

#Ejercicio 5: que y cuantas vocales salen en la frase introducida
voc = input("Introduzca una frase: ")
num = 0
print("Las vocales que aparecen son: ")
for i in voc:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        num = num + 1
        print(i)
print("Aparecen ", num, "vocales")