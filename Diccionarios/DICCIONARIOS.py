# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:20:54 2022

@author: Lucía de Angulo

DICCIONARIOS, LISTAS Y TUPLAS
"""
diccionario = {"nombre": "Susana", "DNI":"56784938E","edad": "30"}

print(diccionario["DNI"])

#recorrer diccionario
for i in diccionario:
    print(i, ":", diccionario[i], sep=" ")
    
print("\n")
#funcion items
for (k,v) in diccionario.items():
    print(k, ":", v)


#funcion enumerate
print("\n")
for (i,v) in enumerate(diccionario):
    print(i,v)
    
    
#eliminar un par clave-valor
del diccionario['DNI']  #pongo la clave que quiero eliminar
print(diccionario)

#operaciones en diccionarios.  
diccionario['nombre']= 'shoy shusheeete'
diccionario['edad']= 456+1
print(diccionario)

#modificar clave con 'pop'
print("\n")
diccionario['edad']=diccionario.pop('nombre')
#le pongo el valor de nombre a edad y el resto lo elimino
print(diccionario)


#metodo get para obtener valor de una clave
print("\n")
diccionario = {"nombre": "Susana", "DNI":"56784938E","edad": "30"}
print(diccionario.get("edad"))
 #imprimir solo las claves.  values para los valores
for keys in diccionario.keys():
    print(keys)


#funcion zip, iterar sobre dos o mas secuencias al mismo tiempo,los valores pueden emparejarse
print("\n")
Preguntas = [ 'Nombre', 'comida favorita', 'Deporte favorito' ]
Respuestas = [ 'Roman', 'Tortilla', 'Futbool' ]
for p, r in zip(Preguntas, Respuestas):
    print( "Cual es tu {0}? es {1}." .format(p, r))
    
























