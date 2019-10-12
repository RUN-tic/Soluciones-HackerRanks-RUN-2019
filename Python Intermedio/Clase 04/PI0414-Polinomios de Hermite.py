def hermite(n, x):
    if n==0:
        return 1;
    elif n==1:
        return 2*x;
    else:
        return 2*x*hermite(n-1,x)-2*(n-1)*hermite(n-2,x);
 
n=int(input())
x=int(input())
print(hermite(n,x))