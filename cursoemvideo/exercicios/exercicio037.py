# CABEÇALHO
print("\n")
print("-=" * 45)
print("\033[1:30:43m-=-\033[m", "\033[1:30:43m-=-\033[m".rjust(99))
print("\033[1:30:41m-=-\033[m", f"\033[1:30:41m CONVERSÃO: BINÁRIO / HEXADECIMAL / OCTAL \033[:m".center(96),
      "\033[1:30:41m-=-\033[m".rjust(6))
print("\033[1:30:43m-=-\033[m", "\033[1:30:43m-=-\033[m".rjust(99))
print("-=" * 45, "\n")
#######################################################################################

num = int(input("\nInforme um número inteiro para converter: "))
print("\nEscolha as seguintes opções: \n")
print("\033[1:44m1 - BINARIO     \033[m")
print("\033[1:43m2 - OCTAL       \033[m")
print("\033[1:42m3 - HEXADECIMAL \033[m")
opcao = int(input("\nOPÇÃO: "))

if opcao == 1:
      print(f"O número \033[35m{num}\033[m em BINÁRIO é: \033[4:34m{bin(num)[2:]}\033[m!")
elif opcao == 2:
      print(f"O número \033[35m{num}\033[m em OCTAL é: \033[4:33m{oct(num)[2:]}\033[m!")
elif opcao == 3:
      print(f"O número \033[35m{num}\033[m em HEXADECIMAL é: \033[4:32m{hex(num)[2:]}\033[m!")
else:
      print("\n\033[1:7mValor inválido. Tente novamente!!\033[m")

# Outra forma: print(f"O número {num} em BINÁRIO é: {str(bin(num)).lstrip('0b')}!")
# str(bin(num) - De dentro pra fora: Recebe um número (num) converte em binario(bin) e depois converte em string(str)
# lstrip('0b') - Retira da esquerda da string o caracteres 0b pq aparece assim: binario de 10 = ob1010 (resp = 1010)
