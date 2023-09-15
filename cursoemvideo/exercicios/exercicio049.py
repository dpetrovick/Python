num = int(input("\nInforme um número para ver a sua tabuada: "))
print("\n")

for i in range(1, 11):
    print(f"{num}  X {i:2} = {num * i:2}")

# o :2 é para usar duas casas para alinhar um número com 1 e dois algarismos (ex: 9 e 10) - para não "ficar torto"
