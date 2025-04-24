# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:50:43 2022

@author: lucia
"""

s = 'foo'
t = 'bar'
print('barf' in 2*(s+t)) # * creates 2 copies in this case, barf is inside
print(2*(s)) 
print(ord('f'))
print("----------")
ss='hola123'
print(s[::-3])
print(s[-1::-3])
print("----------")

sss = 'foobar'
print(sss[0]+sss[-1])
print(sss[::-1][-1]+sss[len(s)-1])  
print(sss[::-5])
print(sss[::-1][::-5])
print(sss[::5])
print(sss[::-1][-1]) #devuelve posicion -1 de la nueva palabra creada
print(sss[0:5:2][-2])  #devuelve posicion penultima de foa 
print(sss[:]) # imprime todo 
print("----------")
print(s[::-1][::-1] == s)
print(s[::-1][::-1] is s )#is si tienen el mismo id
print(s[:] == s)
print(s[:] is s)
print("----------")
def greet (person):
    return f'Hello, my name is {person}.'
print(greet('lucia'))
print("----------")
print(
    '$100 $200 $300'.count('$'),
    '$100 $200 $300'.count('$', 5, 10),#start and end but does not include end
    '$100 $200 $300'.count('$', 5)
)

print("----------")

s2 = 'foo-bar-baz'
print('-'.join(s2.split('-'))) #separa en una lista por guiones y  los junta de nuevo con guiones
print(s2.center(23)) #lo centra en la consola, como que lo tabula entero, tanto como le pongas de numero
print(s.upper().lower())
print('-'.join(s2.partition('f'))) #le pido que ponga la f entre guiones
print(s2.strip('-')) #elimina a inicio o final el elemento que le pedimos

print(s2.find('o'))
x = 345.3456
print(format(x,"20.3f")) #3 decimales y centrado en 25


num = 6
for i in range(1,num+1):
    print(i)












