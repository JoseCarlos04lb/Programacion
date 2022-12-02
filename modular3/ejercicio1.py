'''
Created on Nov 29, 2022

@author: jose carlos
'''

def charactersInString(cadena,caracter):
    contador =0
    for i in range (len(cadena)):
        if caracter.upper()==cadena[i]. upper():
            contador+=1
    return contador