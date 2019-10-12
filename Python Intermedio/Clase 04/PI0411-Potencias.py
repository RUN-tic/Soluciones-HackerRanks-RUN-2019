def es_potencia(n,b):
	if n==1:
		print("True")
		return 0
	elif b==1 or b==0 or n==0:
		print("False")
		return 0
	elif n%b==0:
		if n/b==1:
			print("True")
		else:
			n=n/b
			es_potencia(n,b)
	else:
		print("False")

n=input().split(" ")
es_potencia(int(n[0]),int(n[1]))
