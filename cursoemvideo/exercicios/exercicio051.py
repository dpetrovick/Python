print("\n # PROGRESSÃO ARITIMÉTICA (10 NÚMEROS) #\n")

# Fórmula da PA = {a + [r* (n-1)]}, onde: a = número inicial; r = intervalo, n = posição final
# Sequência: (a, a+r, a+2r, a+3r, a+4r, a+5r, a+6r, a+7r, a+8r, a+9r...), ou seja, 1º = a, 10º = a+9r

num = int(input("Informe o termo da PA: "))
raz = int(input("Informe a razão da PA: "))
posicao = num + (raz * (10-1)) # 10 - 1 é a posição final seria na fórmula acima (a + 9r)
print("="*72)

for i in range(num, posicao + raz, raz): # Explicação abaixo
    print(i, end=" --> ")

print("FIM")
print("="*72)

""" Como o índice é reduz 1 (for in range(1,10) conta de 1 a 9 o 10 n conta),por isso temos que somar mais uma raz
(razão), ao final do número para que de fato seja contado até a posição desejada. Seria como se fosse(for in range(1,11)
para o 10 aparecer"""
