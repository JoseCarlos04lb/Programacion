'''
Created on Nov 23, 2022

@author: estudiante
'''
numero=int(input("Dime un numero"))

def isPrime(numero):
    if numero>0:
        esPrimo=True
        if numero>2:
            for i in range(2,numero):
                if numero%i==0:
                    esPrimo=False
   
    else:
        esPrimo=None
    return esPrimo
print(isPrime(numero))