'''
Created on Nov 17, 2022

@author: estudiante
'''
lista = []
numero = int(input("Ingresa un número (ingresa uno negativo para terminar): "))
contador = 1
lista.append(numero)
while numero >=0:
  numero = int(input("Ingresa un número (ingresa uno negativo para  terminar): "))
  lista.append(numero)
  contador +=1
  def Primos(lista):
    listaPrimos = []
    for NUM in range(1,lista+1):
        c=0
        for inx in range(1,NUM+1):
            if NUM % inx == 0:
                c+=1
        if c == 2:
            listaPrimos.append(NUM)
   
    return Primos
   
  def SumaN():
    suma=0
    for i in range (len[lista]):
      suma += lista[i]
    return SumaN

  def Promedio():
    promedio_valores= SumaN/contador
    return Promedio
   
  def calcularFactorial():
    factorial=1
    for i in range (lista + 1):
      factorial=factorial*i
      return calcularFactorial
print (calcularFactorial)


