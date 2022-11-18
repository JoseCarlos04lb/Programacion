'''
Created on Nov 11, 2022

@author:  jose carlos 
'''

def bisiesto(year):
    return (year%4==0 and (year%100!=0 or year%400==0))

def fechavalida(d, m, y):
    dias_maximo_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return (1<= d <= dias_maximo_por_mes[m-1]
            or (bisiesto(y) and m==2 and 1<=d<=29)
        )

def transformarfecha(day, month, year):
    nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if fechavalida(day, month, year):
    
        mes_largo = nombre_meses[month-1]
        resultado = f"{day} de {mes_largo} de {year}"
        
    else:
        resultado = "La fecha introducida es incorrecta."
        
    return resultado


dia     = int(input("Introduzca un día: "))
mes     = int(input("Introduzca un mes válido: "))
año    = int(input("Introduzca un mes válido: "))

while dia >= 0:
    print(transformarfecha(dia, mes, año))
    
    dia     = int(input("Introduzca un día: "))
    mes     = int(input("Introduzca un mes válido: "))
    año    = int(input("Introduzca un mes válido: "))

        
        
        