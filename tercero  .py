
dia= int(input("Que día es?:"))
mes = int(input("Que mes es?:"))
año = int(input("Que año es?:"))

while dia <1  or dia >31:
    dia= int(input("Que día es?:"))
while mes <1 or mes >12:
    mes = int(input("Que mes es?:"))


while dia>0:   
    if mes==1:
        print(f"Hoy es {dia} de enero de {año} ")
    elif mes == 2:
        print(f"Hoy es {dia} de febrero de {año} ")
    elif mes == 3:
        print(f"Hoy es {dia} de marzo de {año} ")
    elif mes==4:
        print(f"Hoy es {dia} de abril de {año} ")
    elif mes ==5:
        print(f"Hoy es {dia} de mayo de {año} ")
    elif mes == 6:
        print(f"Hoy es {dia} de junio de {año} ")
    elif mes == 7:
        print(f"Hoy es {dia} de julio de {año} ")
    elif mes == 8:
        print(f"Hoy es {dia} de agosto de {año} ")
    elif mes==9:
        print(f"Hoy es {dia} de septiembre de {año} ")
    elif mes ==10:
        print(f"Hoy es {dia} de octube de {año} ")
    elif mes == 11:
        print(f"Hoy es {dia} de noviembre de {año} ")
    elif mes ==12:
        print(f"Hoy es {dia} de dieciembre de {año}")

