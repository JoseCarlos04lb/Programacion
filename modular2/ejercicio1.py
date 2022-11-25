"""
Diseñe un método llamado computeFactorial que reciba un entero positivo y
devuelve el factorial para ese número. Si el número es negativo, el método debe
devuelve Ninguno.
"""
numero= int(input("Introduce un numero positivo= "))

def calcular_factorial(numero):
    if numero>=0:
        factorial=1
        for i in range(1, numero+1):
            factorial=factorial*i
        return factorial
    else:
        return None
   
print(f"El factorial es:  {calcular_factorial(numero)}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    