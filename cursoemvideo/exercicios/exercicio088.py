from random import randint
from time import sleep
print("\n## MEGA SENA ##\n")

palpites = []
mega = []
cont = 0
jogos = int(input("Informe a quantidade de jogos que desaja fazer: "))
print()
print("-=" * 19)
print()
while cont < jogos:
    for i in range(0, 6):
        numeros = randint(1, 60)
        if numeros not in palpites:
            palpites.append(numeros)
    # print(palpites) mostra os palpites a cada "rodada".
    mega.append(palpites[:])
    cont += 1
    palpites.clear()
print("-=" * 5, "SORTEANDO NÚMEROS", "-=" * 5)
sleep(1)
for i, l in enumerate(mega):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
