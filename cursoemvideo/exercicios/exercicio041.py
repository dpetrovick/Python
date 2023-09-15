from datetime import date

# CABEÇALHO
print("\n")
print("-=" * 45)
print("\033[1:30:44m-=-\033[m", "\033[1:30:44m-=-\033[m".rjust(99))
print("\033[1:30:46m-=-\033[m", f"\033[1:30:46m CATEGORIAS DE ATLETAS - NATAÇÃO \033[:m".center(96),
      "\033[1:30:46m-=-\033[m".rjust(6))
print("\033[1:30:44m-=-\033[m", "\033[1:30:44m-=-\033[m".rjust(99))
print("-=" * 45, "\n")
#######################################################################################

nasc = int(input("Informe o ano dos nascimento do atleta: "))
ano = date.today().year
idade = ano - nasc

if idade < 10:
      print(f"\nA catergotia do atleta é: MIRIM. Ele possui {idade} anos e a faixa é até 9 anos.")
elif idade < 15:
      print(f"\nA catergotia do atleta é: INFANTIL. Ele possui {idade} anos e a faixa é até 14 anos.")
elif idade < 20:
      print(f"\nA catergotia do atleta é: JÚNIOR. Ele possui {idade} anos e a faixa é até 19 anos.")
elif idade < 26:
      print(f"\nA catergotia do atleta é: SÊNIOR. Ele possui {idade} anos e a faixa é até 25 anos.")
else:
      print(f"\nA catergotia do atleta é: MASTER. Ele possui {idade} anos e a faixa é acima de 25 anos.")
