def funcion(n):
	if n==1:
		return 4
	elif 1<n<10:
		return funcion(n-1)-2
	else:
		return 0.5*funcion(n-1)+4

print(round(funcion(int(input())),4))