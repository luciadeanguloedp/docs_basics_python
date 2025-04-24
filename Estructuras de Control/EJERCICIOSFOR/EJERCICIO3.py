# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:41:34 2022
Ejercicio 3: Codificar  un programa que solicite al usuario una 
cantidad y luego itere la cantidad de veces dada. En cada iteración, 
solicitar al usuario que ingrese un número. Al finalizar, mostrar la 
suma de todos los números ingresados.
@author: LUCIA DE ANGULO, JIMENA MINIÑO, PAULA DIZ
"""
x = input("Introduzca una cantidad")
num = int(x)
sum =0
for i in range(num):
    y = input("Ingrese otro número")
    num2=int(y)
    sum = sum+num2
    
print("La suma de los números ingresados es de: ", sum)
