from random import choice
from time import sleep

# CABEÇALHO
print("\n")
print("\033[1:33:40m-=\033[m" * 45)
print("\033[1:33:40m-=-\033[m", "\033[1:33:40m-=-\033[m".rjust(99))
print("\033[1:33:40m-=-\033[m", f"\033[1:33:40m JOKENPÔ  -  PEDRA / PAPEL / TESOURA \033[:m".center(96),
      "\033[1:33:40m-=-\033[m".rjust(6))
print("\033[1:33:40m-=-\033[m", "\033[1:33:40m-=-\033[m".rjust(99))
print("\033[1:33:40m-=\033[m" * 45, "\n")
#######################################################################################

print(f"""  VAMOS COMEÇAR!!!

  Faça sua escolha...

\033[1:33:40m 1 - PEDRA   \033[m
\033[1:33:40m 2 - PAPEL   \033[m
\033[1:33:40m 3 - TESOURA \033[m""")

opcao = int(input("\nEscolha uma opção: "))

print(f"\nJO...")
sleep(1)
print("KEN...")
sleep(1)
print("Pô!!")
sleep(1)

pc = ["PEDRA", "PAPEL", "TESOURA"]
opcaopc = choice(pc)
if opcao == 1 and opcaopc == pc[0]:
    print(f"\nVocê: PEDRA \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mEMPATE: PEDRA = {opcaopc}!\033[m")
elif opcao == 1 and opcaopc == pc[1]:
    print(f"\nVocê: PEDRA \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mVOCÊ PERDEU: O {opcaopc} embrulha a PEDRA!\033[m")
elif opcao == 1 and opcaopc == pc[2]:
    print(f"\nVocê: PEDRA \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mVOCÊ VENCEU: A PEDRA amassa a {opcaopc}!\033[m")

elif opcao == 2 and opcaopc == pc[0]:
    print(f"\nVocê: PAPEL \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mVCCÊ VENCEU: O PAPEL embrulha a {opcaopc}!\033[m")
elif opcao == 2 and opcaopc == pc[1]:
    print(f"\nVocê: PAPEL \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mEMPATE: PAPEL = {opcaopc}!\033[m")
elif opcao == 2 and opcaopc == pc[2]:
    print(f"\nVocê: PAPEL \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mVOCÊ PERDEU: A {opcaopc} corta o PAPEL!\033[m")

elif opcao == 3 and opcaopc == pc[0]:
    print(f"\nVocê: TESOURA \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mVOCÊ PERDEU: A {opcaopc} amassa a TESOURA!\033[m")
elif opcao == 3 and opcaopc == pc[1]:
    print(f"\nVocê: TESOURA \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mVOCÊ VENCEU: A TESOURA corta o {opcaopc}!\033[m")
elif opcao == 3 and opcaopc == pc[2]:
    print(f"\nVocê: TESOURA \nComputador: {opcaopc} ")
    print(f"\n\033[1:33:40mEMPATE: TESOURA = {opcaopc}!\033[m")
else:
    print("\nOpção inválida!!")

print("\nVAMOS JOGAR OUTRA VEZ!! ")
