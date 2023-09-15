print("\n# SUPER PROGRESSÃO ARITIMÉTICA #\n")

num = int(input("Informe o número: "))
raz = int(input("Informe a Razão: "))
qtd = 10
cont = 1
fase2 = 1
while fase2 != 0:
    while cont <= qtd:
        print(num,  end=" --> ")
        num += raz
        cont += 1
    print("FIM")
    fase2 = int(input("Informe quantos termos gostaria de adicionar a PA, 0 para sair: "))
    if fase2 != 0:
        adiciona = fase2
        qtd += adiciona
print(f"\nPrograma encerrado com {cont - 1} termos !!")
