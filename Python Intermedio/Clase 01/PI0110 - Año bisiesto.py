n=int(input())
if n%4 ==0:
	if n%400==0:
		print("Es bisiesto")
	elif n%100==0:
		print("No es bisiesto")
	else:
		print("Es bisiesto")

else :
	print("No es bisiesto")