print("\n## LISTA DE VOGAIS ##\n")

palavras = ("DEUS", "JESUS", "ESPITO SANTO", "OBEDIENCIA", "AMOR", "SALVACAO", "CRUZ", "PERDAO", "DEDICACAO", "BIBLIA")
for i in palavras:
    print(f"\nA palavra {i} tem as seguintes vogais: ", end="")
    for letra in i:
        if letra in "AEIOU":
            print(letra, end=" ")
print("\nFIM")
