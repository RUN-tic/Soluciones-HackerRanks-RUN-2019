def Impares(lista):
	lis=[]
	cont=0
	for i in range(len(lista)):
		if int(lista[i])%2!=0:
			lis.append(int(lista[i]))
			cont+=1
	if cont==0:
		return "VACIO"
	return(lis)

s=input().split(" ")

print(Impares(s))