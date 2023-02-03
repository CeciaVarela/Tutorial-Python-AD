suma1=0
suma2=0
x=1
print("Carga de la primera lista")
while x<=15:
    valor = int(input("Ingrese valor: "))
    suma1 = suma1 + valor
    x = x + 1
x=1
print("Carga de la segunda lista")
while x<=15:
    valor = int(input("Ingrese valor: "))
    suma2 = suma2 + valor
    x = x + 1
if suma1>suma2:
    print("La lista 1 tiene un valor acumulado mayor")
else:
    if suma2>suma1:
        print("La lista 2 tiene un valor acumulado mayor")
    else:
        print("Las listas tienen un valor acumulado igual")