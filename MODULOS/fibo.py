# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:44:06 2022
MODULOS EN PYTHON
@author: lucia
"""
def fib(n):
    a,b=0,1
    while a<n:
        print(a, end='')
        a,b=b, a+b
    print()
   
def fib2(n):
    result=[]
    a,b = 0,1
    while a<n:
        result.append(a)
        print(a,end=' ')
        a,b=b ,a+b
    return result

