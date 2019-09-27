s=input().split()

for i in s:
	if i==" ":
		s.remove(i)

for i in range(len(s)):
	a=len(s[i])
	if len(s[i])>5:
		s[i]=s[i][0:5]+"@"

for i in s:
	print(i,end=" ")