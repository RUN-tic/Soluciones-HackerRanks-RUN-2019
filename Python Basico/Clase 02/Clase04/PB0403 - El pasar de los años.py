fecha1 = int(input())
fecha2 = int(input())

if fecha1 > fecha2:
    print("Desde el", fecha2, "han pasado", fecha1 - fecha2)
elif fecha1 < fecha2:
    print("Para llegar al", fecha2, "faltan", fecha2 - fecha1)
else:
    print("Son el mismo.")