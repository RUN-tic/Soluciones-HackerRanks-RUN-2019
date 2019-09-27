s=input()
sinvert=""
for i in range(len(s)):
	j=len(s)-i
	sinvert=sinvert+s[j-1]
palabra=input()

if palabra in s:
	print("Si se encuentra la palabra en la frase")
elif palabra in sinvert:
	print("Si se encuentra la palabra en la frase")
else:
	print("No se encuentra la palabra en la frase")
