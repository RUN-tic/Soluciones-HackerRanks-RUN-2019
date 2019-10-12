def mcd(a,b):
  if b==0:
    return a
  elif a==0:
    return b
  elif a>=b:
    return mcd(a-b,b)
  else:
    return mcd(a,b-a)