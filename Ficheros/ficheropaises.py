# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:07:47 2022

@author: lucia

FICHEROS
"""
import csv
archivo = open("paises.csv", "r")
#print(archivo.read()) #imprime todo el archivo

#readline(numero), para leer un numero de caracteres
caracter = archivo.readline(15)
#print(caracter)

#metodo readlines() que devuelve lista donde cada elemento es una linea del fichero
lineas = archivo.readlines()
print(lineas)

archivo.close()
