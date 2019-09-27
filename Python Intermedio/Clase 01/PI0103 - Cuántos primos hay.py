n=int(input())
contador=0
for i in range(n):
	a=int(input())
	for i in range(2,a//2+1,1):
		if a%i==0:
			break
	else:
		contador=contador+1

print("La cantidad de numeros primos es",contador)