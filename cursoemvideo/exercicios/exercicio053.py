print("\n # DETECTOR DE PALÍNDROMOS #\n")

frase = str(input("Digite uma frase: ")).upper()
divide = frase.split()
junta = "".join(divide)
palindromo = ""
# palindromo2 = junto[::-1] - só esse comando já traz o inverso. Ele pega do início ao fim[:] de trás pra frente[-1].
for i in range(len(junta)-1, -1, -1):
    palindromo += junta[i]
    print(palindromo)
print("\n",junta, palindromo)
if junta == palindromo:
    print("A frase digitada É UN PALÍNDROMO!")
else:
    print("A frase digitada NÃO É UM PALÍNDROMO")

'''EXPLICAÇÃO DO FOR:
for i in range(len(junta)-1, -1, -1): Quando é número (vide teste abaixo), ele pega o valor absoluto 15. Por isso ele 
conta do 15 ao 1. Coloca o -1 para contar até o 0. Quando é string, ele conta o índice e não a quantidade de caracteres,
desta forma uma palavra de 15 letras o início dela será o 0 se for crescente, ou 14 se for decrescente. Assim quando se
manda contar uma string deve diminuir 1 para cair na posição correta do índice( letra 1/índice 0, letra 2/índice 1,
letra 3/índice 2, letra 4/índice3...)'''


'''TESTANDO CONTADOR DECRESCIVO
for i in range (15,0,-1):
    print(i, end=" ")'''