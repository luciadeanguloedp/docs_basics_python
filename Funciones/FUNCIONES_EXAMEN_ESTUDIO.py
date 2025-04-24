# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 00:40:51 2022
PRACTICA EXAMEN - FUNCIONES
@author: lucia
"""

#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
def saludo(nombre):
    cadena = "¡Hola {0}!"
    print(cadena.format(nombre))
    
name = input("Introduzca su nombre: ")
saludo(name)





"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""
def factura(cantidad,IVA):
    if(IVA == 0):
        print("La factura total es: ", cantidad+cantidad*0.21)
    else:
        IVA = float(input("Introduzca el IVA: "))
        IVA = IVA/100
        print("La factura total es: ", cantidad+cantidad*IVA)
        
cant = float(input("Introduzca la cantidad sin IVA: "))
IVA = int(input("Si desea introducir el IVA, pulse 1, si no, pulse 0: "))
factura(cant,IVA)







"""Escribir una función que calcule el área de un círculo y otra que 
calcule el volumen de un cilindro usando la primera función."""
import math
def areaCirculo (radio):
    area = math.pi*radio**2
    return area
def volumenCilindro(radio,altura):
    area = areaCirculo(radio)
    vol = area*altura
    return vol
    
rad = float(input("Introduzca el radio de la base del cilindro: "))
h = float(input("\nIntroduzca la altura del cilindro: "))
print("\nEl volumen del cilindro es: ",volumenCilindro(rad,h))




"""Escribir una función que calcule el máximo común divisor de 
dos números y otra que calcule el mínimo común múltiplo."""
def mcd(num1,num2):
    for i in range(1,num1+1):
        div1 = num1%i
        for j in range(1, num2+1):
            div2 = num2%j
            if (div1 == 0):
                if (div2 == 0):
                    if(i == j):
                        maxdiv = i
        
    return maxdiv
def mcm(num1,num2):
    
    return minmult
n1 = int(input("Introduzca el primer número: "))
n2 = int(input("\nIntroduzca el segundo número: "))
print("El mcd es: ", mcd(n1,n2))
    





















