num = int(input("Cuantos triángulos procesará: "))
cantidad = 0
for f in range(num):
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    superficie = base * altura / 2;
    print("Superficie")
    print(superficie)
    if superficie > 12:
        cantidad = cantidad + 1
print("Cantidad de triángulos con superficie mayor a 12")
print(cantidad)
