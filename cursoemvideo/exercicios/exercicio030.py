num = int(input("\nInforme um número inteiro qualquer: "))
if num % 2:
    print(f"O número {num} digitado é ÍMPAR!!")
else:
    print(f"O número {num} digitado é PAR!!")

# solução do professor

num = int(input("\nInforme um número inteiro qualquer: "))
res = num % 2 # Armazana na variável "res", o resto da divisão do número (num) dividido por 2
if res == 0:
    print(f"O número {num} digitado é PAR!!")
else:
    print(f"O número {num} digitado é ÍMPAR!!")
