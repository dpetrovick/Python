print("\n## JOGADOR DE FUTEBOL ##\n")

jogador = {}
jogador["Nome"] = str(input("Informe o nome do jogador: ")).strip().capitalize()
jogador["Partidas"] = int(input("Informe quantas partidas ele disputou: "))
gols = []
soma_gol = 0
for i in range(0, jogador["Partidas"]):
    gol = int(input(f"Quantos gols ele fez na {i+1}º partida? "))
    soma_gol += gol
    gols.append(gol)

jogador["gols"] = gols
jogador["TotGols"] = soma_gol
print(jogador)
print("-=" * 30)
for k,v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print("-=" * 30)
print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas")
for i, v in enumerate(jogador["gols"]):
    print(f" ==> Na {i+1}º partida ele fez {v} gols")
print(f"{jogador['Nome']} fez um total de {jogador['TotGols']} gols")


