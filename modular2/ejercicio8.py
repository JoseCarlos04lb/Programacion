'''
Created on Nov 25, 2022
Diseñe un método llamado solveSecondOrderEquation que reciba tres enteros
números positivos correspondientes a los coeficientes de una ecuación de segundo orden
(hacha
2+bx+c=0) y calcula sus posibles soluciones. Si los parámetros no son válidos, el
El método debe devolver Ninguno.
@author: estudiante
'''
from math import sqrt

a = int(input("Ingrese el valor al cuadrado"))
b = int(input("Ingrese el valor de x"))
c = int(input("Ingrese el valor del termino independiente"))
x1= 0
x2= 0
def ecuacion2grado():
    if ((b**2)-4*a*c) < 0:
        print("La solución de la ecuación es con números complejos")
    else:
        x1 = (-b+sqrt(a**2-(4*b*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        print("Las soluciones de la ecuación son:")
        print(x1)
        print(x2)
    

print(ecuacion2grado())