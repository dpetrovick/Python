print("\n## fUNÇÃO - FICHA DE JOGADOR ##\n")


def ficha(nome="Desconhecido", gols=0):
    print(f"O jogador {nome}, fez {gols} gol(s)")


# PROGRAMA PRINCIPAL

jog_nome = str(input("Informe o nome do jogador: ")).capitalize()
jog_gols = str(input(f"Informe quantos gols o jogador {jog_nome} fez gols "))
if jog_gols.isnumeric():# para saber se o valor digitado é um número.
    jog_gols = int(jog_gols)
else:
    jog_gols = 0
if jog_nome.strip() == "":
    ficha(gols=0)
else:
    ficha(jog_nome, jog_gols)


