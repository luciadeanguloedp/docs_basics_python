# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:44:24 2022

Ejercicio 3: Crear un programa que tenga el siguiente menú:
1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la 
posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
3. Longitud de la lista: te muestra el número de elementos de la lista.
4. Eliminar el último número: Muestra el último número de la lista y lo borra.
5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella 
(la posición se pide a partir de 1).
6. Contar números: Te pide un número y te dice cuántas apariciones hay en la lista.
7. Posiciones de un número: Te pide un número y te dice en que posiciones está 
(contando desde 1).
8. Mostrar números: Muestra los números de la lista
9. Salir

@author: lucia
"""
op = 0
lista = [1,2,3,4,5]

print(f"La lista es: {lista}\n")
while(op != 9):
    op = int(input("INTRODUZCA UNA OPCIÓN:\n\t1. AÑADIR NÚMERO A LA LISTA\n\t2. AÑADIR NÚMERO EN POSICIÓN CONCRETA\n\t3. LONGITUD DE LA LISTA\n\t4. ELIMINAR ÚLTIMO NÚMERO\n\t5. ELIMINAR UN NÚMERO\n\t6. CONTAR NÚMEROS\n\t7. POSICIÓN(ES) DE UN NÚMERO\n\t8. MOSTRAR NÚMEROS\n\t9. SALIR\n"))
    
    if(op == 1):
        n = len(lista)
        final = int(input("Introduzca el número de la lista que desea añadir al final"))
        for i in range(n):
            if(final == lista[i]):
                lista[i],lista[n-1] = lista[n-1],lista[i]
        print(f"La nueva lista es: {lista}\n")
        
    elif(op == 2):
        n = len(lista)
        contt = 0
        num = int(input("¿Qué número desea añadir? "))
        pos = int(input("¿Y en qué posición (a partir de 1) ? "))
        for i in range(n):
            if(i == pos-1):
                contt+=1
                lista.insert(i,num)
        if(contt==0):
            lista.append(num)
        print(f"La nueva lista es: {lista}\n") 
        
    elif(op == 3):
        n = len(lista)
        print(f"En la lista hay {n} elementos\n")
    elif(op == 4):
        n = len(lista)
        ult = lista.pop(n-1)
        print(f"El elemento eliminado es {ult} y la lista ahora es: {lista}")
    elif(op == 5):
        n = len(lista)
        contt = 0
        num = int(input("¿Qué posición desea eliminar? "))
        for i in range(n):
            if(i == num-1):
                contt+=1
                lista.pop(i)
        if(contt==0):
            print("La posición introducida no existe, la lista se queda igual.\n")
        else:
            print(f"La nueva lista es: {lista}\n") 
    elif(op == 6):
        n = len(lista)
        num = int(input("Introduzca un número para ver cuántas veces aparece en la lisa: "))
        cont = 0
        for i in lista:
            if(num == i):
                cont+=1
        print(f"El número {num} aparece {cont} veces en la lista\n")
    elif(op == 7):
        n = len(lista)
        cont = 0
        num = int(input("Introduzca un número para ver en qué posición(es) está: "))
        for i in range(n):
            if(lista[i] == num):
                print(f"El número {num} aparece en la posición {i+1}\n")
    elif(op == 8):
        print(f"La lista es: {lista}\n")
    elif(op == 9):
        print("Saliendo...")
    else:
        print("Opción incorrecta.")
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        