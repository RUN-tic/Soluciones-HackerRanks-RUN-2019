    fecha = int(input())

    if fecha % 400 == 0:
        print(fecha, "es bisiesto")
    elif fecha % 100 == 0:
        print(fecha, "no es bisiesto")
    elif fecha % 4 == 0:
        print(fecha, "es bisiesto")
    else:
        print(fecha, "no es bisiesto")
