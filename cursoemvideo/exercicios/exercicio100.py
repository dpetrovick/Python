from random import choice
from random import randint

print("\n## FUNÇÃO - SORTEIA E SOMA PARES ##\n")

'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = []


def sorteia():
    print("Os números sorteados foram: ", end="")
    for i in range(0, 5):
        num = choice(lista)
        numeros.append(num)
    print(numeros)


def somapar():
    soma = 0
    print("A soma dos números são: ", end="")
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(soma)


sorteia()
somapar()'''
#################################################################################################################


def sorteia(lista):
    print("os númros sorteados foram: ", end="")
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=" ")
    print()


def somapar(lista):
    soma = 0
    print(f"A soma dos valores pares da lista {lista} é: ", end="")
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma, end=" ")


num = []
sorteia(num)
somapar(num)
print()
