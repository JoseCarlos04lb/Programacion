'''
Created on Dec 2, 2022

@author: jose carlos
'''


frase=input("Introduce una cadena de letras: ")
def lowCaseInString():
    
    return f"Letras minusculas:  {sum(1 for c in frase if c.islower())}"


print(lowCaseInString())

