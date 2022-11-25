'''
Created on Nov 25, 2022

@author: estudiante
'''
base= int(input("Introduce la base:"))
exponente = int(input("Introduce el exponente:"))

def poder (base, exponente=0):
    potencia = base**exponente
    return potencia

print("La potencia es: ")
print(poder (base,exponente ))