print("\n# FIBONACCI #\n")

num = int(input("Informe a quantidade de termos que deseja mostrar: "))
termo1 = 0 # Primeiro termo da Fibonacci (Fixo)
termo2 = 1 # Segundo termo da Fibonacci (Fixo)
cont = 3 # Conta a partir do 3 termo porque 1º e o 2º já estão definidos.
print(f"{termo1} --> {termo2}", end=" --> ")
while cont <= num:
    termo3 = termo1 + termo2
    print(termo3, end=" --> ")
    termo1 = termo2 # Faz o termo anterior ser atualizado com o valor do próximo para que a senquencia possa "andar"
    termo2 = termo3
    cont += 1
print("FIM")
