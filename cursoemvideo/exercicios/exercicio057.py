sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input("Informe o seu sexo (M ou F): ")).strip().upper()
    if sexo == "M":
        print("Você é do homem!")
    elif sexo == "F":
        print("Você é mulher!")
    else:
        print("Tente novamente!!")
