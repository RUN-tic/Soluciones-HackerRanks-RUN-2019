respuesta = input()

if respuesta == "T" or respuesta == "t":
   base = int(input())
   altura = int(input())
   print("Un triangulo de base", base, "y altura", altura, "tiene un area de", base * altura / 2)
elif respuesta == "C" or respuesta == "c":
   r = int(input())
   print("Un circulo de radio", r, "tiene un area de", 3.141592 * r * r)
