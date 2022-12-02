'''
Created on Dec 2, 2022

@author: jose carlos
'''
cadena = str(input("Introduce una cadena: "))
vocales = 'aeiou'
consonants = "qwrtyplñkjhgfdszxcvbnm"
a = ""
b= ""
for x in cadena:
    if x in vocales:
        a += x
    elif x in consonants:
        b +=x 
print(f"The change is:",b+a)