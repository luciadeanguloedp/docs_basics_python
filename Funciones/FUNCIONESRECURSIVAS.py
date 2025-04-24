# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 08:20:06 2022
FUNCIONES RECURSIVAS
@author: lucia
"""

def jugar(intento=1): 
    respuesta = input("¿De qué color es una naranja? ") 
    if respuesta != "naranja": 
        if intento < 3: 
            print ("\nFallaste! Inténtalo de nuevo") 
            intento += 1 
            jugar(intento) # Llamada recursiva 
        else: 
            print ("\nPerdiste!") 
    else:
        print ("\nGanaste!") 
jugar()


def potencia(n):
    x = input("Introduzca un número: ")
    n = int(x)
    