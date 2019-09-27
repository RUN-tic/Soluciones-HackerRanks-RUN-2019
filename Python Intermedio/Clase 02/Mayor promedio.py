lista=[]
promedio1=0
promedio2=0
promedio3=0
for i in range(3):
	s=input()
	lista.append(s)
	for i in range(5):
		n=int(input())
		lista.append(n)

for i in range(5):
	promedio1+=lista[i+1]
	promedio2+=lista[i+7]
	promedio3+=lista[i+13]

promedio1=promedio1/5
promedio2=promedio2/5
promedio3=promedio3/5

if promedio1>promedio2 and promedio1>promedio3:
	print(lista[0],"tiene el mayor promedio")
elif promedio2>promedio3 and promedio2>promedio3:
	print(lista[6],"tiene el mayor promedio")
else:
	print(lista[12],"tiene el mayor promedio")


