"""Izveidot programmu elektroenerģijas ikmēneša patēriņa aprēķināšanai (Tet Stabilā lietotājiem), kas prasa lietotājam ievadīt līguma termiņu, iepriekšējo un esošo skaitītāja rādījumu un izvada patērētās kWh un maksājamo summu. Programmas sastādīšanā izmantot funkcijas.
Zināms, ka Tet Stabilais tarifs ir atkarīgs no termiņa, uz cik ilgu laiku slēgts līgums."""
import rekins
term=int(input("Ievadi līguma termiņu: \n"))
r1=float(input("Ievadi iepriekšējo rādījumu: \n "))
r2=float(input("Ievadi esošo rādijumu:\n"))
print("Paterētas", kw)