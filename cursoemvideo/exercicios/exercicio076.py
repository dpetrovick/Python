print("\n# LISTA DE PREÇOS #\n")

tabela = ("SSD 240GB", "250,00", "SSD 128GB", "180,00", "RAM 4GB DDR4", "230,00", "RAM 8GB DDR4", "340,00")


for i in range(0, len(tabela)):
    if i % 2 == 0:
        print(f"{tabela[i]:.<30}", end=" ")
    else:
        print(f"R$ {tabela[i]:>6}")

print("#"*42)
print(f"\n{tabela[0]}.................. R$ {tabela[1]}")
print(f"{tabela[2]}.................. R$ {tabela[3]}")
print(f"{tabela[4]}.................. R$ {tabela[5]}")
print(f"{tabela[6]}.................. R$ {tabela[7]}")
