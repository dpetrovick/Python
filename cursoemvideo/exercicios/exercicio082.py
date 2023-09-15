print("\n## LISTAS: GERAL, PAR E IMPAR ##\n")

lista = []
lpar = []
limpar = []

while True:
    lista.append(int(input("Informe um valor: ")))
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continaur? S/N ")).strip().upper()
    if resp == "N":
        break
print(f"A lista digitada é: {lista}")
for i in lista:
    if i % 2 == 0:
        lpar.append(i)
    else:
        limpar.append(i)
print(f"A lista PAR digitada é: {lpar}")
print(f"A lista ÍMPAR digitada é: {limpar}")
