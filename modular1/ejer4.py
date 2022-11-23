'''
Created on Nov 11, 2022
Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
@author: jose carlos
'''
fin="no"
lista=[]
while fin!="si":
    numero=int(input("Dí un numero:"))
    lista.append(numero)
    if numero<0:
        fin="si"
   
def Obtenerelementomayor(lista):
    mayor=lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
   
       
    return mayor


def numeroPares(lista):
    par=[0]
    for i in lista:
        if i%2==0:
            par.append(i)
           
    return par
print(f"Los numeros pares son los siguente:{numeroPares(lista)}")
print(f"El numero mayor es :{Obtenerelementomayor(lista)}")

















