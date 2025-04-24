# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 09:45:38 2022

EJERCICIO 3.  DESARROLLAR UN PROGRAMA QUE LEA DESDE TECLADO una FRASE CON DIGITOS, ME SUME DICHOS DIGITOS
QUE APARECEN EN LA FRASE Y ME IMPRIMA EL RESULTADO CON FUNCIONES
@author: lucia de angulo pelayo
"""

def sumadigitos(cadena): #funcion que suma los elementos cuando en array ya no hay espacios
    suma = 0
    for i in cadena:
        suma = suma+int(i)
    print("La suma de todos los dígitos es: ",suma)
    
    
frase = input("Introduzca una frase solo de dígitos: ")
#quiero quitarle los espacios, eliminar esas posiciones
cad = frase.split(" ")

cad2  = ''
for i in cad:
    cad2 = cad2+i
 #variable sin los espacios

        
if(cad2.isdigit()==True):
    sumadigitos(cad2)
else:
    while(cad2.isdigit()==False):
        print("Error.  Escriba solamente números. ")
        frase = input("Introduzca una frase solo de dígitos: ")
    
        cad = frase.split(" ")

        cad2  = ''
        for i in cad:
            cad2 = cad2+i
        if(cad2.isdigit()==True):
            sumadigitos(cad2)
        
                