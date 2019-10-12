def ordenar(lista, cant):
    if cant>1:
        for f in range(0, cant-1):
            if lista[f]>=lista[f + 1]:
                aux=lista[f]
                lista[f]=lista[f + 1]
                lista[f + 1] = aux
            ordenar(lista, cant - 1)

datos=input().split(" ")
for i in range(len(datos)):
	datos[i]=int(datos[i])

ordenar(datos, len(datos))

for i in range(len(datos)-1,-1,-1):
	print(datos[i])