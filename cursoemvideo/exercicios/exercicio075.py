print("\n## ANÁLISE DE TUPLAS ##\n")

num1 = int(input("Informe um numero: "))
num2 = int(input("Informe um numero: "))
num3 = int(input("Informe um numero: "))
num4 = int(input("Informe um numero: "))
tupla = (num1, num2, num3, num4)
print(f"\n{tupla}")

if 9 in tupla:
    print(f"O numero 9 aparece {tupla.count(9)} vezes!")
else:
    print("O número 9 não existe na tupla")
if 3 in tupla:
    print(f"O número 3 aparece na {tupla.index(3)+1}ª posição")
else:
    print("O numero 3 não existe na tupla")

print("Os numeros pares são:", end=" ")
for i in tupla:
    if i % 2 == 0:
        print(f"{i}", end=", ")
print("Fim")
