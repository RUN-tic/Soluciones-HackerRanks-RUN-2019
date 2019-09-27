lista=[]
hombre=0
mujer=0
for i in range(10):
	s=input()
	if s=='hombre':
		hombre+=1
		lista.append('XY')
	else:
		mujer+=1
		lista.append('XX')

print(lista)
print("Hay",hombre,"hombres")
print("Hay",mujer,"mujeres")
