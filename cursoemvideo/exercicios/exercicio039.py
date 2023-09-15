from datetime import date

# CABEÇALHO2
print("\n")
print("-=" * 45)
print("\033[1:30:42m-=-\033[m", "\033[1:30:42m-=-\033[m".rjust(99))
print("\033[1:30:43m-=-\033[m", f"\033[1:30:43m ALISTAMENTO MILITAR \033[:m".center(96),
      "\033[1:30:43m-=-\033[m".rjust(6))
print("\033[1:30:42m-=-\033[m", "\033[1:30:42m-=-\033[m".rjust(99))
print("-=" * 45, "\n")
#######################################################################################

ano = int(input("Informe o ano do seu nascimento: "))
sexo = str(input("Informe o seu sexo (M ou F): ")).upper()
idade = date.today().year - ano

if sexo == "M":
      print("\nVócê é do sexo masculino, Seu alistamento é obrigatório!!\n")
      print(f"Você nasceu em {ano}, tem ou terá {idade} anos neste ano, {date.today().year}.")
      if idade < 18:
            print(f"Ainda faltam {18 - idade} ano(s) para o seu alistamento.")
            print(f"Seu alistamento será no ano {(18 - idade) + date.today().year}.")
      elif idade > 18:
            print(f"Você perdeu o prazo do seu alistamento. Ele deveria ter ocorrido há {idade - 18} ano(s)! ")
            print(f"Seu alistamento deveria ter ocorrido no ano {date.today().year - (idade - 18)}!!")
      else:
            print(f"Você tem ou terá 18 anos este ano. Se aliste IMEDIATEMENTE!!")
else:
      print("Você é do sexo feminino e está dispensada do alistamento obrigatório.")
