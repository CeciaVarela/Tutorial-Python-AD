num = int(input("Ingrese un número entre 1 y 999: "))
if num < 10:
    print("Tiene 1 dígito")
else:
    if num < 100:
        print("Tiene 2 dígitos")
    else:
        if num < 1000:
            print("Tiene 3 dígitos")
        else:
            print("Error en la entrada de datos")
"""print("Fin del programa")"""