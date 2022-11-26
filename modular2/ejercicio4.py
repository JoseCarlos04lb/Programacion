'''
Created on 26 nov 2022

@author: Usuario
'''
fecha=[]
fecha.append(int(input("Introduzca un dia:")))
fecha.append(int(input("Introduzca un mes:")))
fecha.append(int(input("Introduzca un año :")))
def diadelasemana(fecha):
    semana=["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
    a=(14-fecha[1])//12
    y=fecha[2]-a
    m=fecha[1]+12*a-2
    d=(fecha[0] + y + y//4 - y//100 + y//400 + (31*m)//12)%7  
    return semana[d]
print(diadelasemana(fecha))