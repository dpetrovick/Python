from random import randint
print("\n## MAIOR E MENOR VALOR DE UMA TUPLA ##\n")

tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
# tambeém poderia fazer assim: a = tuple(sample(range(10), 5)) - vai gerar uma tupla com 5 aleatórios de 0 a 10
print(tupla)

print(f"O maior valor é: {max(tupla)}")
print(f"O menor valor é: {min(tupla)}\n")
print("{:#^40}".format(" Usando ordenação "))
print(f"\nO maior Valor é: {sorted(tupla)[4]}")
print(f"O menor valor é: {sorted(tupla)[0]}")

''' se eu quiser escrever o resultado sem os parênteses...
for i in tupla:
    print(i, end=" ")'''

