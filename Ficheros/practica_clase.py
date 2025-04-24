# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:22:19 2022
PRÁCTICA ARCHIVOS - PAISES.CSV 
PROGRAMACIÓN II
@author: Lucía de Angulo, Paula Diz, Jimena Miniño
"""
import csv
with open('paises.csv', 'r') as file: #esto luego me cerrara el archivo automaticamente
    reader = csv.reader(file, delimiter=";") #delimiter: separa cuando lo encuentra, como strtok en C
    lineas=0
    for fila in reader:
        if lineas == 0:
            print(f'Columnas: {"; ".join(fila)}')
        else:
            print(f'País: {fila[0]} Capital: {fila[1]} ({fila[2]})')
        lineas+=1
    print(f'\nLineas tratadas: {lineas}')
    
import csv  
with open('paises2.csv', 'w',newline='') as file:
    writer = csv.writer(file,delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['Pais', 'Capital','Prefijo'])
    writer.writerow(['Holanda', 'Amsterdam', 31])
    writer.writerow(['Italia', 'Roma', 39])
    print("\nFichero creado: verifica en tu carpeta.")
