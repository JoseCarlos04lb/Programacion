'''
Created on Nov 25, 2022
Diseñe un método llamado isFriendNumber que reciba dos números positivos y
devuelve True si los números son amigos, False en caso contrario. dos numeros son
considerados amigos si la suma de sus divisores, excepto el número dado, es igual
al segundo y viceversa.
@author: estudiante
'''
numero1=int(input("Dime el primer numero"))
numero2=int(input("Dime el primer numero"))
def numerosamigos(numero1,numero2):
    lista1=[]
    lista2=[]
    divisores1=0
    divisores2=0
    amigos=False
    if numero1>0 and numero2>0:
        for i in range(2,numero1):
            if numero1%i==0:
                lista1.append(i)
                divisores1+=i
        for i in range(2,numero2):
            if numero2%i==0:
                lista2.append(i)
                divisores2+=i
        if divisores1==divisores2:
            amigos=True
    else:
        None
    return amigos
print(numerosamigos(numero1, numero2))