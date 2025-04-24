# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:09:42 2022

Ejercicio 7: Programa que declare tres listas 'lista1', 'lista2' y 'lista3' de 
cinco enteros cada uno, pida valores para 'lista1' y 'lista2' y calcule 
lista3=lista1+lista2

@author: Jimena Miniño, Paula Diz, Lucía de Angulo
"""

lista1=[]
lista2=[]
lista3=[]

print("RELLENAR LISTA 1")
for i in range(5):
    x = input(f"Introduzca el numero de la posición {i+1} de la lista: ")
    num = int(x)
    lista1.append(num)
print(lista1)

print("RELLENAR LISTA 2")

for i in range(5):
    x1 = input(f"Introduzca el numero de la posición {i+1} de la lista: ")
    num1 = int(x1)
    lista2.append(num1)
print(lista2)

lista3 = lista1+lista2

print("LA LISTA 3 ES: ")
print(lista3)