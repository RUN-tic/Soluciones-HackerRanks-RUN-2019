a = float(input())
b = float(input())

if a == b == 0:
    print("Hay infinitas soluciones")
elif a == 0:
    print("No hay solucion")
else:
    print("Hay una solucion:", -b/a)
