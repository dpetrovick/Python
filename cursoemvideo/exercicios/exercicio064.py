print("\n # SOMANDO NÚMEROS ATÉ PEDIR PARA PARA!! #\n")

num = int(input("Digite um número qualquer para ter a soma no final, para sair digite 999: "))
soma = 0
cont = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número qualquer para ter a soma no final, para sair digite 999: "))
print(f"Você digitou {cont} números e a soma entre eles é {soma}!!")
