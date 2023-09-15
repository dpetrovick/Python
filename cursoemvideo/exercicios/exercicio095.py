print("\n## APRIMORANDO EXERCÍCIO 93 ##\n")

time = []
jogador = {}
gols = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input("Informe o nome do jogador: ")).strip().capitalize()
    jogador['Jogos'] = int(input(f"Informe quantos jogos o jogador {jogador['Nome']} fez: "))
    soma_gol = 0
    for i in range(0, jogador['Jogos']):
        gol = (int(input(f"Informe quantos gols o jogador {jogador['Nome']} fez no {i+1}º jogo: ")))
        soma_gol += gol
        gols.append(gol)
    jogador['Gols'] = gols[:]
    gols.clear()
    jogador['TotGols'] = soma_gol
    time.append(jogador.copy())

    while True:
        resp = str(input("Deseja cadastrar outro jogador? (S ou N): ")).upper()
        if resp in "SN":
            break
        print("Por favor, digite apenas 'S' ou 'N'!! ")
    if resp == "N":
        break
print("-="*30)
print(" Código  ", end="")
for i in jogador.keys():
    print(f"{i:<12} ", end="")
print()
print("-="*30)
for k, v in enumerate(time):
    print(f"{k:>5} ", end="   ")
    for d in v.values():
        print(f"{str(d):<12}", end="  ")
    print()
print("-="*30)
while True:
    busca = int(input("Informe o código do jogador que deseja consultar (999 para sair): "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Não existe jogador cadastrado com este código!!")
    else:
        print(f"Segue abaixo os dados do jogador {time[busca]['Nome']}:")
        for k, v in time[busca].items():
            print(f"{k} = {v}")
