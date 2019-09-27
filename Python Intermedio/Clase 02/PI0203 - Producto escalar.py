v1=input().split(",")
v2=input().split(",")

producto=0
for i in range(3):
	producto+=int(v1[i])*int(v2[i])

print("El producto escalar es",producto)