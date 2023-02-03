altas = 0
bajas = 0
x = 1
while x<=10:
    nota = int(input("Ingrese la nota: "))
    if nota>=7:
        altas = altas + 1
    else:
        bajas = bajas + 1
    x=x+1
print("Cantidad de alumnos con notas mayores o iguales a 7")
print(altas)
print("Cantidad de alumnos con notas menores a 7")
print(bajas)