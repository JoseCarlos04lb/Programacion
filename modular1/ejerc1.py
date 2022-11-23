'''
Created on Nov 4, 2022

@author: Jose Carlos
'''

from random import randint
lista=[]

for i in range(100):
    lista.append(randint(0,1000))
     
print(lista)

def obtenerMayor(lista):
    mayor =lista[0]
    for i in range (i) > mayor :
        if lista(i) >mayor:
            mayor = lista(i)     
    return mayor
print(obtenerMayor(lista))

def obtenerMenor(lista):
    menor = lista[0]
    for i in range [i] < menor:
        if lista[i]< menor:
            menor=lista[i]
    return menor
print(obtenerMenor(lista))


def suma(lista):
    contador=0
    for i in range(len(lista)):
        contador+=lista(i)
    return contador

print(suma())

def sustituir_valor(lista_sus,num_buscar,sustituir):  
    for i in range(len(lista_sus)):
        if num_buscar==lista_sus[i]:
            lista_sus[i]=sustituir
    return sustituir

"""
sustituido=int(input("que "))
ns =int(input("que")
"""











