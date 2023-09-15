from random import choice

print("\n# JOGO DO PAR OU ÌMPAR #\n")
num_pc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cont = 0
while True:
    num_jog = int(input("Informe um número: "))
    opcaopc = choice(num_pc)
    soma = opcaopc + num_jog
    print("""Faça uma escolha. Digite:
    
    1 - PAR
    2 - ÍMPAR
    """)
    opcao = int(input("Sua opção é: "))

    if opcao == 1:
        if soma % 2 == 0:
            print(f"\nvocê: {num_jog} ; Computador: {opcaopc}, soma: {soma}")
            print(f"Deu Par, você GANHOU!  Vamos jogar outra vez!\n")
            cont += 1
        else:
            print(f"\nvocê: {num_jog} ; Computador: {opcaopc}, soma: {soma}")
            print(f"Deu ÍMPAR, você perdeu! Você teve {cont} vitórias consecutivas")
            break
    if opcao == 2:
        if soma % 2 == 1:
            print(f"\nvocê: {num_jog} ; Computador: {opcaopc}, soma: {soma}")
            print("Deu ÍMPAR, você GANHOU! Vamos jogar outra vez!\n")
            cont += 1
        else:
            print(f"\nvocê: {num_jog} ; Computador: {opcaopc}, soma: {soma}")
            print(f"Deu PAR, você PERDEU! Você teve {cont} vitórias consecutivas")
            break

print("\n -=- GAME OVER -=-")
