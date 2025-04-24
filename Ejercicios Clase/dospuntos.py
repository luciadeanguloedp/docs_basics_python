# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:13:30 2022

@author: lucia
"""
#LOS DOS PUNTOS EN PHYTON 



"""
#SEGMENTACION DE LISTAS.  Para recuperar un elemento en particular.
a = [5,-9,8,33,4,64] #*creamos lista
print(a[:])#recupera la lista de la lista

#recupera elementos del tercer indice
print(a[2:3])
#RECUPERA ELEMENTOS POR ENCIMA DEL QUINTO HASTA EL ULTIMO INDICE
print(a[4:])

#recupera elemetnos `pr encima del segundo indice
print(a[1:])
"""





"""
#segmentacion de cadenas
ss = "Sammy shark!"
print(ss[:]) #imprime toda la cadena
print(ss[4]) #imprime cuarto elemento de la cadena

#con indice negativo: cadena larga, para localizar elemento al final
print(ss[-1]) #todo lo restante se puede hacer con los indices negativos
#imrpime desde el elemento 6 hasta el 10(11 no se incluye)
print(ss[6:11])


print(ss[:5]) #imprime de la 0 a la 4

print(ss[7:]) #imprime desde la 7 hasta el final

print(ss[-4:-1]) #imp desde la -2 a la -4 incluida

print(ss[6:11:1]) #de la 6 a la 10 de 1 en 1

print(ss[::4]) # desde el inicio y de 4 en 4
print(ss[::-1]) #lo escribe al reves

"""



"""
#BUCLE FOR
for i in range(0,5):
    print(i)
    
nums = [4,78,9,84] #imprime la lista
for n in nums:
    print(n)
    
for i in "Python": #imprime cada letra
    print(i)
"""



"""
#ITERABLES - IDENTIFICARLOS

from collections import Iterable
lista = [3,4,6,4] #true
cadena = "Python"#true
numero = 1#false, no se puede recorrer
print(isinstance(lista, Iterable))#funcion xa saber si es iterable o no 
"""


"""
#ITERADORES
lista=[5,6,7,6]
it = iter(lista)
print(it)
print(type(it))"""



"""
#ITERABLES E ITERADORES
lista=[5,6,7,6]
it = iter(lista)
print(next(it))
print(next(it))
print(next(it))
"""









































































































