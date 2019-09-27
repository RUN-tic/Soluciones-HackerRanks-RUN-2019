s=input()

mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
a=""
for i in s:
    if i in mayusculas:
        a=a+i.lower()
    elif i in minusculas:
        a=a+i.upper()
    else:
        a=a+i

print(a)
