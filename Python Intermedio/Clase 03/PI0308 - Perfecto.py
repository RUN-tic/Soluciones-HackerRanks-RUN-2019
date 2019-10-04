def Perfecto(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

if Perfecto(int(input())):
	print("Es perfecto")
else:
	print("No es perfecto")
