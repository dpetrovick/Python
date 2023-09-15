print("#\n CALCULANDO A SOMA E QUANTIDADE #\n")

soma = 0
cont = 0
while True:
    num = int(input("Informe um número: "))
    print("Para sair digite 999")
    if num == 999:
        break
    soma += num
    cont += 1
print(f"\nA quantidade de números digitados foi {cont} e a soma deles é: {soma}!!")
