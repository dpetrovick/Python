from math import hypot

cateto1 = float(input("\nInforme o valor do cateto oposto: "))
cateto2 = float(input("Informe o valor do cateto adjacente: "))
# hipotenusa = hypot(cateto1, cateto2), caso quizesse salver em uma variável.
# hipotenusa = ((cateto1 * cateto1) + (cateto2 * cateto2)) ** (1/2) - sem o import.
print(f"O valor da hipotenusa é: {hypot(cateto1, cateto2):.2f}")


# hipotenusa = sqrt(cateto1 * cateto1 + cateto2 * cateto2), neste cado tem que importar a função "sqrt"