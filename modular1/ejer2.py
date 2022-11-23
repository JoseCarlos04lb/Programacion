'''
Created on Nov 10, 2022

@author: estudiante
'''
#ACTIVIDAD 2

def Listanumero():
    lista=[]
    contador=0
    while contador<10:
        numero = int(input("Introduce un número:"))
        contador+=1
        lista.append(numero)
    return(lista)
print(Listanumero())
