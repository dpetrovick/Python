print("\n# CALCULANDO FATORIAL #\n")

num = int(input("informe um número: "))
cont = num
fat = 1
while cont > 0:
    print(cont, end=" ")
    fat *= cont
    cont -= 1

print(f"\n{fat}")

"""UTILIZANDO FOR - EXISTE TB UM MÓDULO EM "MATH"
for i in range (num, 0, -1):
    print(i, end=" ")
    fat *= i
print (f"\nO fatorial é :{fat}")
"""

