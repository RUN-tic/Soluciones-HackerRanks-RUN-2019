#PI0320
def potencia(b,n):
    """ Precondición: n debe ser mayor o igual que cero.
        Devuelve: b\^n. """

    # Caso base
    if n <= 0:
        return 1

    # n par
    if n % 2 == 0:
        pot = potencia(b, n/2)
        return pot * pot
    # n impar
    else:
        pot = potencia(b, (n-1)/2)
        return pot * pot * b

def euler(n):
    if n<0:
        return 1
    elif n==0:
        return 1
    else:
        return 1+1/n
    
n=int(input())
print(potencia(euler(n),n))
