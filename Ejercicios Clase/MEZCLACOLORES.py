# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:25:32 2022

@author: lucia
"""

#ESTE PROGRAMA MEZCLA DOS COLORES

print("\n\nEste programa mezcla dos colores. \n\n", sep= "-")

print("R = Rojo        A = Azul")
primera = input("\nElija uno: ")

if primera == "r":
    print("\n\nA = Azul    V = Verde");
    segunda = input("\nElija otro color:  ")
    if segunda == "a":
        print("\nLa mezcla de ROJO y AZUL es MAGENTA")
    else:
        print("\nLa mezcla ROJO y VERDE produce AMARILLO")
else:
    print("V = Verde     R = Rojo")
    segunda = input("\nElija uno: ")
    if segunda == "v":
        print("\nLa mezcla AZUL y VERDE produce CIAN")
    else:
        print("\nLa mezcla AZUL y ROJO produce MAGENTA")
        
