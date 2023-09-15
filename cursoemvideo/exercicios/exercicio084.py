print("\n ## LISTAS PARTE 2: ANÁLISE PESO DAS PESO ##\n")

pessoas = []
pessoa = []
pesadas = leves = 0
while True:
    nome = (str(input("Informe o nome da pessoa: "))).capitalize()
    pessoa.append(nome)
    pessoa.append(float(input("Informe o peso da pessoa: ")))
    if len(pessoas) == 0:
        pesadas = pessoa[1]
        leves = pessoa[1]
    else:
        if pessoa[1] > pesadas:
            pesadas = pessoa[1]
        if pessoa[1] < leves:
            leves = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja contnuar? S ou N: ")).strip().upper()
    if resp == "N":
        break
print(f"\n{pessoas}")
print(f"Foram cadastradas {len(pessoas)} pessoas!")
print(f"A(s) pessoa(s) mais pesada(s) é(são): ", end="")
for p in pessoas:
    if p[1] == pesadas:
        print(f"{p[0]}", end=" ")
print()
print(f"A(s) pessoa(s) mais leves(s) é(são): ", end="")
for p in pessoas:
    if p[1] == leves:
        print(f"{p[0]}", end=" ")
