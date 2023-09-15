from random import shuffle
# shuffle embaralha o conteúdo da variável

aluno1 = input("\nInforme o nome do 1º aluno: ")
aluno2 = input("Informe o nome do 2º aluno: ")
aluno3 = input("informe o nome do 3º aluno: ")
aluno4 = input("Informe o nome do 4º aluno: ")
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f"A ordem de apresentação sera: {alunos}")


