'''
Created on Dec 2, 2022

@author: Jose carlos
'''
letras=input("Introduce una cadena de letras: ")

def upperCaseInString():
    
    return f"Letras mayusculas: {sum(1 for c in letras if c.isupper())}"


print(upperCaseInString())