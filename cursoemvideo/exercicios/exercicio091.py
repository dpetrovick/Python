from random import randint
from time import sleep
from operator import itemgetter
print("\n## JOGANDO DADOS ##\n")

jogo = {"Jogador 1": randint(1, 6), "Jogador 2": randint(1, 6), "Jogador 3": randint(1, 6), "Jogador 4": randint(1, 6)}
ranking = {} # Para se ordenar um dicionário é preciso criar outro vazio para receber a ordenação.
print("-=" * 20)
print(f"Dados sorteados!".center(35))
print("-=" * 20)
for k, v in jogo.items():
    print(f"O {k} tirou {v} nos dado!")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"O {i+1}º lugar ficou com {v[0]} que fez {v[1]} pontos!")
    sleep(1)
