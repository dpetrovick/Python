# CABEÇALHO
print("\n")
print("-=" * 45)
print("\033[1:30:46m-=-\033[m", "\033[1:30:46m-=-\033[m".rjust(99))
print("\033[1:30:42m-=-\033[m", f"\033[1:30:42m FINANCIAMENTO DA CASA PRÓPRIA \033[:m".center(96),
      "\033[1:30:42m-=-\033[m".rjust(6))
print("\033[1:30:46m-=-\033[m", "\033[1:30:46m-=-\033[m".rjust(99))
print("-=" * 45, "\n")
#######################################################################################

val_casa = float(input("Informe o valor da casa que deseja adquirir: "))
renda = float(input("Informe a sua renda mensal: "))
tempo = int(input("Informe o tempo em anos que deseja concluir o fianciamento: "))

prestacao = (val_casa / tempo) / 12
# 1 ano  = 12 meses, por isso "/ 12"
prestacao_Max = renda * (30 / 100)
if prestacao > prestacao_Max:
    print("\nPrestação superior a 30% da sua renda. O financiamento foi NEGADO!!")
else:
    print("\nFianciamento APROVADO!!")

print(f"\nA prestação ficou em R${prestacao:.2f} e o valor máximo para ser aprovado é R${prestacao_Max:.2f} !! ")
