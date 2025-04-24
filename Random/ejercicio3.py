# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:28:55 2022

MODULO RANDOM - EJERCICIO 3
Realizar un programa que lea por teclado las 5 notas obtenidas por 
un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las 
notas, la nota media, la nota mas alta que ha sacado y la menor.
@author: Jimena Miniño, Paula Diz, Lucía de Angulo
"""
import random
notas = []
suma = 0

for i in range(5):  #relleno vector con notas aleatorias
    nota=random.randint(0,10)
    notas.append(nota)
    suma = suma + nota
    
print("Las notas son: ", notas)
print("La media es: ", suma/5)

maxima = max(notas)
print("La nota maxima es ", maxima)

minima = min (notas)
print("La nota minima es ", minima)

