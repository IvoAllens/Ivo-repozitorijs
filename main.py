
import rekins
term=int(input("Ievadi līguma termiņu: \n"))
r1=float(input("Ievadi iepriekšējo rādījumu: \n "))
r2=float(input("Ievadi esošo rādijumu:\n"))
v=rekins.vati(r1,r2)
s=rekins.summa(term, v)
print("\nParerēti", v, "un samaksāts", round(s,2), "euro." )