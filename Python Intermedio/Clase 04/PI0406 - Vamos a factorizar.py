def factorizar(num):
  i=2
  while i<=num:
    if num%i == 0:
      print(i)
      return factorizar(num/i)
    else:
      i+=1
  return i
      

