n=input()
n=n.split(" ")
def Maximo2(a,b):
	if a > b:
		return a
	return b

def Maximo3(a,b,c):
	return Maximo2(a,Maximo2(b,c))

print("El maximo numero es",Maximo3(int(n[0]),int(n[1]),int(n[2])))




