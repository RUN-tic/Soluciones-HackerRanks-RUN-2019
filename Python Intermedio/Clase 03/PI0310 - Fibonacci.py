def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n=int(input())
print("El termino",n,"de la sucesion de Fibonacci es", fib(n))