centimetros = int(input())

kilometros = centimetros // 100000
metros = centimetros % 100000 // 100
resto = centimetros % 100

print(centimetros, "cm son ", end="")
if kilometros:
    if metros or resto:
        print(kilometros, "km ", end="")
    else:
        print(kilometros, "km ")
if metros:
    if resto:
        print(metros, "m ", end="")
    else:
        print(metros, "m ")
if centimetros == 0 or resto:
    print(resto, "cm")