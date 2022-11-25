'''
Created on Nov 25, 2022

@author: estudiante
'''
anyo = int(input("Introduce un año: "))

def bisiesto(anyo):
    bisiesto = False
    if anyo%4 == 0:
        bisiesto = True 
    if anyo%4 == 0 and anyo%100 == 0:
        bisiesto = False
    if anyo%4 == 0 and anyo%100 == 0 and anyo%400 == 0:
        bisiesto = True
    return bisiesto

print(f"El anño {anyo} es bisiesto? {bisiesto(anyo)}")