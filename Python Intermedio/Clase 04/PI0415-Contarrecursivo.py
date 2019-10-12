def contar_recursivo(s, c):
  if len(s) == 1:
    if s == c:
      return 1
    else:
      return 0
  else:
    if s[0] == c:
      return 1 + contar_recursivo(s[1:], c)
    else:
      return contar_recursivo(s[1:], c)

print(contar_recursivo(input(), input()))
