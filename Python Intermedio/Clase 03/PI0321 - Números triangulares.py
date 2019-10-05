#PI0321

def triangular(n):
    if n<=0:
        return 0
    else:
        return triangular(n-1)+n
n=int(input())
print(triangular(n))
