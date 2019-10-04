if divisor == 0:
        print("No se puede dividir por 0")
    else:
        if Dividendo % divisor == 0:
            print("La division es exacta. Cociente:", Dividendo // divisor)
        else:
            print("La division no es exacta. Cociente:", Dividendo // divisor, "Resto:", Dividendo % divisor)