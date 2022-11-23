'''
Created on Nov 15, 2022
 Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
@author: estudiante
'''

def Listanumero():
    lista=[]
    contador=0
    while contador<10:
        numero = int(input("Introduce un número:"))
        contador+=1
        lista.append(numero)
    return(lista)
rev = list(reversed(Listanumero()))
print(rev)
    
    
    
    
    
    
    
    
