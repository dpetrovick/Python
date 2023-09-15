from time import sleep
print("\n#CRIAÇÃO DE MENU #\n")

somar = 0
multiplicar = 0
maior = 0
sair = False
# opcao = 0

valor1 = int(input(f"informe o 1º valor: "))
valor2 = int(input(f"informe o 2º valor: "))


while not sair: # while opcao != 5:
    print("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    opcao = int(input("\nInforme sua opção de acordo ao menu acima: "))
    if opcao == 1:
        somar = valor1 + valor2
        print(f"\n\033[1:30:42mA soma entre {valor1} e {valor2} é: {somar}\033[m")
        print("-=" * 25)
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print(f"\n\n\033[1:30:42mA multiplicação entre {valor1} e {valor2} é: {multiplicar}\033[m")
        print("-=" * 25)
    elif opcao == 3:
        if valor1 > valor2:
            print(f"\n\033[1:30:42mO maior valor entre {valor1} e {valor2} é: {valor1}\033[m")
            print("-=" * 25)
        elif valor1 < valor2:
            print(f"f\n\033[1:30:42mO maior valor entre {valor1} e {valor2} é:{valor2}\033[m")
            print("-=" * 25)
        else:
            print(f"\n\033[1:30:42mOs valores {valor1} e {valor2} são iguais!\033[m")
            print("-=" * 25)
    elif opcao == 4:
        valor1 = int(input("\nInforme um novo 1º valor: "))
        valor2 = int(input("Informe um novo 2º valor: "))
    elif opcao == 5:
        sair = True
print("\nSaindo...")
sleep(2)
print("\nFIM!!")
