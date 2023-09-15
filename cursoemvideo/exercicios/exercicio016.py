from math import trunc

num = float(input("\nInforme um número real qualquer: "))
print(f"A parte inteira do número {num}, é: {trunc(num)}") # o import é para este caso.
print(f"A parte inteira do número {num}, é: {int(num)}")
print(f"A parte inteira do número {num}, é: {num // 1:.0f}")
''' Se fizer o comando import math. No print deveria usar math.trunc(num). Mas como importei uma função específica, não
precisa colocar o "math." antes da função"'''

