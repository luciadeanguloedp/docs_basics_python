# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:07:32 2022

@author: lucia
"""
#EJERCICIO 6
"""DETERMINAR RENTA ANUAL DE UNA PERSONA"""

renta = input("Introduzca su renta: ")
renta1 = int(renta)

if renta1<10000:
    renta2 = (renta1*0.05)
elif 10000 < renta1 < 20000:
    renta2 = (renta1*0.15)
elif 20000 < renta1 < 35000:
    renta2= (renta1*0.2)
elif 35000 < renta1 < 60000:
    renta2 = (renta1*0.3)
else:
    renta2 = (renta1*0.45)
    
print("Su renta anual es: ", renta2)
