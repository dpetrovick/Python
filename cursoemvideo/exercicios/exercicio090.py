print("\n## MÉDIA - DICIONÁRIO ##\n")
aluno = {}
aluno["nome"] = str(input("Informe o nome do aluno: ")).strip().capitalize()
aluno["media"] = float(input("Informe a média do aluno: "))
aluno["situacao"] = ""
if aluno["media"] < 5:
    aluno["situacao"] = "Reprovado"
elif 5 <= aluno["media"] < 7:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Aprovado"

print(f"O nome do aluno é: {aluno['nome']}")
print(f"A média do aluno é: {aluno['media']}")
print(f"A situação do aluno é: {aluno['situacao']}")
