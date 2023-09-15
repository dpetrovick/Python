print("\n## CADASTRO DE PESSOAS ##\n")

pessoas = []
pessoa = {}
tot_idade = med_idade = 0
while True:
    pessoa['Nome'] = str(input("Informe o nome: ")).strip().capitalize()
    while True:
        pessoa['Sexo'] = str(input(f"Informe o sexo de {pessoa['Nome']}(M ou F): ")).upper()
        if pessoa['Sexo'] in "MF":
            break
        print("Por favor, digite apenas M ou F!")
    pessoa['Idade'] = int(input(f"Informe a idade de {pessoa['Nome']}: "))
    tot_idade += pessoa['Idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input("Deseja continuar? Digite S ou N: ")).upper()
        if resp in "SN":
            break
        print("Por favor, digite apenas S ou N!")
    if resp == "N":
        break
print("-="*30)
for i in pessoas:
    print(i)
print("-="*30)
print(f"Foram cadastradas {len(pessoas)} pessoas")
print("-="*30)
med_idade = tot_idade / len(pessoas)
print(f"A média de idade das pessoas cadastradas é de {med_idade} anos.")
print("-="*30)
print("As pessoas do sexo feminino é(são): ")
for i in pessoas:
    if i['Sexo'] == "F":
        print(i['Nome'])
print("-="*30)
print("A(s) pessoa(s) com idade acima da média é(são): ")
for i in pessoas:
    if i['Idade'] >= med_idade:
        print(f"{i['Nome']} com {i['Idade']} anos")
print("-="*30)
print("\nFIM DO PROGRAMA!!\n")
