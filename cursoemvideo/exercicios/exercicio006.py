'''num = int(input("\nInforme um número: "))
dob = num * 2
trip = num * 3
raiz = num**(1/2)

print(f"O número informado é: {num};\nO seu dobro é: {dob};\nO seu triplo é: {trip};\nA sua raíz quadrada é: {raiz}")'''

# solução do professor (caso não vá se usar as variáveis)

num = int(input("\nInforme um número: "))
print(f"O número informado é: {num}.\nO dobro de {num} é: {num * 2}.\nO triplo de {num} é: {num * 3}."
      f"\nA raíz quadrada de {num} e: {num ** (1/2):.2f}")

# Outra forma de calcular potenciação é usar a função pow(variável,(expoente))
# Ex:
num2 = int(input("\nInforme um número: "))
print(f"A raíz do número {num2} é: {pow(num2,(1/2)):.2f}")
