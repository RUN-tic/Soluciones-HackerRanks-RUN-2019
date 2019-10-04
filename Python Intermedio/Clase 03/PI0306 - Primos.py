def Esprimo(x):
	cont=0
	for j in range(2,1+int(x/2)):
		if x%j==0:
			cont+=1
			break
	if cont==0:
		return 1
	else:
		return 0

s=input().split(" ")
lista=[]
for i in range(len(s)):
	if Esprimo(int(s[i])):
		lista.append(int(s[i]))
if len(lista)==0:
	print("VACIO")
else:
	print(lista)
