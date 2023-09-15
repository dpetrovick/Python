from datetime import datetime
print("\n## CADASTRO DE FUNCIONÁRIO ##\n")

trabalhador = {}
trabalhador["Nome"] = str(input("Informe o nome do funcionário: ")).strip().title()
trabalhador["Sexo"] = str(input("Informe o sexo do funcionário [M ou F]: ")).strip().upper()[0]
ano_nac = int(input(("Informe o ano de nascimento: ")))
trabalhador["Idade"] = datetime.now().year - ano_nac
trabalhador["CTPS"] = int(input("Informe o número da CTPs do funcioário (caso não tenha digite 0): "))

if trabalhador["CTPS"] != 0:
    trabalhador["Admissao"] = int(input("Informe o ano de admissão do funcionário: "))
    trabalhador["Salario"] = float(input("Informe o salário do funcionário: R$"))
    trabalhador["aposenta"] = trabalhador["Idade"] + ((trabalhador["Admissao"] + 35) - datetime.now().year)
for k, v in trabalhador.items():
    print(f" - {k}: {v} ")