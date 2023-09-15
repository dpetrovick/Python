cidade = str(input("\n Informe o nome de uma cidade: "))
teste = (cidade.lower().find("santo"))
if teste == 0:
    print(f"\nA cidade digitada {cidade} começa com o nome 'Santo'!")
else:
    print(f"\nA cidade digitada {cidade} NÃO começa com o nome 'Santo'!")


# Solução do professor

cidade2 = str(input("\nInforme se o nome de uma cidade: ")).strip() # .strip() retira os espaços do início e fim
print(f"\n{cidade2[:5].upper() == 'SANTO'}") # Compara se as 5 primeiras letras são iguais a 'SANTO'.

