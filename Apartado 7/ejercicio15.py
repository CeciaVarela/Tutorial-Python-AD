num1 = int(input("Introduce el primer valor: "))
num2 = int(input("Introduce el segundo valor: "))
num3 = int(input("Introduce el tercer valor: "))
print("El valor mayor de los tres es")
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)