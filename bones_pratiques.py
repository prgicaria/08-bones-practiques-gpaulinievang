#!/usr/bin/env python

'''División entera. Calcula el resultado de una división entera
Institut Icària
Programació - 1r Batxillerat - Curs 2025-26

Realiza la división de dos números enteros, calculando su resultado y el
resto'''

__author__ = "Gabriela Paulini"
__contact__ = "gpaulini@instituticaria.cat"
__date__ = "2025/10/22"

Dividendo = int(input("Dividendo de la operación"))
Divisor = int(input("Divisor de la operación"))

Cociente = Dividendo//Divisor
Resto = Dividendo % Divisor
print(f"La división es: {Dividendo/Divisor} /n")
print(f"El coeficiente de la división es:{Cociente} /n")
print(f"El resto de la división es:{Resto}")
