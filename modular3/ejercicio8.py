'''
Created on Dec 2, 2022

@author: jose carlos
'''
def contar_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

cadena = "Vamos a contar vocales"
cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}'' hay {cantidad} vocales")


lista1 = ['A','B','C','D','**H**','P','**O**','T','R','**L**','**A**','L','A']
palabra = 'HOLA'

import re

regex="("+".*?".join(palabra) + ")"

lista1Cadena=" ".join(lista1)

encontrados = re.finditer(regex, lista1Cadena, re.MULTILINE)
cantidad=len([matchNum for matchNum, match in enumerate(encontrados, start=1)])

print("Se encontraron {} palabra(s) {} en la lista".format(cantidad,palabra))