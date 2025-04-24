# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:39:36 2022

@author: lucia
"""
#EJERCICIO 1
"""Realizar un programa que pida un número positivo
al usuario, después comprobar si es negativo.  Si lo es,
el programa avisa de que no había pedido eso.  Al final, el programa
imprime el valor introducido por el usuario."""

num = input("Escriba un número positivo: ")
x = int(num)
if x < 0:
    print("Número no válido.  Escriba un número positivo")
else:
    print("El número es: ", num)


