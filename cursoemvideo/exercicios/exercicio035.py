from math import fabs

reta1 = float(input("\nInforme o valor da 1º reta: "))
reta2 = float(input("Informe o valor da 2º reta: "))
reta3 = float(input("Informe o valor da 3 reta: "))

if fabs(reta2-reta3) < reta1 < reta2 + reta3 and fabs(reta1 - reta3) < reta2 < reta1 + reta3 and fabs(reta1 - reta2) < reta3 < reta1 + reta2:
    print(f"Os valores informados, {reta1}, {reta2}, {reta3} FORMAM um triângulo")
else:
    print(f"Os valores informados, {reta1}, {reta2}, {reta3} NÃO FORMAM um triângulo")
