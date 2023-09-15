print("\n## LISTA DE VALORES NA ORDEM CRESCENTE ##\n")

lista = []
while True:
    num = int(input("Digite um numero: "))
    if num not in lista:
        lista.append(num)

    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja digitar mais algum numero? S/N: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"\nSua lista é ordenada é: {sorted(lista)}")
