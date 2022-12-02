'''
Created on Dec 2, 2022

@author: estudiante
'''
text = input("Introduce una frase para contar palabras:")


result = len(text.split())

print("tiene " + str(result) + " palabras.")
def contar_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

cadena = input("introduzcamos una frase para contar vocales")
cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}'' hay {cantidad} vocales")
lista1 = ['A','B','C','D','**H**','P','**O**','T','R','**L**','**A**','L','A']
