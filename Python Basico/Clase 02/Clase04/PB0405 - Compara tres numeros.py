X = int(input())
Y = int(input())
Z = int(input())

if X == Y == Z:
    print("Ha escrito tres veces el mismo numero")
elif X == Y or X == Z or Y == Z:
    print("Ha escrito uno de los numeros dos veces")
else:
    print("Los tres numeros que ha escrito son distintos")
