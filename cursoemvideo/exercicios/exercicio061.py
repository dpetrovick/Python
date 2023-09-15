print("\n # PROGRESSÃO ARITIMÉRICA COM WHILE #\n")

num = int(input("Informe um número: "))
raz = int(input("Informe a razão: "))
for pa in range(num, num + (raz * 10), raz):
    print(pa, end=" --> ")
print("FIM")

print("\nAgora com while\n")

num = int(input("Informe um número: "))
raz = int(input("Informe a razão: "))
termo = num
cont = 1
while cont <= 10:
    print(f"{termo}", end=" --> ")
    termo += raz
    cont += 1
print("fim")
