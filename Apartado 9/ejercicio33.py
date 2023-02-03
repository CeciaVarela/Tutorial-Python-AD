suma = 0
x = 1
num = int(input("Cuantas personas va a procesar: "))
while x<=num:
    altura = float(input("Ingrese la altura: "))
    suma = suma + altura
    x = x + 1
promedio = suma / num
print("Altura promedio")
print(promedio)