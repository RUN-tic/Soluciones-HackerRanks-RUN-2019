s=input()
longitud=len(s)
altura=round(((1+8*len(s))**0.5-1)//2)
h=s+"*"*(longitud-int(altura*(altura+1)/2))

a=0
b=1
for i in range(altura+1):
	print(h[a:b])
	a=b
	b=b+i+2
