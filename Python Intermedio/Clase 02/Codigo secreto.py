s=input()
lista=s.split(" ")
n=len(lista)
a=""
for i in s:
	if i!=" ":
		a+=i

for i in range(0,len(a),n):
	print(a[i],end="")

