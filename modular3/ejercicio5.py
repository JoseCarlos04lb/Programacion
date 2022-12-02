'''
Created on Dec 2, 2022

@author: jose carlos
'''
print("Example: 'Dabale arroz a la zorra el abad', '¿Son robos o sobornos?', 'A ti no, bonita', 'Añora la roña', 'Di clases al Cid'")

cadena = str(input("Introduce una frase: "))
def palindromo(cadena):
    beginning = 0
    finish = len(cadena) - 1
    while cadena[beginning] == cadena[finish]:
        if beginning >= finish:
            return True
        beginning += 1
        finish -= 1
    return False



def remove_characters(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("á", "a")
    string = string.replace("é", "e")
    string = string.replace("í", "i")
    string = string.replace("ó", "o")
    string = string.replace("ú", "u")
    string = string.replace("?", "¿")
    string = string.replace("¿", "?")
    
    return string


cadena1 = remove_characters(cadena)
is_Palindromo = palindromo(cadena1)


if is_Palindromo:
    print(True)
    print("Es palindromo")
    
else:
    print(False)
    print("No es palindromo")