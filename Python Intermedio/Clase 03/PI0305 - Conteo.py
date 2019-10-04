x=int(input())
def conteo(x):
	resultado=0
	n=1
	while (resultado <= x):
		resultado += n*(n+1)*(n+2)
		n+=1
	
	return n-1

print("La cantidad de terminos es",conteo(x))