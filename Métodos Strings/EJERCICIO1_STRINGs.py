# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 09:10:35 2022

EJERCICIO 1: DESARROLLAR UN PROGRAMA CON UNA FUNCION , ME PEDIRA UNA FRASE
"ESTO ES UN EJEMPLO"
Y ME CAMBIARA EL PRIMER CARACTER DE CADA PALABRA DE MINUSCULA A MAYUSCULA 

USAR SPLIT, UPPER Y UNA FUNCION
@author:  LUCIA DE ANGULO, PAULA DIZ, JIMENA MINIÑO
"""
def mayus(cad):
    lista = cad.split(" ")
    lista2 = []
    for i in lista:
        x = i.capitalize()
        lista2.append(x)
        strA = " ".join(lista2)
    print("\n",strA) 
   
cadena = input("Introduzca una frase en minusculas:" )
mayus(cadena)


    
    

    
