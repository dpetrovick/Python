from random import randint

print("\n# ADVINHA EM QUE NÚMERO PENSEI? #\n")

'''num = int(input("Informe um número: "))
pc = randint(0, 10)
tentativas = 0

while num != pc:
    num = int(input("\nVocê errou, tente novamente. Informe um número: "))
    tentativas += 1
    if num == pc:
        print(f"\nParabéns, você acertou! Foram preciso {tentativas +1} tentativas para acertar. !")
    else:
        if num > pc:
            print("Menos...")
        elif num < pc:
            print("Mais...")
print("\nFIM")'''

# solução do professor

pc = randint(0, 10)
acertou = False
tentativas = 0

while acertou != True: # while not acertou: seria outra opção, inclusive sugerido pelo pycharm
    num = int(input("\nInforme um número: "))
    tentativas += 1
    if num == pc:
        acertou = True
        print(f"Parabéns você acertou!! Precisou de {tentativas} tentativas!!")
    else:
        if num > pc:
            print("Menos...")
        elif num < pc:
            print("Mais...")
print("\nFim do jogo, vamos jogar novamente?")






