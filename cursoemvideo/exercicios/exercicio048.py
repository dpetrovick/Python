print("\nSOMANDO NÚMEROS ÍMPARES MÚLTIPLOS DE 3, DE 1 ATÉ 500!!\n")

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print(f"Existem {cont} números múltiplos de 3 compreendidos entre 1 e 500. A soma deles é: {soma}")

# um contador conta ele +1
# Um acumulador é a soma da interação
