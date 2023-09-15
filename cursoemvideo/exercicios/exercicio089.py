print("\n## BOLETIM DOS ALUNOS ##\n")

boletim = []
ltemp = []
media = 0
while True:
    nome = str(input("Informe o nome do aluno: ")).strip().capitalize()
    nota1 = (float(input("Informe a 1ª nota: ")))
    nota2 = (float(input("Informe a 2ª nota: ")))
    media = (nota1 + nota2) / 2
    ltemp.append(nome)
    ltemp.append(nota1)
    ltemp.append(nota2)
    ltemp.append(media)
    boletim.append(ltemp[:])
    ltemp.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja inserir mais um aluno, S ou N? ")).strip().upper()
    if resp == "N":
        break
print("-=" * 20)
print(f"{'Nº':<4}{'Nome':<10}{'Média':>8}")
for i, v in enumerate(boletim):
    print(f"{i:<4}{v[0]:<10}{v[3]:>8.1f}")
print()
print("-=" * 20)
print()
while True:
    aluno = int(input("Informe que aluno deseja consultar (Digite 999 para encerrar): "))
    if aluno == 999:
        print("Fim da consulta")
        break
    if aluno <= len(boletim) - 1:
        print(f"As notas de {boletim[aluno][0]} são: {boletim[aluno][1:3]}")
