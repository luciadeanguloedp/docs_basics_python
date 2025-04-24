# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 09:32:40 2022
EJERCICIO EXCEL - crearlo y modificar informacion
@author: lucia
"""


from openpyxl import Workbook
from openpyxl.styles import Font  #cambiar estilo, fuente
import time  #meteremos la hora tb

book = Workbook()
sheet = book.active

sheet['A1']=5 #primera columna fila 1
sheet['A2']=10 #primera columna fila 2

sheet['B1']= 'rango'
sheet['B1'].font= Font(color='FF0000', bold=True) #rango en rojo y negrita
for i in range(2,15):
    sheet[f'B{i}']=i**2  #string formateado
    

book.save('agen.xlsx')

