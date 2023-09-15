print("\n## FUNÇÃO - MAIOR VALOR ##\n")


def Maior(*num):
    cont = maior = 0
    print("-"*25)
    print("ANALISANDO OS NÚMEROS...")
    for i in num:
        print(f"{i} ", end="")
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f"Foram informados {cont} números e o maior é {maior}!!")



#   PROGRAMA PRINCIPAL
Maior(2,4,6,9,5,8)
Maior(7,4,2)
Maior(8)
Maior()