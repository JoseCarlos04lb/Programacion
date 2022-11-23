'''
Created on Nov 15, 2022
Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario.
@author: estudiante
'''
lista =[25 , 1, 69,89]

def estaordenada(lista=[]):
    aux=lista=[0]
    estado=True
    contador=0
    for i in range (len (lista[0:-1])):
        if lista[i]>aux and lista[i]<lista[i+1]:
            contador+=1
    if contador ==len(lista)-1:
        estado=True 
    else:
        estado= False 
    return estado
print(estaordenada(lista))