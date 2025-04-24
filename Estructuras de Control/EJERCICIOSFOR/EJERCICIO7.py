# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:27:36 2022

@author: LUCIA DE ANGULO, JIMENA MINIÑO, PAULA DIZ
"""

capital=input("introduzca un capital: ")
interes=input("introduzca los intereses (entre 0 y 100): ")
M=input("introduzca los años: ")
C=int(capital)
I=int(interes)
for i in M:
    C=C*(1+I/100)
print(C)