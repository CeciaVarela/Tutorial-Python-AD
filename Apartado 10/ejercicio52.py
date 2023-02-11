cant1=0
cant2=0
cant3=0
cant4=0
num=int(input("Cantidad de puntos: "))
for f in range(num):
    x=int(input("Ingrese coordenada x: "))
    y=int(input("Ingeres coordenada y: "))
    if x>0 and y>0:
        cant1 = cant1 + 1
    else:
        if x<0 and y>0:
            cant2 = cant2 + 1
        else:
            if x<0 and y<0:
                cant3 = cant3 + 1
            else:
                if x>0 and y<0:
                    cant4 = cant4 + 1
print("Cantidad de puntos ingresados en el primer cuadrante")
print(cant1)
print("Cantidad de puntos ingresados en el segundo cuadrante")
print(cant2)
print("Cantidad de puntos ingresados en el tercer cuadrante")
print(cant3)
print("Cantidad de puntos ingresados en el cuarto cuadrante")
print(cant4)

