def token(expr):
  tmp = expr.strip()
  if tmp[0] != "(":
    print("error")
    return
  count = 0
  res = 0
  for (k, item) in enumerate(tmp):
    if item == "(":
      count += 1
    if item == ")":
      count -= 1
    if count == 0:
      res = k
    k += 1  
  return res
