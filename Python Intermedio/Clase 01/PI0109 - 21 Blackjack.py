suma = 0
a = int(input())
while a != 0:
    suma += a
    if suma >= 21:
        print('La suma total es:', suma)
        break
    a = int(input())
else:
    print('La suma total es:',suma)