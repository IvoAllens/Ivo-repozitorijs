def vati(r1, r2):
  kw= r2-r1
  return kw

def summa(term, kw):
  if term==1:
    summa=kw*0.20159
  elif term==2:
    summa=kw*0.16961
  elif term==3:
    summa=kw*0.16427
  else:
    summa=kw*0.15964
  return summa
