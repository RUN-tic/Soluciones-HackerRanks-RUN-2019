def Entre_ellos(x,y):
	lista=[]
	if x<y:
		for i in range(y-x-1):
			lista.append(x+i+1)
	elif y<x:
		for i in range(x-y-1):
			lista.append(y+i+1)
	else:
		return "VACIO"

	return lista

n=int(input())
m=int(input())
print(Entre_ellos(n,m))