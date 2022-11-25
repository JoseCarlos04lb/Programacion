'''
Created on Nov 25, 2022
Diseñe un método llamado getPrimeDivisors que reciba un número positivo como
parámetro y devuelve una lista que contiene sus divisores primos. Si el parámetro no es válido
el método debe devolver Ninguno.
@author: estudiante
'''

numero = int(input("Introduce un numero:"))

def primo(numero):
    while numero>0:
        primo =True
        for i in range(2,numero):
            if numero%i==0:
                primo=False
        return primo
    
def divisor(numero):
    lista=[]
    for i in range(1,numero):
        if numero%i==0:
            if primo(i):
                lista.append(i)
    return lista 

print(divisor(numero))