a1=float(input())
suma=0
for i in range(10):
	a2=float(input())
	suma=suma+a2

prom=suma/10
if (prom>a1):
	print("SUBIO")
else:
	print("BAJO")