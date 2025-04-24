# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 08:15:26 2022

METODOS PRINCIPALES STRING
CADENAS

@author: lucia de angulo pelayo

"""
#METODOS DE FORMATO. 
#Devuelve string con la primera mayúscula
cadena = 'hola, qué tal'
print(cadena.capitalize())
#devolver todo en mayusculas o todo en minusculas
cad = 'Hola, Qué tal'
print(cad.upper())
print(cad.lower())
#devuelve cadena con mayusculas en minuscula y viceversa
print(cad.swapcase())




#MÉTODOS DE BÚSQUEDA
#cuantas veces aparece un caracter
cont = 'holaaaaa'
print(cont.count('a'))
#encontrar caracter, retorna -1 si no encuentra, y si la encuentra me dice la posicion, en este caso 1
print(cont.find('ol'))






#MÉTODOS DE VALIDACION
#indicar si cadena empieza por cierta subcadena.  Retorna true o false.  Importante:sensible a mayus y minusculas
cadena2 = 'Me llamo'
print(cadena2.startswith('Me',0)) #añado que sea en posicion 0
#verifica cadena alfanumerica.  Return true si los elementos son alfa numericos(letras + nums), return false otherwise
verif = 'python123'
print(verif.isalnum())
#verifica si es cadena numerica. false o trye. solo numeros (ni puntos, comas...)
nums = '2345'
print(nums.isdigit())




#MÉTODOS DE SUSTITUCION
#para formateo de cadena, retorna cadena formateada
cad2 = 'Bienvenido a python{0}'
print(cad2.format(' luis'))
cad3 = 'importe bruto: ${0} + IVA {1}'
print(cad3.format(100,21))
#devuelve cadena donde sustituye primera subcadena por la segunda indicandole como parametro
buscar = "nombre_apellido"
reemplazar_por = "Ivan rodriguez"
print("Estimado sr nombre_apellido".replace(buscar, reemplazar_por))
#devuelve cadena sin espacios al principio y al final
cadd = '  www.ufv .es   '
print(cadd.strip())









#MÉTODOS DE UNION Y DIVISION
#union entre cadenas, en las comas añado
formato_factura=("N 000-0","-000(10:",")")
numero = "275"
numero_factura=numero.join(formato_factura)
print(numero_factura)
#separador. retorna lista con todos los elementos encontrados al divicir la cadena con un separador, creo lista
palabras='casa,arbol-silla,mesa'.split("-")
print(palabras)







numss = '2345f'
print(numss.isdigit())

contrasena = "sdgrnkewk8865"
print(contrasena.islower())












