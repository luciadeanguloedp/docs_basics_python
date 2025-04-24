# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:44:24 2022

@author: lucia
"""

import pandas as pd
from pandas import ExcelWriter

nombre = input("Intro nombre:")
apellido = input("Intro edad: ")
numero = input("Intro numero: ")

data = {'Nombre': nombre,
        'Apellido': apellido,
        'Numero': numero,
        }

df = pd.DataFrame(data, index = [0])

with pd.ExcelWriter('agenda.xlsx') as writer:
    df.to_excel(writer)

