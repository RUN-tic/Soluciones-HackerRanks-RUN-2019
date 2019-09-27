n=int(input())
a=[]
for i in range(n):
    gg=input()
    gg=gg.split(" ")
    a.append(gg)

b=input()

for i in range(n):
    if b==a[i][0]:
        suma=0
        for j in range(5):
        	suma+=float(a[i][j+1])

#print("{0:.1f}".format(float(suma/3)))
print(round(suma/5,1))