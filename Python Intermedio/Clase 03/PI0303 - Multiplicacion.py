def Multiplicacion(lista):
	n=1
	for i in range(len(lista)):
		n=n*int(lista[i])
	return n

s=input().split(" ")

print(Multiplicacion(s))
