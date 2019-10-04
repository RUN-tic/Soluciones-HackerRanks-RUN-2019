a = float(input())
b = float(input())
c = float(input())
 
d = b * b - 4 * a * c
if a == b == c == 0:
   print("No tiene solucion")
elif a == b == 0:
   print("No tiene solucion")
elif a == 0:
   print("Tiene una solucion:", - c / b)
elif d < 0:
   print("Tiene solucion imaginaria")
elif d == 0:
   print("Tiene una solucion:", - b / (2 * a))
else:
   print("Tiene dos soluciones:", (-b - d ** 0.5) / (2 * a), "y", (-b + d ** 0.5) / (2 * a))
