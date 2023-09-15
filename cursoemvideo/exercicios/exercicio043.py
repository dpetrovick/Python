# CABEÇALHO
print("\n")
print("\033[1:40m-=\033[m" * 45)
print("\033[1:40m-=-\033[m", "\033[1:40m-=-\033[m".rjust(96))
print("\033[1:40m-=-\033[m", f"\033[1:40m IMC - ÍNDICE DE MASSA CORPORAL \033[:m".center(93),
      "\033[1:40m-=-\033[m".rjust(6))
print("\033[1:40m-=-\033[m", "\033[1:40m-=-\033[m".rjust(96))
print("\033[1:40m-=\033[m" * 45, "\n")
#######################################################################################

peso = float(input("Informe o seu peso: "))
altura = float(input("informe a sua altura: "))
imc = peso / altura ** 2

if imc < 18.5:
    print(f"Seu IMC é: {imc:.2f}. Você está na capa do batman!!")
elif imc < 25:
    print(f"Seu IMC é: {imc:.2f}. Você está no shape!!")
elif imc < 30:
    print(f"Seu IMC é: {imc:.2f}. Você está roliço(a)!!")
elif imc < 40:
    print(f"Seu IMC é: {imc:.2f}. Go Willy!!")
else:
    print(f"Seu IMC é: {imc:.2f}. Chama o guindaste!!")
