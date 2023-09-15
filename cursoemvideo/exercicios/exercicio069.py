print("\n# MINE SENSO IBGE #\n")
cont_m = cont_f = 0
cont_idade = cont_idade_f = 0
while True:
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Informe o sexo da pessoa. Digite M para Maculino e F para Feminino: ")).strip().upper()[0]
    if sexo == "M":
        idade = int(input("Informe a idade da pessoa: "))
        cont_m += 1
    else:
        idade = int(input("Informe a idade da pessoa: "))
        cont_f += 1

    sair = " "
    while sair not in "SN":
        sair = str(input("Deseja sair? Digite S para SIM e N para NÃO: ")). strip().upper()[0]
    if sair == "N":
        if idade > 18:
            cont_idade += 1
        if sexo == "F" and idade < 20:
            cont_idade_f += 1
    else:
        print(f"\nForam cadastradas {cont_idade} pessoas maiores de 18 anos")
        print(f"Foram cadastrados {cont_m} Homens")
        print(f"Foram cadastradas {cont_idade_f} mulheres menores de 20 anos\n")
        break
print("### FIM DO MINI SENSO IBGE ###")



