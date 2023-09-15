print("\n## LISTAS ##\n")

lista = []
maior = menor = 0

for i in range(0, 5):
    lista.append(int(input("Informe um valor: ")))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print("=-"*30)
print(f"A sua lista é: {lista}")
print(f"O maior numero da lista é {maior} na(s) posição(ões) ", end="")
for c, v in enumerate(lista):
    if v == maior:
        print(c, end=" ")
print("")
print(f"O menor numero da lista é {menor} na(s) posição(ões) ", end="")
for c, v in enumerate(lista):
    if v == menor:
        print(c, end=" ")

