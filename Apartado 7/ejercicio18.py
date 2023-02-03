total_preguntas = int(input("Ingrese el total de preguntas: "))
total_correctas = int(input("Ingrese el total de preguntas correctas: "))
porcentaje = (total_correctas * 100) / total_preguntas
if porcentaje >= 90:
    print("Nivel máximo")
else:
    if porcentaje >= 75:
        print("Nivel Medio")
    else:
        if porcentaje >= 50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
