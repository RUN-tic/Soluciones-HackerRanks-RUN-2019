def mult(a,b):
  if b==0:
    return 0
  else:
    return a+mult(a,b-1)