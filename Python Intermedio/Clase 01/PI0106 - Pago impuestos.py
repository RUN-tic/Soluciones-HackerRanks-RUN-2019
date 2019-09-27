Edad=int(input())
Sueldo=float(input())


if Edad>=18:
	if Sueldo>= 1200.0:
		print("Debes pagar impuestos")
	else:
		print("Tus ingresos son bajos")
else:
	if Sueldo>=1200.0:
		print("Eres menor de edad")
	else:
		print("Eres menor de edad y tus ingresos son bajos")