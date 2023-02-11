cantidad=0
num = int(input("Cuantos valores ingresará: "))
for f in range(num):
    valor = int(input("Ingrese el valor: "))
    if valor>=1000:
        cantidad = cantidad + 1
print("Cantidad de valores mayores o iguales a 1000")
print(cantidad)