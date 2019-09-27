suma=0
num=int(input())
while num!=0:
    digito=num%10
    suma+=digito
    num=num//10

print("La suma de digitos es:", suma)