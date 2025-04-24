# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:57:34 2022

Ejercicio 6: Realizar un programa que pida al usuario un 
número de mes (por ejemplo, el 4) y diga cuántos días tiene (por 
ejemplo, 30)  y el nombre del mes. Debes usar listas. Ejemplo: febrero 
(2) tiene 28 días.

@author: Jimena Miniño, Paula Diz, Lucía de Angulo
"""
x = input("Introduzca un número de mes, del 1 al 12: ")
mes = int(x)

#decir cuantos dias tiene y como se llama el  mes

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")


dias = [31,28,31,30,31,30,31,31,30,31,30,31]

print("El mes es ", meses[mes-1], " y tiene ",dias[mes-1], " días")