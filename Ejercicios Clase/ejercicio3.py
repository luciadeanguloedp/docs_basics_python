# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:58:42 2022

@author: lucia
"""
#EJERCICIO 3
"""Desarrollar un programa donde pida al usuario un
número y verifique si es par o impar y lo imprima"""

num = input("Introduzca un número: ")
num1 = int(num)

if num1%2 == 0:
    print("El número es par")
else:
    print("El número es impar")
