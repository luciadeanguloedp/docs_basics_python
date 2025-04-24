# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:26:01 2022

@author: lucia
"""

class Motocicleta():
    # Atributos de clase
    estado = "nueva"
    enmarcha = False

    # Métodos
    def __init__(self, color, matricula,  ruedas, marca, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.ruedas = ruedas
        self.marca = marca
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
    def arrancar(self):
        if self.enmarcha:
            print("El motor ya estaba arrancado.")
        else:
            print("Motor arrancado correctamente.")
    def detener(self):
        if self.enmarcha:
            print("Se ha detenido el motor.")
        else:
            print("No puedes parar el motor, ya está parado.")
#ahora creare dos objetos
motocicleta1 = Motocicleta("Negro", "1234QQQ", 2, "Dinamo", 2022, 288, "200 kg" )
motocicleta2 = Motocicleta("Rojo", "11111QQQQ", 2, "Yamaha", 2021, 288, "199 kg")

print("\n\t***MOTOCICLETA 1***\n")
motocicleta1.arrancar()
print(f"La motocicleta {motocicleta1.estado} de la marca {motocicleta1.marca} es de color {motocicleta1.color}, tiene {motocicleta1.ruedas} ruedas, se fabricó en el año {motocicleta1.fecha_fabricacion}, su velocidad punta es {motocicleta1.velocidad_punta} km/h y pesa {motocicleta1.peso}\n\n")
print("\n\t***MOTOCICLETA 2***\n")
motocicleta1.detener()
print(f"La motocicleta {motocicleta2.estado}  de la marca {motocicleta2.marca} es de color {motocicleta2.color}, tiene {motocicleta2.ruedas} ruedas, se fabricó en el año {motocicleta2.fecha_fabricacion}, su velocidad punta es {motocicleta2.velocidad_punta} km/h y pesa {motocicleta2.peso}")
