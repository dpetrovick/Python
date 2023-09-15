# CABEÇALHO
print("\n")
print("-=" * 45)
print("\033[1:30:45m-=-\033[m", "\033[1:30:45m-=-\033[m".rjust(99))
print("\033[1:30:43m-=-\033[m", f"\033[1:33:45m CÁLCULO DA MÉDIA DO ALUNO \033[:m".center(96),
      "\033[1:30:43m-=-\033[m".rjust(6))
print("\033[1:30:45m-=-\033[m", "\033[1:30:45m-=-\033[m".rjust(99))
print("-=" * 45, "\n")
#######################################################################################

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(f"\n Sua média foi {media}. Você foi REPROVADO!! Estude mais e até ano que vem !!")
elif 5 <= media < 7:
    print(f"\nSua média foi {media}. Você está em RECUPERAÇÃO, nem tudo está perdido!!!")
else:
    print(f"\nSua média é {media}. PARABÉNS, VOCÊ ESTÁ APROVADO!! CURTA SUA MERECIDAS FÉRIAS!!")
