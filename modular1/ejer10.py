'''
Created on Nov 23, 2022

@author: Jose carlos
'''
def conversor (lista):
    if (len(lista)[:-1])=="D":
        def to_decimal(n):
            n = list(n)
            n.reverse()
            decimal = 0
            for i in range(len(n)):
                decimal += int(n[i]) * 2 ** i
            return decimal[:-1]
          
    elif (len(lista)[:-1])=="B":
        def to_binary(n):
            binario = []
            while n > 0:
                binario.append(str(n % 2))
                n //= 2
            binario.reverse()
      
            return ''.join(binario[:-1])
print (lista)