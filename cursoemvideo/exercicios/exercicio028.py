from random import randint
from time import sleep

num = int(input("\nInforme um número entre 0 e 5: "))
pc = randint(0, 5)
print("Calma aí...")
sleep(2)
if num == pc:
    print(f"PARABÉNS, VOCÊ ACERTOU!!! O número digitado foi {num} e o número escolhido pelo pc foi {pc}!!")
else:
    print(f"AHHH, VOCÊ ERROU!! O número digitado foi {num} e o número escolhido pelo pc foi {pc}!!")
