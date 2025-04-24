# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:46:56 2022
PRÁCTICA ARCHIVOS - NOMBRES.CSV 
PROGRAMACIÓN II
@author: Lucía de Angulo, Paula Diz, Jimena Miniño
"""
import csv  
with open('nombres.csv', 'w',newline='') as file:
    fieldnames = ['first_name', 'last_name', 'grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
 
    writer.writeheader() #para escribir first name, last name, grade
    writer.writerow({'first_name':'Tania', 'last_name':'Garcia', 'grade':'A'})
    writer.writerow({'first_name':'Antonio', 'last_name':'Carbonero','grade': 'B'})
    writer.writerow({'first_name':'Sergio', 'last_name':'Ramos', 'grade':'C'})
    print("\nFichero creado: verifica en tu carpeta.")

results=[]
with open('nombres.csv') as file:
    reader = csv.DictReader(file) 
    for i in reader:
        results.append(i)
    print(results)
    
    
#ARCHIVOS TXT- crearlo
fichero = open('Frutas.txt', 'w')
lista = ['Manzana', 'Naranja']

for row in lista:
    fichero.write(row + '\n')
fichero.close()