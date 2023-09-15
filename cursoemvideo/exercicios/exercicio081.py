print("\n## LISTA EM ORDEM DECRESCENTE ##\n")

lista = []

while True:
    lista.append(int(input("Digete um valor: ")))

    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja Continuar? S/N: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"A lista contem um total de {len(lista)} elementos")
lista.sort(reverse=True)
print(f"A lista em ordem decrescente é: {lista}")
if 5 in lista:
    print("O elemento 5 CONSTA na lista!")
else:
    print("O elemento 5 NÃO CONSTA na lista!")
