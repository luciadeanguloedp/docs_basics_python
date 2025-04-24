# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 09:35:47 2022

EJERCICIO 2.  PROGRAMA QUE PIDA UNA FRASE Y ME REGRESE LA PALABRA MAS CORTA DE LA FRASE

@author:  LUCIA DE ANGULO, PAULA DIZ, JIMENA MINIÑO
"""
fras_digitos = input("Introduzca una frase: ")
lista = fras_digitos.split(" ")

long = len(lista)
for i in range(long):
    mas_corta = lista[0];
    if (len(mas_corta)>len(lista[i])):
        mas_corta = lista[i]
        
print(mas_corta)
    