# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:23:57 2022

@author: Lucía de Angulo Pelayo

EXAMEN PROGRAMACIÓN II

EJERCICIO 1.  Cafetería Coffe Matte
"""

print("Bienvenido a Coffe Matte\n")
cafe = int(input("Elija qué café desea:\n1 - NORMAL\n2 - DESCAFEINADO: "))



def azucar(az):  #FUNCION QUE PREGUNTA SI QUIERE AZUCAR
    while(az!= 'SI' and az!='NO'):
        az = input("¿Desea Azucar?  Escriba SI o NO: ")
        return az
    
sugar = '0'
if(cafe == 1):
    leche = int(input("¿Qué leche desea?\n1 - Semidesnatada\n2 - Avena\n3 - Arroz: "))
    if (leche==1):
        lechetipo = "Semidesnatada"
    elif (leche==2):
        lechetipo = "Avena"
    elif (leche==3):
        lechetipo = "Arroz"

    print("Su café es: Normal, con leche (de)",lechetipo,"y", azucar(sugar), "tiene azucar");
    
elif(cafe == 2):
    leche = int(input("¿Qué leche desea?\n1 - Desnatada\n2 - Entera\n3 - Soja: "))
    if (leche==1):
        lechetipo = "Desnatada"
    elif (leche==2):
        lechetipo = "Entera"
    elif (leche==3):
        lechetipo = "Soja"

    print("Su café es: Descafeinado, con leche (de)",lechetipo,"y", azucar(sugar), "tiene azucar");
