s=input()
width=int(input())
a=""
for i in s:
	a=a+i
	if len(a)==width:
		print(a)
		a=""
print(a)