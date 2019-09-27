s=input()
sinvert=""
for i in range(len(s)):
	sinvert=sinvert+s[-i-1]

if s==sinvert:
	print("Es palindroma")
else:
	print("No es palindroma")