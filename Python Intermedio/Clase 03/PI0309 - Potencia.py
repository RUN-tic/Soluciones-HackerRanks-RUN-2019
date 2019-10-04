def potencia(b,n):
    if n == 0 or b==1:
        return 1

    elif n % 2 == 0:
        pot = potencia(b, n/2)
        return pot * pot
    else:
        pot = potencia(b, (n-1)/2)
        return pot * pot * b

a=int(input())
b=int(input())

print(potencia(a,b))