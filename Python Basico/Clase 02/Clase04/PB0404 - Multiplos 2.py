X = int(input())
Y = int(input())

if X >= Y and X % Y != 0:
    print(X, "no es multiplo de",Y)
elif X >= Y and X % Y == 0:
    print(X, "es multiplo de", Y)
elif X < Y and Y % X != 0:
    print(Y, "no es multiplo de", X)
else:
    print(Y, "es multiplo de", X)