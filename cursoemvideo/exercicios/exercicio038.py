# CABEÇALHO
print("\n")
print("-=" * 45)
print("\033[1:30:44m-=-\033[m", "\033[1:30:44m-=-\033[m".rjust(99))
print("\033[1:30:45m-=-\033[m", f"\033[1:30:45m LENDO DOIS NÚMEROS E COMPARANDO-OS \033[:m".center(96),
      "\033[1:30:45m-=-\033[m".rjust(6))
print("\033[1:30:44m-=-\033[m", "\033[1:30:44m-=-\033[m".rjust(99))
print("-=" * 45, "\n")
#######################################################################################

num1 = int(input("\nInforme o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 > num2:
    print(f"\nO PRIMEIRO número digitado é o MAIOR: {num1}")
elif num2 > num1:
    print(f"\nO SEGUNDO número digitado é o MAIOR: {num2}")
else:
    print(f"\nOs números {num1} e {num2} são IGUAIS!!")
