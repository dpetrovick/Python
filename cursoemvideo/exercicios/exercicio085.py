print("\n## PARES E IMPAR EM LISTAS ##\n")

geral = [[], []]

for i in range(1, 8):
    numero = int(input(f"Informe o {i}º número: "))
    if numero % 2 == 0:
        geral[0].append(numero)
    else:
        geral[1].append(numero)
print(f"Os números digitados foram: {geral}")
# geral[0].sort() - Outra forma de ordenar.
# geral[1].sort() - Outra forma de ordenar.
print(f"Os números pares, em ordem crescente são: {sorted(geral[0])}")
print(f"Os números impares, em ordem crescente são: {sorted(geral[1])}")
# print(f"A lista completa é: {geral[0] + geral[1]}") - Se eu quizesse mostrar uma lista única com os valores digitados
