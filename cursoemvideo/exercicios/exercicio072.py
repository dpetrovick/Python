print("\n## NÚMERO POR EXENTENSO ##\n")

extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
           "treze", "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Informe o número: "))
    if 0 <= num <= 20:
        print(f"O numero digitado foi: {extenso[num]}")
        resp = " "
        while resp not in "SN":
            resp = str(input("Deseja Continuar? Digite S ou N: ")).strip().upper()[0]
        if resp == "N":
            break
    else:
        print("Tente novamente!", end=" ")

print("FIM")