#PI0319
def padovan(n):
    """ Precondición: n entero >=0
        Devuelve: n! """
    if n == 0 or n==1:
        return 1
    if n == 2:
        return 1
    return padovan(n-2)+padovan(n-3)
    
n=int(input())
S=padovan(n+5)-2
print(S)
