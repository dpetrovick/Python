print("\n ANÁLISE - NOME / IDADE / SEXO #")


soma_idade = 0 # soma as idades
maior_idade_m = 0 # Idade do homem mais Velho
media_idade = 0 # Calcula a média da idade das pessoas do grupo
nome_maior = " " # Nome do homem mais velho
soma_idade_f = 0 # Soma a idade das mulheres
cont_mulher = 0 # conta quantas mulheres tem menos de 20 anos

for i in range (1, 7):
    print("\n")
    print(f"Dados da {i}º pessoa:")
    nome = str(input(f"Informe o nome: ")).upper()
    idade = int(input(f"Informe a idade: "))
    sexo = str(input("Informe o sexo (M OU F): ")).upper()

    soma_idade += idade
    if sexo == "M":
        if i == 1:
            maior_idade_m = idade
            nome_maior = nome
        else:
            if idade > maior_idade_m:
                maior_idade_m = idade
                nome_maior = nome
    elif sexo == "F":
        if idade < 20:
            soma_idade_f += idade
            cont_mulher += 1
    else:
        print("\nSexo inexistente!!")

media_idade = soma_idade / 4
print(f"\nA média de idade do grupo é: {media_idade}")
print(f"O homem mais velho é {nome_maior} e ele tem {maior_idade_m}")
print(f"Existem {cont_mulher} mulheres com menos de 20 anos. A soma da idade delas é: {soma_idade_f}")
