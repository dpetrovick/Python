num1 = int(input("\nInforme um número: "))
num2 = int(input("Informe mais um número: "))
num3 = int(input("Informe o último número: "))

if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f"\nO maior número é: {maior}")
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f"O menor número é: {menor}\n")
