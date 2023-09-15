valor_real = float(input("\nInforme o valor da compra: "))
valor_desc = valor_real - (valor_real * 0.05)

print(f"O valor da compra foi: R${valor_real}. Com o desconto ficou: R${valor_desc:.2f}")


# Calculo da porcentagem também poderia ser: valor_desc = valor_real + (valor_real * 15 / 100)