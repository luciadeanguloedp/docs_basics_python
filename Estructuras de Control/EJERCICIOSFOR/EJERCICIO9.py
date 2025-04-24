# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:31:49 2022

Ejercicio 9: Realizar un Programa que solicite el Nombre de un alumno, le 
solicite la cantidad de calificaciones que tiene en su papeleta y que va a 
promediar, el programa calculará el promedio de dichas calificaciones y si el 
promedio es mayor o igual a 70 será Aprobatorio y si es menor 
Reprobatorio, al final preguntará al usuario si desea capturar otro alumno, en 
caso de si, vuelve a ejecutar el programa
 y si dice No, termina el programa.
 usar while, for e if
 
@author: LUCIA DE ANGULO, JIMENA MINIÑO, PAULA DIZ
"""


suma = 0
cont = 0
while(cont == 0):
    nombre = input("Introduzca su nombre: ")
    calif = input("Introduzca la cantidad de calificaciones que tiene en su papeleta: ")
    calificaciones = int(calif)
    
    for i in range(calificaciones):
        x = input("Introduzca su nota: ")
        nota = int(x)
        suma = suma + nota
    
    promedio = suma/calificaciones

    if(promedio>=70):
        print("Aprobado")
    else:
            print("Suspenso")
    
    otro = input("¿Desea evaluar a otro alumno: ")
    
    if(otro == "No"):
        cont = 1
    