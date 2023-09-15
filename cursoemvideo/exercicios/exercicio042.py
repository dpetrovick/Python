# CABEÇALHO
print("\n")
print("\033[1:31:40m-=\033[m" * 45)
print("\033[1:31:40m-=-\033[m", "\033[1:31:40m-=-\033[m".rjust(99))
print("\033[1:31:40m-=-\033[m", f"\033[1:31:40m TRIÂNGULOS: EQUILÁTERO / ESCALENO / ISÓCELES \033[:m".center(96),
      "\033[1:31:40m-=-\033[m".rjust(6))
print("\033[1:31:40m-=-\033[m", "\033[1:31:40m-=-\033[m".rjust(99))
print("\033[1:31:40m-=\033[m" * 45, "\n")
#######################################################################################

reta1 = int(input("Informe o valor da primeira reta: "))
reta2 = int(input("Informe o valor da segunda reta:  "))
reta3 = int(input("Informe o valor da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
      if reta1 == reta2 == reta3:
            print(f"\nAs retas {reta1}, {reta2}, {reta3} formam um TRIÂNGULO EQUILÁTERO (TODOS LADOS IGUAIS)!!")

      elif reta1 != reta2 != reta3 != reta1:
            print(f"\nAs retas {reta1}, {reta2}, {reta3} formam um TRIÂNGULO ESCALENO (TODOS OS LADOS DIFERENTES)!!")

      else:
            print(f"\nAs retas {reta1}, {reta2}, {reta3} formam um TRIÂNGULO ISÓCELES (DOIS LADOS IGUAIS E UM DIFERENTE)"
                  f"!!")
else:
      print(f"\nAs retas {reta1}, {reta2}, {reta3} NÃO FORMAM UM TRIÂNGULO!!")
