def summa(term, r1, r2):

  if term==1:
    summa=kw*0.20159
  elif term==2:
    summa=kw*0.16961
  elif term==3:
    summa=kw*0.16427
  else:
    summa=kw*0.15964
  return summa, kw
