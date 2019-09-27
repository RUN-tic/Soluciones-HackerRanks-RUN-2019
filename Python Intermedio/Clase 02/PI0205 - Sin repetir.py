cadena = input()

a= ""
 
for c in cadena:
    if(c not in a):
    	a=a+c
 
print(a)
