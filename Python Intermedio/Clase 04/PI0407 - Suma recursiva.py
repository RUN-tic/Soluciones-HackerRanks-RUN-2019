def operar(numero1, numero2):
  if(numero2 == 0):
      return numero1
  elif(numero2 < 0):
      return operar(numero1-1, numero2+1)
  else:
      return operar(numero1+1, numero2-1)