# Solução matemática

num = int(input("\nInforme um número qualquer entre 0 e 9999: "))
print(f"Unidade: {num // 1 % 10}")
print(f"Dezena: {num // 10 % 10}")
print(f"Centena: {num // 100 %10}")
print(f"Milhar: {num //1000 }")

# Solução por divisão de "string", porém da erro se digitar um número que não tenha 4 dígitos

'''num = int(input("\nInforme um número de 0 à 9999: "))
n = str(num) # "Covertendo" uma variável tipo int em string
print(f"Unidade: {n[3]}")
print(f"Dezena: {n[2]}")
print(f"Centena: {n[1]}")
print(f"Milhar: {n[0]}")'''
