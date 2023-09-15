from time import sleep

print("\n# MAIOR E MENOR VALORES #\n")

'''num = soma = media = cont = 0
opcao = "S"
maior = 0
menor = 999999
while opcao != "N":
    num = float(input("Informe um número: "))
    # Capturado maior e menor
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1

    opcao = str(input("Deseja continuar S/N ? ")).strip().upper()
    if opcao == "S":
        soma += num
        media = soma / cont
    elif opcao == "N":
        print(f"O maior número foi {maior} e o menor foi {menor}")
        print(f"A média entre todos os {cont} números é: {media}")
print("saindo...")
sleep(2)
print("\nPrograma encerrado!\n")
'''
opcao = "S"
media = soma = cont = 0
maior = menor = 0
while opcao =="S":
    num = float(input("Digite um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    opcao = str(input("Quer continur (S / N)? ")).strip().upper()
    if opcao != "S" and opcao != "N":
        opcao = str(input("Opção errada!! Digite apenas 'S' ou 'N' ")).strip().upper()
media = soma / cont
print(" \n# Gerando Relatório #...\n")
sleep(2)
print("=x"* 30)
print(f"Foram digitados {cont} números")
print(f"O maior número digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")
print(f"A média aritimética dos números digitados é: {media:.2f}")
print("=x"* 30)

print("\nPrograma Encerrado!")
