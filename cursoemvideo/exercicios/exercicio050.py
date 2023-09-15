print("\nSOMA DE 6 NÚMEROS PARES\n")

soma = 0
pares = []

for i in range(1, 7):
    num = int(input("Informe um número: "))
    if num % 2 == 0:
        pares.append(num)
        soma += num

print(f"\nOs números pares digitados são: {pares} e a soma deles é: {soma}")
