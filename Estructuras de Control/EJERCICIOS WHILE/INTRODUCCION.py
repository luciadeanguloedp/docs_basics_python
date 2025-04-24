# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 08:07:20 2022

@author: lucia
"""
#BUCLE WHILE ESTRUCTURAS DE CONTROL

"""x=5
while x>0:
    x-=1
    print(x)"""
    
    
    
    
    
"""anio=2001
while anio<= 2012:
    print("Informes del año", str(anio))
    anio +=1 """
    
    
    
#EN UNA MISMA LINEA?    
"""x=5
while x>0:x-=1;print(x)  #se puede hacer en una sola linea"""




#USAR X.POP
"""x=["Uno", "Dos", "Tres"]
while x:
    x.pop(0) #va eliminando elementos, cuando lista esta vacia es "false"
    print(x)"""





#ELSE Y WHILE MEZCLADOS
"""x=5
while x>0:
    x-=1
    print(x)
else:  #se ejecuta al terminar el while enteror
    print("El bucle ha finalizado")"""
    
    
    
"""x=5
while True:
    x-=1
    print(x)
    if x==1:
        break
else: #con el break esto no se cumple
    print("Fin del bucle")"""
    
    
    
    
#FUNCIÓN LEN() PYTHON
"""mylist=["a","b","c"]
x = len(mylist) #len da la length del elemento
print(x)

text = "Python"
i=0
while i<len(text):
    print(text[:i+1])
    i+=1
"""




#SUCESION FIBONACCI
a,b=0,1
while b<1000:
    print(b)
    a,b=b,a+b




















