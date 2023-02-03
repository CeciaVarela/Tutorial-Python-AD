sueldo = int(input("Ingrese el sueldo del empleado: "))
antiguedad = int(input("Ingrese la antigüedad en años: "))
if sueldo<500 and antiguedad >=10:
    aumento = sueldo * 0.20
    sueldopag = sueldo + aumento
    print(sueldopag)
else:
    if sueldo < 500:
        aumento = sueldo * 0.05
        sueldopag = sueldo + aumento
        print(sueldopag)
    else:
        print(sueldo)