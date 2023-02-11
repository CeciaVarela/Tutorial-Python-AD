suma1=0
suma2=0
suma3=0
for f in range(5):
    edad=int(input("Ingrese la edad: "))
    suma1 = suma1 + edad
prom1 = suma1/5
print("Promedio de edades del turno de mañana")
print(prom1)

for f in range(6):
    edad=int(input("Ingrese la edad: "))
    suma2 = suma2 + edad
prom2 = suma2/6
print("Promedio de edades del turno de tarde")
print(prom2)

for f in range(11):
    edad=int(input("Ingrese la edad: "))
    suma3 = suma3 + edad
prom3 = suma3/11
print("Promedio de edades del turno de noche")
print(prom3)

if prom1<prom2 and prom1<prom3:
    print("El turno de mañana tiene un promedio de edades menor")
else:
    if prom2<prom3:
        print("El turno de tarde tiene un promedio de edades menor")
    else:
        print("El turno de noche tiene un promedio de edades menor")
