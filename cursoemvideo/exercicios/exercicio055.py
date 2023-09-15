print("\n MAIOR E MENOR PESO # \n")

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Informe o peso da {i}ª pessoa: "))
    if i == 1: # no primeiro laço os dois valores são iguais, pois só foi informado um valor.
        maior = peso
        menor = peso
    else: # a partir daqui ele compara os seguintes valores com os novos imputados
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso informado foi: {maior}Kg\nO menor peso informado foi: {menor}Kg")
