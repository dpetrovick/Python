ano = int(input("\nInforme um ano para saber se ele é bissexto: "))
res1 = ano % 4
res2 = ano % 100
res3 = ano % 400
if res1 == 0 and res2 != 0 or res3 == 0:
   print(f"\nO ano {ano} digitado é BISSEXTO!!!")
else:
    print(f"\nO ano {ano} digitado NÃO É BISSEXTO!!")

# Solução do professor
from datetime import date
ano = int(input("\nInforme um ano para saber se ele é bissexto: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print(f"\nO ano {ano} digitado é BISSEXTO!!!")
else:
    print(f"\nO ano {ano} digitado NÃO É BISSEXTO!!")