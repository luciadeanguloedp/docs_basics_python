# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:06:45 2022

Ejercicio 2: En un equipo de corredores se quiere guardar el nombre de los corredores que 
entrenan, y los kilómetros que entrenan cada día de la semana.
Se habrá de utilizar dos arreglos:
Nombre_Corredor: Lista para guardar los nombres de los corredores.
kilometros: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que entrena cada 
corredor.
Al finalizar se muestra la lista con los nombres de Corredores y los kilómetros que ha realizado

@author: Lucía de Angulo, Paula Diz, Jimena Miniño
"""
n = int(input("Introduzca cuántos corredores se registrarán: "))
nombres = []

#bucle que rellena la lista
for i in range(n):
    palabra = input(f"Dígame el nombre del corredor {i+1}:")
    nombres += [palabra]
#ahora creamos una tabla con cada dia de la semana y los km corridos de cada corredor
dia = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
kilometros_corridos = [[],[]] #esta es la tabla (matriz)

total_kms =[]
suma=0
for i in range(n):
    for j in range(len(dia)):
        km = int(input(f"\nIntroduzca los kilometros recorridos el {dia[j]} por el corredor {nombres[i]}: "))
        kilometros_corridos[0].append(dia[j])
        kilometros_corridos[1].append(km)
        suma = suma + km;
    total_kms.append(suma)
    suma = 0
        
for i in range(n):
    print(f"Los kilómetros totales recorridos por {nombres[i]} son {total_kms[i]} kms.\n")
