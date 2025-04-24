# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 09:18:04 2022

EJERCICIO 3.  DESARROLLAR UN PROGRAMA QUE LEA DESDE TECLADO una FRASE CON DIGITOS, ME SUME DICHOS DIGITOS
QUE APARECEN EN LA FRASE Y ME IMPRIMA EL RESULTADO CON FUNCIONES

@author: LUCIA DE ANGULO, PAULA DIZ, JIMENA MINIÑO
"""

frase=input("introduzca una frase con dígitos: ")
def sumar_digitos(frase):
    suma=0
    for i in frase:
        if i.isdigit():
            suma=suma+int(i)
        else:
            print("Error.  La cadena debía ser solo de dígitos. ")
            
    print("La suma de todos los dígitos es: ",suma)
sumar_digitos(frase)